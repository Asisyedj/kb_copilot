from enum import Enum


class Intent(str, Enum):
    QUESTION = "question"
    TASK = "task"
    LOOKUP = "lookup"


class PIIAction(str, Enum):
    QUARANTINE = "quarantine"
    REDACT = "redact"
    ALLOW = "allow"


class IngestionStatus(str, Enum):
    PENDING_APPROVAL = "pending_approval"
    APPROVED = "approved"
    REJECTED = "rejected"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"


class VectorDBProvider(str, Enum):
    MILVUS = "milvus"
    PINECONE = "pinecone"
