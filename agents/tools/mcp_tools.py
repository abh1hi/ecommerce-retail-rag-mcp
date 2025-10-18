import os, httpx
from adk.tools import Tool

API_BASE = os.getenv("API_BASE", "http://localhost:8000")

class ProductSearchTool(Tool):
    async def call(self, ctx):
        async with httpx.AsyncClient() as ac:
            payload = {"method":"tools/call","params":{"name":"product_search","arguments":{"query":ctx.state["query"]}}}
            r = await ac.post(f"{API_BASE}/mcp/tools/call", json=payload)
            r.raise_for_status()
            ctx.state["mcp_product_results"] = r.json()
        return ctx.state["mcp_product_results"]

class InventoryCheckTool(Tool):
    async def call(self, ctx):
        async with httpx.AsyncClient() as ac:
            payload = {"method":"tools/call","params":{"name":"inventory_check","arguments":{"sku":ctx.state.get("sku")}}}
            r = await ac.post(f"{API_BASE}/mcp/tools/call", json=payload)
            r.raise_for_status()
            ctx.state["inventory"] = r.json()
        return ctx.state["inventory"]

class PolicyQATool(Tool):
    async def call(self, ctx):
        async with httpx.AsyncClient() as ac:
            payload = {"method":"tools/call","params":{"name":"policy_qa","arguments":{"query":ctx.state["query"]}}}
            r = await ac.post(f"{API_BASE}/mcp/tools/call", json=payload)
            r.raise_for_status()
            ctx.state["policy"] = r.json()
        return ctx.state["policy"]

class AnalyticsQueryTool(Tool):
    async def call(self, ctx):
        async with httpx.AsyncClient() as ac:
            payload = {"method":"tools/call","params":{"name":"analytics_query","arguments":{"range":"7d"}}}
            r = await ac.post(f"{API_BASE}/mcp/tools/call", json=payload)
            r.raise_for_status()
            ctx.state["analytics"] = r.json()
        return ctx.state["analytics"]
