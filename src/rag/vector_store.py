from typing import List, Dict, Any
import os
import chromadb

CHROMA_HOST = os.getenv("CHROMA_HOST","localhost")
CHROMA_PORT = int(os.getenv("CHROMA_PORT","8001"))

_client = None

def get_client():
    global _client
    if _client is None:
        _client = chromadb.HttpClient(host=CHROMA_HOST, port=CHROMA_PORT)
    return _client

def get_collection(name: str="catalog_chunks"):
    return get_client().get_or_create_collection(name)

def upsert(id: str, embedding: List[float], text: str, metadata: Dict[str,Any]):
    col = get_collection()
    col.upsert(ids=[id], embeddings=[embedding], documents=[text], metadatas=[metadata])

def query(query_embedding: List[float], k: int=10):
    col = get_collection()
    return col.query(query_embeddings=[query_embedding], n_results=k)
