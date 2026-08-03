# AI Teacher

> An AI-powered educational platform that teaches students like a real teacher using Large Language Models (LLMs), Retrieval-Augmented Generation (RAG), and conversational AI.

----

## Overview

AI Teacher is an intelligent learning platform designed to provide personalized education for students.

Unlike traditional chatbots, AI Teacher understands educational content, remembers conversations, retrieves information from textbooks, and explains concepts using stories, analogies, and real-life examples.

The first MVP focuses on **CBSE Class 6 Science**, with an architecture that can later expand to all classes and subjects.

---

## Current Progress

### Backend

- FastAPI
- SQLAlchemy ORM
- SQLite Database
- JWT Authentication
- Password Hashing
- Student Registration
- Student Login
- Protected API Endpoints
- Modular Project Architecture

### AI

- OpenRouter Integration
- LLM Provider Layer
- System Prompt Engineering
- Conversation Memory
- Educational AI Teacher Prompt
- Startup-ready AI Architecture

### RAG (Retrieval-Augmented Generation)

- PDF Loader
- Automatic PDF Folder Loader
- Text Chunking
- Embedding Generation
- FAISS Vector Database

### Knowledge Base

Current Knowledge Source

- CBSE
- Class 6
- Science
- NCERT Textbook PDF

---

# Current Architecture

```text
Student

        │
        ▼

FastAPI API

        │
        ▼

Chat Router

        │
        ▼

Chat Service

        │
        ▼

Conversation Memory

        │
        ▼

LLM Provider

        │
        ▼

OpenRouter

        │
        ▼

Qwen LLM
```

---

# RAG Pipeline

```text
NCERT Science Book

        │
        ▼

PDF Loader

        │
        ▼

Text Extraction

        │
        ▼

Text Chunking

        │
        ▼

Embeddings

        │
        ▼

FAISS Vector Store

        │
        ▼

Semantic Search

        │
        ▼

LLM

        │
        ▼

Accurate Educational Response
```

---

# Folder Structure

```text
AI-Teacher
│
├── backend
│   │
│   ├── app
│   │   ├── core
│   │   ├── llm
│   │   ├── memory
│   │   ├── prompts
│   │   ├── rag
│   │   ├── routers
│   │   ├── schemas
│   │   ├── services
│   │   ├── models
│   │   ├── database.py
│   │   └── main.py
│   │
│   ├── knowledge_base
│   │   └── cbse
│   │       └── class6
│   │           └── science
│   │
│   ├── ai_teacher.db
│   └── requirements.txt
│
└── frontend
```

---

# Features Completed

## Authentication

- Student Registration
- Student Login
- JWT Authentication
- Password Hashing
- Secure APIs

---

## AI Chat

- OpenRouter Integration
- Educational System Prompt
- Context-aware Conversations
- Conversation Memory

---

## Educational Prompt

The AI Teacher can:

- Teach Mathematics
- Teach Science
- Teach English
- Teach Computer Science
- Teach Artificial Intelligence
- Explain concepts using stories
- Use real-world analogies
- Give step-by-step explanations
- Adapt explanations for beginners
- Generate programming examples

---

## RAG Components

Implemented

- PDF Loading
- Folder-based PDF Discovery
- Text Extraction
- Character-based Chunking
- Embedding Generation
- FAISS Vector Storage

---

# Tech Stack

## Backend

- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- JWT
- Passlib
- Uvicorn

---

## AI

- OpenRouter
- OpenAI SDK
- Qwen
- Prompt Engineering

---

## RAG

- PyPDF
- Sentence Transformers
- BAAI/bge-small-en-v1.5
- FAISS

---

## Version

Current Version

```
v0.3.0
```

---

# Roadmap

## Phase 1 (Completed)

- Backend Architecture
- Authentication
- Student Module
- AI Integration
- Conversation Memory
- PDF Loading
- Chunking
- Embeddings
- FAISS

---

## Phase 2 (In Progress)

- Complete RAG Pipeline
- Semantic Search
- Source Citation
- NCERT-based Answers

---

## Phase 3

- React Frontend
- Student Dashboard
- AI Chat Interface
- Chapter Navigation

---

## Phase 4

- Quiz Generator
- Notes Generator
- Flashcards
- Homework Generator

---

## Phase 5

- Voice AI
- Speech-to-Text
- Text-to-Speech
- Voice Tutor

---

## Phase 6

- Vision AI
- OCR
- Diagram Understanding
- Image Question Answering

---

## Phase 7

- Teacher Dashboard
- Admin Dashboard
- Analytics
- Student Progress

---

## Phase 8

- Docker
- Cloud Deployment
- CI/CD
- Production Database

---

# Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/AI-Teacher.git
```

Go to project

```bash
cd AI-Teacher/backend
```

Create virtual environment

```bash
python -m venv venv
```

Activate

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run server

```bash
uvicorn app.main:app --reload
```

Open Swagger

```
http://127.0.0.1:8000/docs
```

---

# Current Status

✅ Backend Foundation Complete

✅ Authentication Complete

✅ AI Integration Complete

✅ Conversation Memory Complete

✅ PDF Processing Complete

✅ Text Chunking Complete

✅ Embedding Generation Complete

✅ FAISS Vector Database Complete

🚧 Semantic Retrieval (In Progress)

🚧 Complete RAG Pipeline (In Progress)

🚧 React Frontend (Upcoming)

---

# Long-Term Vision

Build an AI-powered education platform that provides personalized learning experiences through conversational AI, Retrieval-Augmented Generation, and multimodal interaction. The platform is designed to scale from a single CBSE Class 6 Science textbook to support multiple boards, grades, subjects, and learning styles while maintaining production-ready architecture suitable for real-world deployment.
