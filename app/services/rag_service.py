from qdrant_client.models import Filter,FieldCondition,MatchValue
from app.core.config import settings
from app.core.vector_db import client
from app.services.embedding_service import embed_text
def search_knowledge(question,category=None,priority_source=None):
    filt=Filter(must=[FieldCondition(key='category',match=MatchValue(value=category))]) if category and category!='unknown' else None
    result=client.search(collection_name=settings.collection_name,query_vector=embed_text(question),query_filter=filt,limit=settings.top_k,with_payload=True)
    if not result and filt: result=client.search(collection_name=settings.collection_name,query_vector=embed_text(question),limit=settings.top_k,with_payload=True)
    ranked=[]
    for p in result:
        score=float(p.score)+(0.08 if priority_source and p.payload.get('source_name')==priority_source else 0)
        ranked.append((min(score,1.0),p))
    ranked.sort(key=lambda x:x[0],reverse=True); return ranked[:settings.top_k]
