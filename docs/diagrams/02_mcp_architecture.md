# MCP Architecture Diagram: Retail RAG System Tool Integration

![MCP Architecture](../charts/mcp_architecture.png)

## Description
Shows the full MCP protocol stack:
- Host/client layer (API gateway, request auth)
- Protocol message flow (init, tool call, response, error)
- MCP server registry, session/context store
- Per-tool servers (product_search, inventory_check, policy_qa, analytics_query)
- Security boundaries (auth, RBAC)
- Data sources and system integrations
- Logging and error handling
- Arrows illustrate flow of consent, data, requests between layers.