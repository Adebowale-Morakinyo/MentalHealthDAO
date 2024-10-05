from fastapi import APIRouter

router = APIRouter()


@router.post("/therapy/book")
async def book_therapy_session(therapist_id: str, session_type: str):
    # Logic for booking therapy session (dummy example)
    return {"status": "booked", "therapist_id": therapist_id, "session_type": session_type}
