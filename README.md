📚 Student Assistance RAG Chatbot

A Retrieval-Augmented Generation (RAG) based Academic Chatbot built using Flask, LangChain, HuggingFace Transformers, and ChromaDB.
This project allows students to ask questions from uploaded PDF study materials, and the chatbot answers only from the given documents.

🚀 Features

📄 Load academic PDFs as knowledge source

🔍 Semantic search using vector embeddings

🤖 Context-aware answers using RAG architecture

🌐 REST API using Flask

🧠 Uses HuggingFace FLAN-T5 model

💾 Persistent vector storage using ChromaDB

🛠️ Tech Stack

Python 3.10+

Flask

LangChain

HuggingFace Transformers

ChromaDB

Sentence Transformers (MiniLM)

PyPDFLoader

📂 Project Structure
student_assistance_rag/
│
├── app.py            # Flask API for chatbot
├── chatbot.py        # RAG pipeline and chatbot logic
├── ingest.py         # PDF ingestion and chunking
├── test_flask.py     # Flask test file
├── data/             # Folder to store PDF files
├── db/               # Chroma vector database
├── requirements.txt
└── README.md

⚙️ Installation & Setup
1️⃣ Create Virtual Environment
python -m venv rag_env
rag_env\Scripts\activate   # Windows

2️⃣ Install Dependencies
pip install -r requirements.txt

📥 Add Study Materials (PDFs)

Create a folder named data/

Place all your academic PDF files inside it

Example:

data/
├── python_notes.pdf
├── ml_basics.pdf

🧩 Ingest PDFs into Vector Database

Run:

python ingest.py


This will:

Load PDFs

Split text into chunks

Prepare data for vector storage

🤖 Run the Chatbot (Terminal Mode)
python chatbot.py


Example:

Ask: What is Python?
Ask: Explain machine learning

🌐 Run Flask API
python app.py


API Endpoint:

POST /chat

Sample Request (JSON):
{
  "query": "What is machine learning?"
}

Sample Response:
{
  "answer": "Machine learning is ..."
}

🧪 Test Flask Server
python test_flask.py


Open browser:

http://127.0.0.1:5000/


Output:

Flask is working!

🧠 RAG Architecture Used

PDF Loader – Loads academic PDFs

Text Splitter – Breaks text into chunks

Embeddings – Converts text into vectors

Vector Store – ChromaDB

Retriever – Fetches relevant context

LLM – FLAN-T5 generates final answer

📌 Future Improvements

Add frontend (React / HTML UI)

User authentication

Multiple document categories

Better UI for uploads

Cloud deployment

👨‍🎓 Author

Sujith
B.Tech – Artificial Intelligence & Data Science
Student Assistance RAG Chatbot Project
