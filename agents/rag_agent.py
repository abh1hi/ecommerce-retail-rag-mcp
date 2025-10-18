from adk.agents import Sequential
from adk.context import Context
from agents.tools.vector_search import VectorSearchTool
from agents.tools.generate import GenerateTool
from agents.tools.mcp_tools import ProductSearchTool, InventoryCheckTool, PolicyQATool, AnalyticsQueryTool

class RetailRAGAgent:
    def __init__(self):
        self.pipeline = Sequential(steps=[
            ("normalize", self.normalize),
            ("retrieve", VectorSearchTool(k=10)),
            ("augment", self.augment),
            ("generate", GenerateTool(model="gemma3:270m"))
        ])
        self.mcp = {
            "product_search": ProductSearchTool(),
            "inventory_check": InventoryCheckTool(),
            "policy_qa": PolicyQATool(),
            "analytics_query": AnalyticsQueryTool(),
        }

    async def normalize(self, ctx: Context):
        q = ctx.input.get("query", "")
        ctx.state["query"] = q.strip()

    async def augment(self, ctx: Context):
        docs = ctx.state.get("docs", [])
        ctx.state["context"] = "\n\n".join(d.get("text", "") for d in docs)

    async def run(self, query: str):
        return await self.pipeline.run({"query": query})
