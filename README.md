# ⛳ Golf Beginner Chatbot

Proyecto académico: chatbot educativo RAG para principiantes de golf.

## Arquitectura
Frontend HTML/CSS/JS · FastAPI · Qdrant · embeddings y LLM configurables.

## Estado del conocimiento
Incluye cuatro registros semilla (G006, G016, G028 y G043) para demostrar el pipeline RAG. Los 54 registros del Documento Maestro deben verificarse contra sus fuentes originales antes de presentarlos como base definitiva.

## Local
`pip install -r requirements.txt`\nCopiar `.env.example` a `.env`, configurar `OPENAI_API_KEY`, ejecutar `python scripts/ingest_knowledge.py` y luego `uvicorn app.main:app --reload`.

Abrir `http://127.0.0.1:8000` y `http://127.0.0.1:8000/docs`.

## Producción
Conectar este repositorio a Render y usar Qdrant Cloud. Configurar las variables de entorno y ejecutar la ingesta antes de probar el chat.

**Nunca subir `.env` ni claves API a GitHub.**
