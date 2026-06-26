import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi
from sentence_transformers import SentenceTransformer
import psycopg2
from pgvector.psycopg2 import register_vector
from openai import OpenAI
from dotenv import load_dotenv
import os

def chunkText(text):
    chunks = []
    size = 700

    for i in range(0,len(text),size):
        chunks.append(text[i:i+size])
    
    return chunks

@st.cache_resource
def loadmodel():
    return SentenceTransformer("all-MiniLM-L6-v2")

def createEmbedding(chunks):
    return model.encode(chunks)

def ConnectDB():
    load_dotenv()

    conn = psycopg2.connect(
        host = os.getenv("DB_HOST"),
        database = os.getenv("DB_NAME"),
        user = os.getenv("DB_USER"),
        password = os.getenv("DB_PASSWORD"),
        port = os.getenv("DB_PORT") ,
        sslmode = "require"
    )

    register_vector(conn)

    return conn

def getVideoId(url):
    if "youtu.be" in url:
        return (url.split("youtu.be/")[1]).split("?")[0]
    elif "v=" in url:
        return (url.split("v=")[1]).split("&")[0]
    else:
        raise ValueError("Invalid YouTube URL")

@st.cache_data
def getTranscript(url):
    videold = getVideoId(url)
    #st.write(f"Video ID: {videold}")
    
    try:
        transcript = YouTubeTranscriptApi()
        
        data = transcript.fetch(videold , languages = ["en"])
        text = "".join([row.text for row in data])

        return text
    except Exception as e:
        raise ValueError(f"Transcript Unavailable: {str(e)}")

def replaceTranscript(chunks,vectors,url):
    con = ConnectDB()
    cur = con.cursor()

    try:
        cur.execute(
        """
            TRUNCATE TABLE transcript
            RESTART IDENTITY
        """
        )

        for chunk,vector in zip(chunks,vectors):
            cur.execute(
            """
                INSERT INTO transcript (
                video_url ,
                chunk_text ,
                embedding
                ) VALUES ( %s , %s , %s)
            """ , (url , chunk , vector )
            )

            con.commit()
    
    finally:
        cur.close()
        con.close()

def findRelatedVector(questionVector):
    con = ConnectDB()
    cur = con.cursor()

    try:
        cur.execute(
        """
           SELECT chunk_text FROM transcript ORDER BY 
           embedding <=> %s::vector
           LIMIT 3
        """ , (questionVector ,))
        return cur.fetchall()
    finally:
        cur.close()
        con.close()

@st.cache_resource
def initModel():
    load_dotenv()

    Client = OpenAI( api_key = os.getenv("API_KEY") , base_url = "https://openrouter.ai/api/v1")

    return Client

def generatePrompt( related , question):
    prompt = f"""Answer the question only based on the Context.
    Context:
    {related} 
    
    Question: 
    
    {question} 
    """

    return prompt

def askAI(question):
    questionVector = createEmbedding(question)

    related = findRelatedVector(questionVector)

    prompt = generatePrompt(related , question)

    response = client.chat.completions.create( model = "openrouter/free" ,
    messages = [
        {
            "role" : "user" , 
            "content" : prompt }])
    
    return response.choices[0].message.content


model = loadmodel()
client = initModel()

if "processed" not in st.session_state:
    st.session_state.processed = False

st.title("YouTube Transcript RAG")

url = st.text_input("Enter YouTube Video URL")

if st.button("Process"):
    with st.spinner("Processing..."):
        if url:
            try:
                transcript = getTranscript(url)

                chunks = chunkText(transcript)

                vectors = createEmbedding(chunks)

                replaceTranscript(chunks , vectors , url)

                st.success("Video processed successfully!")

                st.session_state.processed = True
                
            except Exception as e:
                st.error(f"Error processing the video: {str(e)}")
            
        else:
            st.error("Please enter a YouTube video URL.")

    
if st.session_state.processed:
    st.subheader("Ask a question about the video")

    question = st.text_input("Enter your question")

    if st.button("Ask"):
        with st.spinner("Getting answer..."):
            if question.strip():
                try:
                    answer = askAI(question)

                    st.subheader("Answer:")
                    st.success(answer)
                
                except Exception as e:
                    st.error(f"Error getting the answer: {str(e)}")
            
            else:
                st.error("Please enter a question.")

