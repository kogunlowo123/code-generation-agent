# Code Generation Agent

[![CI](https://github.com/kogunlowo123/code-generation-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/kogunlowo123/code-generation-agent/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Category**: Software Engineering | **Cloud**: MULTI-CLOUD | **LLM**: gpt-4o

Specification-driven code generator that produces complete modules, APIs, database schemas, and full-stack features from product requirements, user stories, or technical specifications with proper architecture layering.

---

## Domain-Specific Tools

| Tool | Description |
|------|-------------|
| `generate_from_spec` | Generate full module from a technical specification |
| `generate_api_endpoint` | Generate a complete API endpoint with validation, service, and tests |
| `generate_database_schema` | Generate database migration and ORM models from entity description |
| `generate_crud` | Generate full CRUD operations for an entity |
| `generate_frontend_component` | Generate UI component with state management |

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/v1/generate/module` | Generate a full module from spec |
| `POST` | `/api/v1/generate/api` | Generate API endpoint |
| `POST` | `/api/v1/generate/schema` | Generate database schema |
| `POST` | `/api/v1/generate/crud` | Generate CRUD operations |
| `POST` | `/api/v1/generate/component` | Generate frontend component |

## Features

- Spec To Code
- Schema Generation
- Api Scaffolding
- Fullstack Features
- Migration Generation

## Integrations

- Github Connector
- Gitlab Connector
- Ast Parser
- Package Registry

## Architecture

```
code-generation-agent/
├── src/
│   ├── agent/              # Domain-specific agent logic
│   │   ├── code_generation_agent_agent.py  # Main agent with domain tools
│   │   ├── tools.py        # 5 domain-specific tools
│   │   └── prompts.py      # Expert system prompts
│   ├── api/                # FastAPI routes
│   │   └── routes/
│   │       ├── domain.py   # 5 domain-specific endpoints
│   │       └── health.py   # Health check
│   ├── connectors/         # 4 integration connectors
│   ├── config/             # Settings and configuration
│   ├── models/             # Domain-specific Pydantic schemas
│   ├── rag/                # RAG pipeline
│   ├── mcp/                # MCP server
│   └── a2a/                # Agent-to-agent protocol
├── tests/
├── infrastructure/         # Terraform, K8s, Helm, Docker
├── dashboard/              # Next.js frontend
└── docs/                   # Architecture and deployment docs
```

## Quick Start

```bash
# Install
pip install -e ".[dev]"

# Run
make dev

# Test
make test

# Docker
docker compose up -d
```

## Primary Service

**LLM + AST Tooling**

---

Built as part of the Enterprise AI Agent Platform.
