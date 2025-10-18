# ChromaDB Schema and Data Ingestion Architecture (Mermaid)

```mermaid
flowchart TB
  subgraph Sources[Data Sources]
    S1[Product Catalog]
    S2[Reviews]
    S3[Policies/FAQs]
    S4[Support Tickets]
    S5[Inventory/Orders]
  end

  subgraph Ingest[Preprocess & Chunk]
    C1[Cleaning/Normalize]
    C2[Field-Aware Chunking]
    C3[Lang Tags/Metadata]
  end

  subgraph Embed[Embedding]
    E1[Gemma3:270m (or sentence-embedder)\nVectorize Chunks]
  end

  subgraph Chroma[ChromaDB Collections]
    CC1[catalog_chunks\nid, embedding(768), sku, field, lang, brand, category, price, stock, text]
    CC2[policy_chunks\nid, embedding, topic, lang, text]
    CC3[review_chunks\nid, embedding, sku, rating, lang, text]
    CC4[ticket_chunks\nid, embedding, customer_id, lang, text]
  end

  subgraph Query[Query Processing]
    Q1[Query Embedding]
    Q2[KNN + Filters]
    Q3[Rerank/Score Merge]
  end

  S1 & S2 & S3 & S4 & S5 --> C1 --> C2 --> C3 --> E1 --> CC1 & CC2 & CC3 & CC4
  Q1 --> Q2 --> Q3
  Q2 --> CC1 & CC2 & CC3 & CC4
```
