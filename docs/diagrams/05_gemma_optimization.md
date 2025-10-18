# Gemma3:270m Integration and Optimization Architecture (Mermaid, with ADK Tools)

```mermaid
flowchart LR
  subgraph Ollama[Ollama Server]
    M[Load gemma3:270m]
    EP1[/POST /api/generate/]
    EP2[/Embeddings (if available)/]
    CACH[Prompt/Response Cache]
    MON[Latency/Throughput Metrics]
  end

  subgraph ADKTools[ADK Tools]
    GT[GenerateTool]
    VT[VectorSearchTool]
  end

  subgraph Opt[Optimization]
    O1[Quantization (INT8/4)]
    O2[PEFT (LoRA/QLoRA) if supported]
    O3[Distillation (teacher→SLM)]
    O4[Batching/Concurrency]
  end

  GT --> EP1
  VT --> EP2
  EP1 --> CACH
  EP2 --> CACH
  M --> O1 & O2
  GT & VT --> O4
  M --> MON
```
