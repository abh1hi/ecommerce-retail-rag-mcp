# Data Flow Diagram: E-commerce RAG Pipeline (Mermaid)

```mermaid
flowchart LR
  subgraph Client
    U[User Query]
  end

  subgraph API
    N[Normalization & Lang Detect]
    JR[Join Runtime Context]
  end

  subgraph Embedding
    E[Gemma3:270m (Ollama)\nQuery Embedding]
  end

  subgraph VectorDB[ChromaDB]
    Q[Vector Search\n+ Metadata Filters]
    R[Rerank / Score Merge]
  end

  subgraph Augment
    C[Context Builder\n(top-k chunks)]
  end

  subgraph Gen[Generation]
    G[Gemma3:270m (Ollama)\nGrounded Answer]
  end

  subgraph MCP[MCP Tool Layer]
    T1[product_search]
    T2[inventory_check]
    T3[policy_qa]
    T4[analytics_query]
  end

  U --> N --> E --> Q --> R --> C --> G -->|Response| U
  C -->|Insufficient Context?| D{Enough Context?}
  D -- No --> T1 & T2 & T3 & T4 --> JR --> C
  D -- Yes --> G

  classDef stage fill:#eef,stroke:#88f,stroke-width:1px;
  class API,Embedding,VectorDB,Augment,Gen,MCP stage;
```
