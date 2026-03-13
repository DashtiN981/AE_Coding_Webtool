# AE Coding Webtool

Python scripts for MedDRA adverse event coding using embedding-based retrieval and LLM-assisted prediction.

## Overview

This repository contains scripts for:

- generating embeddings for adverse event (AE) terms
- generating embeddings for LLT dictionary terms
- testing chat completion models through an OpenAI-compatible API
- running a retrieval-augmented generation (RAG) pipeline for MedDRA coding

## Workflow

The recommended workflow is:

1. Create AE embeddings
2. Create LLT embeddings
3. Test the API connection
4. Run the RAG pipeline

## Project Structure

- `embed_ae_local.py` — generate AE embeddings
- `embed_llt_local.py` — generate LLT embeddings
- `RAGPipeline.py` — main RAG-based coding pipeline
- `Basic_Chat_Completion.py` — API test script
- `data/` — input datasets and dictionaries
- `embedding/` — generated embedding JSON files
- `model_outputs/` — saved prediction outputs

## Requirements

- Python 3.10+
- pip
- a virtual environment is recommended

## Installation

```bash
git clone <your-repo-url>
cd AE_Coding_Webtool
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt

## Configuration
This project uses an OpenAI-compatible API endpoint.
Store your credentials in environment variables or a local .env file instead of hardcoding them in the code.
Example:

OPENAI_API_KEY=your_api_key_here
OPENAI_BASE_URL=your_base_url_here
MODEL_NAME=your_model_name_here

##Usage
1. Create AE embeddings
python .\embed_ae_local.py
2. Create LLT embeddings
python .\embed_llt_local.py
3. Test API connection
python .\Basic_Chat_Completion.py
4. Run the RAG pipeline
python .\RAGPipeline.py

##Input Files
The scripts expect files such as:
    ./data/AE_mock_dataset.xlsx
    ./data/AE_mock_dataset.csv
    ./data/Excel files/LLT2_Code_Deutsch_25_0.xlsx
    ./data/<LLT dictionary>.csv
    ./data/<PT dictionary>.csv

## Output Files
Typical outputs include:
    ./embedding/ae_embeddings.json
    ./embedding/llt2_deutsch_embeddings.json
    ./model_outputs/*.json

## Notes
Create both AE and LLT embeddings before running the main RAG pipeline.
Do not commit API keys or private datasets.
It is recommended to exclude .venv, .env, and generated output files from Git tracking