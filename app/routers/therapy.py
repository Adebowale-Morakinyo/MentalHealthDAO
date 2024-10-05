from fastapi import APIRouter
from app.services.therapy_service import book_therapy_session

router = APIRouter()


@router.post("/therapy/book")
async def book_therapy_route(user_did: str, therapist_id: str, session_type: str):
    # Book a therapy session
    result = book_therapy_session(user_did, therapist_id, session_type)
    return result
