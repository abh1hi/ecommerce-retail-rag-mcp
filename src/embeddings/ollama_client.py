import os, requests
OLLAMA_URL = os.getenv("OLLAMA_URL","http://localhost:11434")

# Placeholder: if Ollama exposes embeddings for gemma3:270m, implement here.
# Else, swap in a sentence-embedding model and keep Gemma for generation.

def embed_text(text: str):
    raise NotImplementedError("Implement embedding backend for query/doc vectors")

def generate_answer(prompt: str) -> str:
    r = requests.post(f"{OLLAMA_URL}/api/generate", json={
        "model":"gemma3:270m",
        "prompt": prompt,
        "stream": False
    })
    r.raise_for_status()
    return r.json().get("response","")
