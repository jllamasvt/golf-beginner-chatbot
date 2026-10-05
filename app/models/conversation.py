from pydantic import BaseModel
class ConversationResponse(BaseModel): conversation_id:str; messages:list[dict]
