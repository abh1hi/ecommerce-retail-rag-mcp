from adk.tools import Tool
from src.embeddings.ollama_client import generate_answer

GEN_TEMPLATE = """SYSTEM: Answer ONLY using CONTEXT. If insufficient, say so and ask one follow-up.
USER: {query}
CONTEXT:
{context}
STYLE: Concise, include SKU/IDs only if present, no hallucinations.
"""

class GenerateTool(Tool):
    def __init__(self, model="gemma3:270m"):
        self.model = model

    async def call(self, ctx):
        query = ctx.state["query"]
        context = ctx.state.get("context", "")
        prompt = GEN_TEMPLATE.format(query=query, context=context)
        out = generate_answer(prompt)
        ctx.output = {"answer": out}
        return ctx.output
