# AI Structured Output Engine

Convert messy text into structured JSON using AI.

## Features
- Schema-driven outputs
- Multi-provider support
- JSON repair
- CLI + API

## Setup
pip install -r requirements.txt

## Run CLI
python -m app.cli --input "..." --schema "{}"

## Run API
uvicorn app.main:app --reload
