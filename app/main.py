from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from app.rules import is_prompt_injection
from app.tokenizer_utils import count_tokens
from app.sanitizer import sanitize_text
from app.forwarder import forward_to_llm

app = FastAPI(title="LLM Safety Gateway MVP")

class PromptIn(BaseModel):
    prompt: str

@app.get("/")
def home():
    return {"message": "LLM Safety Gateway is running!"}

@app.post("/analyze")
def analyze_prompt(payload: PromptIn):
    prompt = payload.prompt

    # 1. Sanitize
    cleaned = sanitize_text(prompt)

    # 2. Token limit
    if count_tokens(cleaned) > 4000:
        raise HTTPException(status_code=400, detail="Prompt too long")

    # 3. Rule-based detection
    if is_prompt_injection(cleaned):
        return {"status": "blocked", "reason": "Possible prompt injection"}

    # 4. Forward (stub)
    model_response = forward_to_llm(cleaned)

    return {"status": "ok", "sanitized_prompt": cleaned, "model_response": model_response}
