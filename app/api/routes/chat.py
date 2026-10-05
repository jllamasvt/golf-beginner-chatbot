from uuid import uuid4
from fastapi import APIRouter,HTTPException
from app.models.chat import ChatRequest,ChatResponse
from app.services.chat_service import answer_question
from app.services.conversation_service import add_message
router=APIRouter()
@router.post('/chat',response_model=ChatResponse)
def chat(request:ChatRequest):
    cid=request.conversation_id or f'conv_{uuid4().hex[:10]}'; mid=f'msg_{uuid4().hex[:10]}'; add_message(cid,'user',request.message)
    try: result=answer_question(cid,request.message)
    except RuntimeError as e: raise HTTPException(503,str(e))
    except Exception as e: raise HTTPException(500,f'Error procesando la consulta: {e}')
    add_message(cid,'assistant',result['answer']); return ChatResponse(conversation_id=cid,message_id=mid,**result)
