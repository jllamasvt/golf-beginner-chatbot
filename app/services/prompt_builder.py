SYSTEM_PROMPT='''Eres un asistente educativo especializado en golf para principiantes. Responde en español, con claridad. Usa únicamente la evidencia recuperada. No inventes. Para reglas, prioriza USGA. Diferencia reglas oficiales de recomendaciones. No hagas afirmaciones médicas. Si la evidencia no alcanza, dilo.'''
def build_context(documents):
    return '\n\n'.join(f"FUENTE {i}\nID: {p.payload.get('id')}\nFuente: {p.payload.get('source_name')}\nURL: {p.payload.get('source_url')}\nContenido: {p.payload.get('content')}" for i,(_,p) in enumerate(documents,1))
