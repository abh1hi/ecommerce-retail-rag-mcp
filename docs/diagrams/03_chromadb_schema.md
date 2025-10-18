# ChromaDB Schema and Data Ingestion Architecture

![ChromaDB Schema](../charts/chromadb_schema.png)

## Description
Shows how external data (catalogs, reviews, policies, tickets, inventory) are normalized, chunked, embedded (via Gemma3:270m/Ollama or a dedicated embedder), and stored in ChromaDB collections. Explicit metadata and vector structure illustrated. Ingest and query flow arrows connect all stages.