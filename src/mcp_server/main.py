from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os

app = FastAPI(title="Retail RAG MCP Server")

class ToolCall(BaseModel):
    method: str
    params: dict

@app.get("/healthz")
def healthz():
    return {"status": "ok"}

@app.post("/mcp/tools/call")
async def tools_call(payload: ToolCall):
    name = payload.params.get("name")
    args = payload.params.get("arguments", {})

    if name == "product_search":
        # TODO: implement
        return {"results": []}
    raise HTTPException(status_code=404, detail=f"unknown tool: {name}")
