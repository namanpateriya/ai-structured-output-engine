from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.service import generate_structured_output
from app.utils.logger import get_logger

logger = get_logger(__name__)

app = FastAPI(title="AI Structured Output Engine")


class Request(BaseModel):
    input: str
    schema: dict


@app.get("/")
def health():
    return {"status": "running"}


@app.post("/generate")
def generate(req: Request):
    if not req.input.strip():
        raise HTTPException(400, "Empty input")

    if not isinstance(req.schema, dict):
        raise HTTPException(400, "Invalid schema")

    return generate_structured_output(req.input, req.schema)
