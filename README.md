# SHL Assessment Recommendation API

A Retrieval-Augmented Generation (RAG) based conversational recommendation system that recommends the most relevant SHL assessments from the provided SHL assessment catalog.

The application uses semantic search over the SHL catalog and Gemini for conversation understanding and response generation. Recommendations are generated **only from the provided SHL catalog**, without relying on general knowledge.

---

## Features

- Multi-turn conversational recommendation
- Semantic retrieval using Sentence Transformers
- ChromaDB vector database
- FastAPI REST API
- Conversation intent and context extraction
- Recommendation, clarification and comparison support
- Uses only the provided SHL assessment catalog

---

## System Architecture

```
                   User
                     │
                     ▼
              FastAPI REST API
                     │
                     ▼
         Conversation Analyzer (Gemini)
                     │
                     ▼
             Decision Engine
                     │
         ┌───────────┴───────────┐
         ▼                       ▼
 Clarification Needed?      Semantic Retrieval
         │                       │
         │                 SentenceTransformer
         │                       │
         │                  ChromaDB Index
         │                       │
         └───────────────┬───────────────┘
                         ▼
             Response Generator (Gemini)
                         │
                         ▼
                  JSON Response
```

---

## RAG Pipeline

```
catalog.json
      │
      ▼
Document Builder
      │
      ▼
SentenceTransformer
(all-MiniLM-L6-v2)
      │
      ▼
ChromaDB
      │
      ▼
Semantic Search
      │
      ▼
Top Matching SHL Assessments
      │
      ▼
Gemini Response Generation
```

---

## Tech Stack

### Backend

- FastAPI
- Python

### Vector Database

- ChromaDB

### Embeddings

- sentence-transformers
- all-MiniLM-L6-v2

### LLM

- Google Gemini 2.5 Flash

### Other Libraries

- requests
- python-dotenv

---

## Project Structure

```
.
├── app.py
├── config.py
├── requirements.txt
├── README.md
├── data/
│   └── catalog.json
├── chroma_db/
├── services/
│   ├── conversation_analyzer.py
│   ├── decision_engine.py
│   ├── document_builder.py
│   ├── recommendation_service.py
│   ├── response_generator.py
│   └── retriever.py
├── scripts/
│   ├── build_index.py
│   └── inspect_catalog.py
└── tests/
```

---

## Installation

Clone the repository

```bash
git clone <repository-url>
cd <repository-name>
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate it

Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root.

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

---

## Build Vector Index

If `chroma_db` is not present, generate it using

```bash
python -m scripts.build_index
```

---

## Run the API

```bash
uvicorn app:app --reload
```

Swagger documentation

```
http://127.0.0.1:8000/docs
```

---

## API Endpoints

### Health Check

```
GET /health
```

Response

```json
{
  "status": "ok"
}
```

---

### Chat

```
POST /chat
```

Example Request

```json
{
  "messages": [
    {
      "role": "user",
      "content": "I need an assessment for hiring a Java developer."
    }
  ]
}
```

Example Response

```json
{
  "reply": "Here are the most suitable assessments...",
  "recommendations": [
    {
      "name": "Java 8 (New)",
      "url": "https://www.shl.com/..."
    }
  ],
  "end_of_conversation": false
}
```

---

## AI Usage

AI was used in the following components:

### Conversation Analysis

Gemini extracts

- user intent
- job role
- seniority
- assessment category
- conversation context

### Response Generation

Gemini generates concise, natural language responses using only the retrieved SHL assessments.

### Retrieval

The retrieval pipeline **does not use the LLM**.

Semantic retrieval is performed using

- SentenceTransformer embeddings
- ChromaDB vector similarity search

This ensures recommendations are grounded entirely in the provided SHL assessment catalog.

---

## Design Decisions

- Modular service-based architecture
- Retrieval-Augmented Generation (RAG)
- Semantic search over SHL catalog
- Stateless REST API
- Separation between retrieval and generation
- LLM restricted to reasoning over retrieved context only

---

## Current Capabilities

- Recommend assessments
- Ask clarification questions
- Handle multi-turn conversations
- Retrieve semantically relevant SHL assessments
- Generate grounded recommendations

---

## Future Improvements

- Better comparison between assessments
- Support for conversation memory
- Metadata-based reranking
- Hybrid keyword + semantic retrieval
- Improved recommendation explanations

---

## License

MIT License