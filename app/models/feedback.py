from pydantic import BaseModel,Field
class FeedbackRequest(BaseModel): conversation_id:str; message_id:str; rating:int=Field(ge=1,le=5); comment:str|None=None
