# Gemma3:270m Integration and Optimization Architecture (Mermaid)

```mermaid
flowchart LR
  subgraph Ollama[Ollama Server]
    M[Load gemma3:270m]
    EP1[/POST /api/generate/]
    EP2[/Embeddings (if available)/]
    CACH[Prompt/Response Cache]
    MON[Latency/Throughput Metrics]
  end

  subgraph Tasks[Task Routing]
    T1[Generation\n(answers, summaries)]
    T2[Query Rewriting]
    T3[Classification\n(intent/sentiment)]
    T4[Embedding\n(query/doc)]
  end

  subgraph Opt[Optimization]
    O1[Quantization\n(INT8/4)]
    O2[PEFT (LoRA/QLoRA)\n(if supported)]
    O3[Distillation\n(from larger teacher)]
    O4[Batching/Concurrency]
  end

  EP1 --> T1 & T2 & T3
  EP2 --> T4
  T1 & T2 & T3 & T4 --> CACH
  M --> O1 & O2
  T1 & T2 & T3 & T4 --> O4
  M --> MON
```
