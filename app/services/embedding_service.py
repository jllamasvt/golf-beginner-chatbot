from openai import OpenAI
from app.core.config import settings
def embed_text(text):
    if not settings.openai_api_key: raise RuntimeError('Falta OPENAI_API_KEY.')
    return OpenAI(api_key=settings.openai_api_key).embeddings.create(model=settings.embedding_model,input=text).data[0].embedding
def embedding_dimension():
    if settings.embedding_model=='text-embedding-3-small': return 1536
    if settings.embedding_model=='text-embedding-3-large': return 3072
    raise RuntimeError('Configura la dimensión del modelo de embeddings.')
