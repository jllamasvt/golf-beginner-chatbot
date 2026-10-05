import json
from pathlib import Path
from qdrant_client.models import Distance,VectorParams,PointStruct
from app.core.config import settings
from app.core.vector_db import client
from app.services.embedding_service import embed_text,embedding_dimension
KNOWLEDGE_PATH=Path(__file__).resolve().parents[2]/'knowledge/golf_knowledge.json'
def initialize_collection():
    names={c.name for c in client.get_collections().collections}
    if settings.collection_name not in names: client.create_collection(collection_name=settings.collection_name,vectors_config=VectorParams(size=embedding_dimension(),distance=Distance.COSINE))
def index_knowledge():
    initialize_collection(); records=json.loads(KNOWLEDGE_PATH.read_text(encoding='utf-8')); points=[]
    for i,item in enumerate(records,1): points.append(PointStruct(id=i,vector=embed_text(item['content']),payload=item))
    client.upsert(collection_name=settings.collection_name,points=points); return len(points)
