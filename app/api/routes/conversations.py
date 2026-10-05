from fastapi import APIRouter
from app.models.conversation import ConversationResponse
from app.services.conversation_service import get_history,delete_conversation
router=APIRouter()
@router.get('/conversations/{conversation_id}',response_model=ConversationResponse)
def get_conversation(conversation_id): return ConversationResponse(conversation_id=conversation_id,messages=get_history(conversation_id))
@router.delete('/conversations/{conversation_id}')
def remove_conversation(conversation_id): delete_conversation(conversation_id); return {'status':'deleted'}
