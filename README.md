# AE Coding Webtool

Python scripts for MedDRA adverse event coding using embedding-based retrieval and LLM-assisted prediction.

## Overview

This repository contains scripts for:

- generating embeddings for adverse event (AE) terms
- generating embeddings for LLT dictionary terms
- testing chat-completion models through an OpenAI-compatible API
- running a retrieval-augmented generation (RAG) pipeline for MedDRA coding

The workflow is based on embedding retrieval plus LLM reasoning.  
Before running the main RAG pipeline, you should first create both:

1. AE embeddings
2. LLT embeddings

using the scripts provided in the repository.

## Repository Structure

- `API_Test/` : simple API test scripts for chat completion
- `embedding/` : generated embedding JSON files
- `data/` : input datasets and dictionaries
- `embed_ae_local.py` : creates AE embeddings
- `embed_llt_local.py` : creates LLT embeddings
- `RAGPipeline.py`  : main RAG-based MedDRA coding pipeline

## Requirements

- Python 3.10+
- pip
- a virtual environment is recommended

## Installation

Clone the repository and create a virtual environment:

```bash
git clone <your-repo-url>
cd AE_Coding_Webtool
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
