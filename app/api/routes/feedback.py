from fastapi import APIRouter
from app.models.feedback import FeedbackRequest
router=APIRouter(); _feedback=[]
@router.post('/feedback')
def feedback(request:FeedbackRequest): _feedback.append(request.model_dump()); return {'status':'received'}
