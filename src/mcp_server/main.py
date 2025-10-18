from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import os

app = FastAPI(title="Retail RAG MCP Server")

class ToolCall(BaseModel):
    method: str
    params: dict

@app.get("/", response_class=HTMLResponse, include_in_schema=False)
def landing():
    return """
    <html>
      <head>
        <title>Retail RAG MCP Server</title>
        <meta charset=\"utf-8\" />
        <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
        <style>
          body { font-family: -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Arial, sans-serif; margin: 2rem; }
          h1 { margin-bottom: 0.25rem; }
          .muted { color: #666; margin-top: 0; }
          ul { line-height: 1.8; }
          code { background: #f6f8fa; padding: 2px 6px; border-radius: 4px; }
        </style>
      </head>
      <body>
        <h1>Retail RAG MCP Server</h1>
        <p class=\"muted\">ADK + Gemma3:270m (Ollama) + ChromaDB + FastAPI MCP</p>
        <h2>Health</h2>
        <ul>
          <li><a href=\"/healthz\">/healthz</a></li>
        </ul>
        <h2>API</h2>
        <ul>
          <li><code>POST /mcp/tools/call</code></li>
          <li><a href=\"/docs\">/docs</a> (Swagger UI, if enabled)</li>
          <li><a href=\"/redoc\">/redoc</a> (ReDoc, if enabled)</li>
        </ul>
        <h2>Docs</h2>
        <ul>
          <li><a href=\"https://github.com/abh1hi/ecommerce-retail-rag-mcp\" target=\"_blank\">Repository</a></li>
          <li><a href=\"/\" onclick=\"return false;\">Diagrams are in <code>docs/diagrams/</code> on GitHub</a></li>
        </ul>
      </body>
    </html>
    """

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
