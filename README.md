# 🎥 YouTube RAG (Retrieval-Augmented Generation)

An AI-powered application that allows users to ask questions about any YouTube video by extracting its transcript, generating semantic embeddings, storing them in a vector database, and using an LLM to generate accurate context-aware answers.

---

## 🚀 Live Demo

🔗 Live Application: 
https://you-tube-rag.streamlit.app

📂 GitHub Repository: https://github.com/iamGokulraja/You-Tube-RAG

---

## 📖 Project Overview

YouTube RAG is a Retrieval-Augmented Generation (RAG) application built using Python, Streamlit, Sentence Transformers, pgvector, PostgreSQL, and OpenRouter LLM.

Instead of sending the entire transcript to the AI model, the application:

1. Extracts the YouTube transcript.
2. Splits the transcript into smaller chunks.
3. Converts each chunk into vector embeddings.
4. Stores embeddings in PostgreSQL using pgvector.
5. Retrieves only the most relevant chunks based on the user's question.
6. Sends only the relevant context to the LLM.
7. Generates an accurate answer grounded in the video content.

This makes the system faster, scalable, and more cost-efficient.

---

## Features 📊

- 🎥 Process any YouTube video with English subtitles
- 📝 Automatically fetch video transcript
- ✂️ Smart transcript chunking
- 🧠 Generate embeddings using Sentence Transformers
- 🗄 Store embeddings in PostgreSQL (pgvector)
- 🔍 Semantic similarity search
- 🤖 AI-powered question answering
- ⚡ Fast Streamlit web interface
- ☁️ Cloud deployment using Streamlit Community Cloud

---

## 🛠 Tech Stack

### Frontend

- Streamlit

### Backend

- Python

### AI / Machine Learning

- Sentence Transformers
- all-MiniLM-L6-v2

### Vector Database

- PostgreSQL
- pgvector

### LLM

- OpenRouter API

### Libraries

- youtube-transcript-api
- psycopg2
- pgvector
- python-dotenv
- OpenAI Python SDK

---

## 🏗 System Architecture

YouTube URL
      │
      ▼
Fetch Transcript
      │
      ▼
Chunk Transcript
      │
      ▼
Generate Embeddings
      │
      ▼
Store in PostgreSQL + pgvector
      │
      ▼
User Question
      │
      ▼
Generate Question Embedding
      │
      ▼
Similarity Search
      │
      ▼
Retrieve Relevant Chunks
      │
      ▼
OpenRouter LLM
      │
      ▼
Final Answer

---

## 📂 Project Structure

You-Tube-RAG/
│
├── app.py
├── requirements.txt
├── .env
├── README.md
└── assets/

---

## ⚙ Installation

Clone Repository

git clone https://github.com/iamGokulraja/You-Tube-RAG.git

cd You-Tube-RAG

---

## Create Virtual Environment

python -m venv venv

Activate it

Windows

venv\Scripts\activate

Linux / macOS

source venv/bin/activate

---

Install Dependencies

pip install -r requirements.txt

---

## Environment Variables

Create a ".env" file.

API_KEY=your_openrouter_api_key

DB_HOST=your_host
DB_NAME=your_database
DB_USER=your_username
DB_PASSWORD=your_password
DB_PORT=5432

---

## Run the Project

streamlit run app.py

---

## 📚 How It Works

Step 1

Enter a YouTube video URL.

Step 2

The application extracts the transcript.

Step 3

The transcript is divided into smaller chunks.

Step 4

Sentence Transformer generates vector embeddings.

Step 5

Embeddings are stored inside PostgreSQL using pgvector.

Step 6

User asks a question.

Step 7

The question is converted into an embedding.

Step 8

The most similar transcript chunks are retrieved.

Step 9

Only the relevant context is sent to the LLM.

Step 10

The AI generates the final answer.

---

## 💡 Why RAG?

Instead of sending an entire transcript to an LLM, Retrieval-Augmented Generation (RAG):

- Reduces token usage
- Improves response accuracy
- Retrieves only relevant information
- Makes applications scalable
- Reduces API costs

---

## 🔮 Future Improvements

- Support multilingual transcripts
- Upload local video files
- Process multiple videos simultaneously
- Conversation history
- Chat memory
- PDF export
- Better chunking strategy
- Streaming AI responses
- User authentication

---

# 👨‍💻 Author

## Gokul Raja

Electronics and Communication Engineering Student

Passionate about AI, Full Stack Development, Machine Learning, and Generative AI.

---

⭐ Support

If you found this project helpful,

⭐ Star this repository


📝 Share your feedback

---

## 📄 License

This project is licensed under the MIT License.
