# 🧠 Knowledge-Base-Copilot (OC-036)

> **Enterprise-grade RAG pipeline** powered by NVIDIA NIM, NeMo Retriever, Milvus/Pinecone, FastAPI, Okta RBAC, HITL escalation, PII detection, and immutable Audit logging.

---

## 📂 Project Structure

```
kb_copilot/
├── app/
│   ├── config.py                  # Pydantic Settings (all env vars)
│   ├── main.py                    # FastAPI app entrypoint
│   ├── routers/
│   │   └── query.py               # /v1/query endpoint + JWT + Rate Limit
│   └── services/
│       ├── access_control.py      # Okta JWT validation + RBAC namespace resolution
│       ├── retriever.py           # NeMo embeddings + Milvus/Pinecone vector search
│       ├── synthesizer.py         # NVIDIA NIM LLM chat + citation extraction
│       ├── confidence_scorer.py   # Hybrid retrieval + LLM self-evaluation
│       ├── hitl_manager.py        # Human-in-the-loop ticket creation (Postgres)
│       ├── pii_detector.py        # Microsoft Presidio PII quarantine
│       ├── audit_logger.py        # Append-only Postgres audit stream
│       └── rag_pipeline.py        # Master orchestrator
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── .env.example
```

---

## ⚡ RAG Pipeline Flow

```
JWT Auth → Inbound PII Gate → RBAC Retrieve → NIM Synthesize →
Outbound PII Gate → Confidence Score → HITL? → Audit Log
```

---

## 🚀 Quick Start

```bash
git clone https://github.com/Asisyedj/kb_copilot.git
cd kb_copilot
cp .env.example .env
# Fill in your API keys in .env
docker-compose up --build
```

API available at: `http://localhost:8000`

Health check: `GET /health`

Query endpoint: `POST /v1/query`

---

## 🔑 Environment Variables

See `.env.example` for all required variables.

Key variables:
- `NIM_BASE_URL` - NVIDIA NIM endpoint
- `NIM_API_KEY` - NVIDIA API key
- `NEMO_RETRIEVER_URL` - NeMo Retriever endpoint
- `VECTOR_DB_PROVIDER` - `milvus` or `pinecone`
- `OKTA_ISSUER` - Okta OIDC issuer
- `DATABASE_URL` - PostgreSQL connection string

---

## 🛡️ Enterprise Features

| Feature | Implementation |
|---|---|
| Authentication | Okta OIDC JWT (RS256) |
| Authorization | Group → Namespace RBAC |
| LLM | NVIDIA NIM (Llama3-70B) |
| Embeddings | NVIDIA NeMo Retriever |
| Vector DB | Milvus or Pinecone |
| PII Protection | Microsoft Presidio |
| Confidence | Hybrid (Retrieval + LLM self-eval) |
| HITL | Auto-escalation to Postgres tickets |
| Audit | Immutable JSONB audit log |
| Rate Limiting | Redis per-IP + per-user |

---

*Built by Asisyedj | OC-036 | April 2026*
