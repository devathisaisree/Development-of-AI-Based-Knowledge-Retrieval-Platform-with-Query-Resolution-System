# Development of AI-Based Knowledge Retrieval Platform with Query Resolution System

## Overview

This project is an AI-based knowledge retrieval and query resolution system designed to help users find information from uploaded documents.

Instead of manually searching through multiple documents, users can upload documents and ask questions in simple English. The system searches the relevant information from the documents and uses an AI language model to generate a useful response.

The project was developed as a B.Tech academic project to understand the practical use of Artificial Intelligence, Retrieval-Augmented Generation (RAG), embeddings, vector databases, and Large Language Models (LLMs).

---

## Problem Statement

Organizations and users often have information stored across many documents such as:

- HR policies
- Employee handbooks
- Technical documents
- FAQs
- Process guides
- Company-related documents

Finding a specific piece of information manually can be time-consuming.

This project aims to make document-based information retrieval easier by allowing users to upload documents and ask questions directly.

For example:

- What is the leave policy?
- What are the working hours?
- What is the process for applying leave?
- What does the employee handbook say about a particular topic?
- What is the procedure mentioned in a specific document?

The system retrieves relevant information and provides an AI-generated answer.

---

## Objectives

The main objectives of this project are:

- To upload and process documents.
- To extract useful information from documents.
- To generate embeddings from document content.
- To store embeddings in a vector database.
- To retrieve relevant information based on user queries.
- To use an AI language model to generate answers.
- To provide authentication for protected operations.
- To maintain conversation context during queries.
- To provide APIs for document upload and query resolution.
- To understand the practical implementation of a RAG-based application.

---

## Technologies Used

### Programming Language

- Python

### Backend

- FastAPI
- Uvicorn

### Artificial Intelligence

- Ollama
- Llama 3.2 1B

### Embedding Model

- mxbai-embed-large

### Vector Database

- ChromaDB

### Other Technologies

- LangGraph
- SQLAlchemy
- PostgreSQL
- Pydantic
- Gradio
- Git
- GitHub

---

## System Workflow

The basic working of the project is:

```text
User
↓
Upload Documents
↓
Document Processing
↓
Text Extraction
↓
Embedding Generation
↓
Store Embeddings in ChromaDB
↓
User Asks a Question
↓
Search Relevant Information
↓
Retrieve Relevant Document Content
↓
Send Retrieved Content to LLM
↓
Generate Final Answer
↓
Display Answer to User
```

## What is RAG?

RAG stands for Retrieval-Augmented Generation.

It combines information retrieval with a Large Language Model (LLM).

Instead of asking the AI model to answer a question only from its existing knowledge, the system first searches the uploaded documents for relevant information.

The retrieved information is then provided to the language model as context to generate the final answer.



## Project Structure

```text
AI-POWERED-QUERY-RESOLUTION-PROJECT/
│
└── AI-Powered-Intelligent-Query-Resolution-System/
    │
    ├── app/
    │   ├── api/
    │   │   ├── auth.py
    │   │   ├── upload.py
    │   │   └── query.py
    │   │
    │   ├── auth/
    │   ├── core/
    │   ├── database/
    │   ├── models/
    │   ├── rag/
    │   ├── agents/
    │   ├── llm/
    │   ├── transparency/
    │   ├── memory/
    │   ├── services/
    │   ├── schemas/
    │   └── ui/
    │
    ├── tests/
    ├── uploads/
    ├── docker/
    ├── dependencies.py
    ├── main.py
    ├── pyproject.toml
    ├── .env.example
    └── README.md
