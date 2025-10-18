# Deployment Architecture: Local to Production Environments

![Deployment Architecture](../charts/deployment_architecture.png)

## Description
Describes local, staging, and production environments. Shows how Ollama, ChromaDB, and MCP server are orchestrated (Docker Compose, K8s). Monitoring (Prometheus, Grafana, log shipper) and security (auth, encryption, RBAC) layers are illustrated. CI/CD paths, backup, scaling, and disaster recovery flows are noted.