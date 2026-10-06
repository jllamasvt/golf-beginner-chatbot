from qdrant_client import QdrantClient
from app.core.config import settings
def create_qdrant_client():
    if settings.qdrant_mode.lower()=='cloud':
        if not settings.qdrant_url or not settings.qdrant_api_key: raise RuntimeError('Faltan QDRANT_URL/QDRANT_API_KEY.')
        return QdrantClient(url=settings.qdrant_url, api_key=settings.qdrant_api_key)
    return QdrantClient(path=settings.qdrant_path)
client=create_qdrant_client()
