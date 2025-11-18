
def forward_to_llm(prompt: str):
    # Later: call your real LLM here
    # For now we just echo back the text
    return f"[SAFE OUTPUT] {prompt}"
