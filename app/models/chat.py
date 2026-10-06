from pydantic import BaseModel,Field
class ChatRequest(BaseModel): conversation_id:str|None=None; message:str=Field(min_length=1,max_length=4000); language:str='es'
class Source(BaseModel): id:str; name:str; url:str; relevance:float
class ChatResponse(BaseModel): conversation_id:str; message_id:str; answer:str; category:str; subcategory:str; confidence:float; sources:list[Source]
