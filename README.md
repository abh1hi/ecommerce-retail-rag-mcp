# E-commerce & Retail RAG with ADK + Gemma3:270m + Ollama + ChromaDB + MCP

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/) [![MCP](https://img.shields.io/badge/Protocol-MCP-green.svg)]() [![ADK](https://img.shields.io/badge/Google-ADK-orange.svg)]()

A production-ready blueprint for building a low-latency, grounded RAG system for retail using:
- Google ADK (Agent Development Kit) for orchestration (agents, tools, workflows, evaluation)
- Gemma3:270m served via Ollama for generation (32K context, lightweight)
- ChromaDB for vector search with metadata filtering
- FastAPI MCP server exposing retail tools (product_search, inventory_check, policy_qa, analytics_query)

## Architecture at a Glance
- ADK agent orchestrates: preprocess → retrieve (VectorSearchTool) → augment → generate (GenerateTool)
- Vector retrieval via ChromaDB; strict grounding in generation prompts
- MCP servers back tools for catalog/inventory/policy/analytics; host-enforced consent, schemas, RBAC

## Quickstart

### Option A: Docker Compose
```bash
docker compose up --build
```
Services:
- Ollama (pulls gemma3:270m on first run)
- ChromaDB (vector DB)
- FastAPI MCP server (http://localhost:8000)

### Option B: Python venv
```bash
bash scripts/setup_venv.sh
# in three terminals (or use dev_up_local.sh)
ollama serve & && ollama pull gemma3:270m
chroma start --host 0.0.0.0 --port 8001 &
uvicorn src.mcp_server.main:app --host 0.0.0.0 --port 8000 --reload
```

Run checks:
```bash
bash scripts/checks.sh
```

## Documentation Index
- Developer Guide: docs/developer-guide.md
- Developer Help Guide: docs/developer-help.md
- Testing Strategy: docs/testing-strategy.md
- ADK Integration: docs/adk-integration.md
- Comparison Tables: docs/comparison-tables.md
- Diagrams (Index): docs/diagrams/README.md
  - Data Flow: docs/diagrams/01_data_flow_diagram.md
  - MCP Architecture: docs/diagrams/02_mcp_architecture.md
  - ChromaDB Schema: docs/diagrams/03_chromadb_schema.md
  - Deployment: docs/diagrams/04_deployment_architecture.md
  - Gemma Optimization: docs/diagrams/05_gemma_optimization.md
  - Customer Journeys: docs/diagrams/06_customer_journeys.md

## Repo Layout
```
configs/           # env templates, config files
scripts/           # dev scripts (venv, compose, checks)
src/
  mcp_server/      # FastAPI MCP server
  rag/             # vector store adapter
  embeddings/      # ollama client (generate, TODO: embed_text)
agents/
  tools/           # ADK tools (vector search, generate, MCP wrappers)
  eval/            # ADK evaluation cases
  rag_agent.py     # Sequential RAG agent
  workflows.py     # example workflows
docs/
  diagrams/        # mermaid diagrams
```

## Next Steps
- Implement embed_text in src/embeddings/ollama_client.py (use Ollama embeddings if available; otherwise a sentence-embedder)
- Ingest catalogs/policies/reviews into Chroma (field-aware chunks)
- Flesh out MCP tools and schemas; enforce RBAC/rate limits
- Add reranker and evaluation harness (recall@k, groundedness)
- Wire metrics/logging/tracing, then stage and load-test
