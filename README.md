# AI Structured Output Engine

Convert messy input text into structured JSON using AI.

Supports:

* CLI-based structured generation
* API-based structured generation

---

## Features

* Convert unstructured text into structured JSON
* Schema-driven output generation
* Multi-provider support (OpenAI, Anthropic)
* JSON parsing with repair fallback
* Input validation and type enforcement
* CLI and API support
* Evaluation and optimization support

---

## Setup

```bash
git clone <repo_url>
cd ai-structured-output-engine
pip install -r requirements.txt
```

Create `.env` file:

```
PROVIDER=openai
MODEL=gpt-4o-mini

OPENAI_API_KEY=your_openai_key
ANTHROPIC_API_KEY=your_anthropic_key

MAX_INPUT_LENGTH=2000
```

For API based execution

```
uvicorn app.main:app --reload
Open Swagger UI - http://127.0.0.1:8000/docs
```

For CLI based execution
Run using the client cli.py with appropriate options

---

# Execution Modes

## Direct Mode (CLI)

Generate structured output using command line:

```
python -m app.cli --input "Login fails randomly" --schema "{\"problem\":\"\",\"root_causes\":[],\"impact\":\"\",\"priority\":\"\"}"
```

---

## Direct Mode (API)

Endpoint:

```
POST /generate
```

Sample request:

```
{
  "input": "Login fails randomly",
  "schema": {
    "problem": "",
    "root_causes": [],
    "impact": "",
    "priority": ""
  }
}
```

---

# CLI Options

| Option   | Description |
| -------- | ----------- |
| --input  | Input text  |
| --schema | JSON schema |

---

# Use Cases

* Structuring raw requirements
* Extracting structured insights from text
* Preprocessing inputs for agents or RAG systems
* Converting logs or feedback into actionable data
* Building structured pipelines for AI workflows

---

# Roadmap

* Add support for additional providers (Google, AWS)
* Add batch processing support
* Improve validation and type enforcement
* Add UI for easier interaction
* Enhance evaluation with semantic scoring

---

Built for speed, clarity, and real-world use
