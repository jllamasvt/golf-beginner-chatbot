from pathlib import Path
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from app.core.config import settings
from app.api.routes import chat,health,conversations,sources,feedback
app=FastAPI(title=settings.app_name,version=settings.app_version,description='Chatbot RAG educativo para golfistas principiantes.')
app.add_middleware(CORSMiddleware,allow_origins=['*'],allow_credentials=False,allow_methods=['*'],allow_headers=['*'])
p=settings.api_prefix
for r in [chat.router,health.router,conversations.router,sources.router,feedback.router]: app.include_router(r,prefix=p)
frontend=Path(__file__).resolve().parents[1]/'frontend'
if frontend.exists(): app.mount('/',StaticFiles(directory=str(frontend),html=True),name='frontend')
