from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.routers import query
import logging

logging.basicConfig(level="INFO")
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Knowledge-Base-Copilot starting up...")
    yield
    # Graceful shutdown: close pipeline connections
    if hasattr(app.state, "rag_pipeline"):
        await app.state.rag_pipeline.shutdown()
        logger.info("RAG pipeline shut down cleanly.")


app = FastAPI(
    title="Knowledge-Base-Copilot",
    description="Enterprise RAG pipeline: NVIDIA NIM + NeMo + Milvus/Pinecone + RBAC + HITL + PII",
    version="1.0.0",
    lifespan=lifespan,
)

app.include_router(query.router)


@app.get("/health", tags=["System"])
async def health_check():
    return {"status": "healthy", "service": "Knowledge-Base-Copilot"}
