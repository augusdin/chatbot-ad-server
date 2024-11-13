# app/api/v1/endpoints/check_ad.py

from fastapi import APIRouter, HTTPException
from typing import List, Optional
from pydantic import BaseModel

from app.services.check_ad import check_advertisement

router = APIRouter()

class Message(BaseModel):
    created_at: str
    role: str
    content: str

class MessagesRequest(BaseModel):
    messages: List[Message]

class AdResponse(BaseModel):
    show_ad: bool
    advertiser_name: Optional[str] = None
    ad_use_case: Optional[str] = None
    display_format: Optional[str] = None
    advertiser_link: Optional[str] = None

@router.post("/check-ad", response_model=AdResponse)
async def check_ad_endpoint(request: MessagesRequest):
    messages = request.messages
    if not messages:
        raise HTTPException(status_code=400, detail="Message content cannot be empty.")

    messages_dict = [message.dict() for message in messages]
    result = check_advertisement(messages_dict)
    return result