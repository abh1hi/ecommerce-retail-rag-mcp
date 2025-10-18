# Data Flow Diagram: E-commerce RAG Pipeline

![Data Flow Diagram](../charts/ecommerce_rag_pipeline.png)

## Description
This diagram shows the complete data journey from user query through normalization, embedding, vector retrieval (ChromaDB), context augmentation, Gemma3:270m generation, MCP tool orchestration, and output back to the user. Branching is shown for insufficient context or tool API calls. Includes timing estimates per stage.

Core steps:
- Query input and normalization
- Embedding via Gemma3:270m served by Ollama
- ChromaDB vector/database retrieval (with filters)
- Context build and rerank
- Generation (Gemma3:270m, context-grounded)
- MCP integration points
- Output to user