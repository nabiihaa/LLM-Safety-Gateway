# LLM Safety Gateway (MVP)

A lightweight, real-time gateway that analyzes and sanitizes prompts before they reach an LLM.

## Features
- FastAPI-based HTTP gateway
- Rule-based prompt injection detection
- Token counting using `tiktoken`
- HTML/script sanitization
- Extensible architecture
- Minimal test suite

## Run locally

```bash
pip install -r requirements.txt
./run.sh
