from openai import OpenAI
from app.core.config import settings
from app.services.prompt_builder import SYSTEM_PROMPT
def generate_response(question,context,history):
    if not settings.openai_api_key: raise RuntimeError('Configura OPENAI_API_KEY.')
    h='\n'.join(f"{m['role']}: {m['content']}" for m in history[-6:])
    prompt=f'EVIDENCIA:\n{context}\n\nHISTORIAL:\n{h}\n\nPREGUNTA:\n{question}'
    return OpenAI(api_key=settings.openai_api_key).responses.create(model=settings.openai_model,instructions=SYSTEM_PROMPT,input=prompt).output_text.strip()
