from app.services.classifier import classify
from app.services.rag_service import search_knowledge
from app.services.prompt_builder import build_context
from app.services.llm_service import generate_response
from app.services.conversation_service import get_history
def answer_question(cid,question):
    c=classify(question); docs=search_knowledge(question,c['category'],c['priority_source'])
    if not docs: return {'answer':'No tengo información suficiente en la base de conocimiento para responder esa pregunta.','category':c['category'],'subcategory':c['subcategory'],'confidence':0.0,'sources':[]}
    ans=generate_response(question,build_context(docs),get_history(cid)); sources=[]
    for score,p in docs:
        x=p.payload; sources.append({'id':x['id'],'name':x['source_name'],'url':x['source_url'],'relevance':round(float(score),3)})
    return {'answer':ans,'category':c['category'],'subcategory':c['subcategory'],'confidence':round(sum(s for s,_ in docs)/len(docs),3),'sources':sources}
