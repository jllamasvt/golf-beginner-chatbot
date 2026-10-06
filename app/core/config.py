from pydantic_settings import BaseSettings, SettingsConfigDict
class Settings(BaseSettings):
    app_name: str='Golf Beginner Chatbot'; app_version: str='1.0.0'; api_prefix: str='/api/v1'
    qdrant_mode: str='local'; qdrant_path: str='./data/qdrant'; qdrant_url: str|None=None; qdrant_api_key: str|None=None
    collection_name: str='golf_knowledge'; openai_api_key: str|None=None; openai_model: str='gpt-5-mini'
    embedding_model: str='text-embedding-3-small'; top_k: int=5
    model_config=SettingsConfigDict(env_file='.env', extra='ignore')
settings=Settings()
