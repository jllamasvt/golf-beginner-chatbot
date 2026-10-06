from app.core.config import settings
from app.core.vector_db import client
from app.services.embedding_service import embed_text


def search_knowledge(question: str, category=None, priority_source=None):
    query_vector = embed_text(question)

    result = client.query_points(
        collection_name=settings.collection_name,
        query=query_vector,
        using="default",
        limit=settings.top_k,
        with_payload=True,
    )

    return [(point.score, point) for point in result.points]


def retrieve_context(question: str):
    return search_knowledge(question)
