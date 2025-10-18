# Data Flow Diagram: E-commerce RAG Pipeline (Mermaid, with ADK)

```mermaid
flowchart LR
  subgraph Client
    U[User Query]
  end

  subgraph ADK[Google ADK Orchestration]
    AG[RetailRAGAgent (Sequential)]
    VS[VectorSearchTool]
    GT[GenerateTool]
  end

  subgraph API[FastAPI MCP Server]
    N[Normalize/Lang Detect]
    JR[Join Runtime Context]
  end

  subgraph Embedding
    E[embed_text\n(Ollama Gemma3 embeddings or\nsentence-embedder)]
  end

  subgraph VectorDB[ChromaDB]
    Q[Vector Search\n+ Metadata Filters]
    R[Rerank / Score Merge]
  end

  subgraph Augment
    C[Context Builder\n(top-k chunks)]
  end

  subgraph Gen[Generation]
    G[Ollama Gemma3:270m\nGrounded Answer]
  end

  subgraph MCP[MCP Tool Layer]
    T1[product_search]
    T2[inventory_check]
    T3[policy_qa]
    T4[analytics_query]
  end

  U --> AG --> N --> E --> Q --> R --> C --> G -->|Response| U
  AG -.calls.-> VS
  AG -.calls.-> GT
  C -->|Insufficient Context?| D{Enough Context?}
  D -- No --> T1 & T2 & T3 & T4 --> JR --> C
  D -- Yes --> G

  classDef stage fill:#eef,stroke:#88f,stroke-width:1px;
  class ADK,API,Embedding,VectorDB,Augment,Gen,MCP stage;
```
