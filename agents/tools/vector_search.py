from adk.tools import Tool
from src.rag.vector_store import query as vdb_query
from src.embeddings.ollama_client import embed_text

class VectorSearchTool(Tool):
    def __init__(self, k=10):
        self.k = k

    async def call(self, ctx):
        q = ctx.state["query"]
        qv = embed_text(q)
        res = vdb_query(qv, k=self.k)
        docs = []
        for i, txt in enumerate(res.get("documents", [[]])[0]):
            md = res.get("metadatas", [[]])[0][i]
            docs.append({"text": txt, "meta": md})
        ctx.state["docs"] = docs
        return {"count": len(docs)}
