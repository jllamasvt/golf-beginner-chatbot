from fastapi import APIRouter
from app.models.source import SourceInfo
router=APIRouter()
SOURCES=[SourceInfo(id='G006',name='Golf Digest',url='https://www.golfdigest.com/story/beginners-guide-to-golf'),SourceInfo(id='G016',name='GOLF.com',url='https://golf.com/instruction/how-to-swing-a-golf-club-in-five-simple-steps/'),SourceInfo(id='G028',name='USGA',url='https://www.usga.org/rules-hub.html'),SourceInfo(id='G043',name='USGA',url='https://www.usga.org/rules-hub.html')]
@router.get('/sources',response_model=list[SourceInfo])
def list_sources(): return SOURCES
