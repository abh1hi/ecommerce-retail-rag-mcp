# MCP Architecture Diagram: Retail RAG System Tool Integration (Mermaid, with ADK)

```mermaid
flowchart TB
  subgraph Host[Host / Client Layer]
    GW[API Gateway / App]
    AUTH[AuthN/Z & Consent]
    SESS[Session & Context Store]
  end

  subgraph ADK[Google ADK]
    AG[RetailRAGAgent/Workflows]
    TOOLS[ADK Tools: VectorSearch, Generate, MCP Tool Wrappers]
  end

  subgraph Protocol[MCP Protocol]
    INIT[Initialize]
    CALL[Tool Call]
    RESP[Tool Response]
    ERR[Error/Retry]
  end

  subgraph Servers[MCP Servers]
    REG[Tool Registry & Routing]
    SRV1[product_search]
    SRV2[inventory_check]
    SRV3[policy_qa]
    SRV4[analytics_query]
    LOG[Observability: Logs/Metrics/Tracing]
  end

  subgraph Data[External / Data Systems]
    CAT[ChromaDB (Vectors)]
    INV[Inventory/Orders]
    POL[Policies/FAQs]
    DWH[Analytics Warehouse]
    OLM[Ollama (Gemma3:270m)]
  end

  GW --> AUTH --> SESS --> AG
  AG --> TOOLS
  TOOLS --> OLM
  TOOLS --> CAT
  TOOLS --> REG
  GW --> INIT --> REG
  REG --> CALL --> SRV1 & SRV2 & SRV3 & SRV4
  SRV1 --> CAT
  SRV2 --> INV
  SRV3 --> POL
  SRV4 --> DWH
  SRV1 & SRV2 & SRV3 & SRV4 --> RESP --> GW
  SRV1 & SRV2 & SRV3 & SRV4 --> LOG
  CALL --> ERR --> CALL
```
