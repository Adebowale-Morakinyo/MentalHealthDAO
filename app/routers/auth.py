from fastapi import APIRouter
from app.services.auth_service import generate_did, create_session, get_session
from app.icp.canister_interaction import get_user_balance, create_user_tokens

router = APIRouter()


@router.get("/wallet/did")
async def generate_did_route():
    # Call the service to generate a DID
    did = generate_did()
    return {"status": "DID generated", "did": did}


@router.post("/session/create")
async def create_session_route(user_did: str, session_data: str):
    # Create a new session for the user
    create_session(user_did, session_data)
    return {"status": "session created"}


@router.get("/session/{user_did}")
async def get_session_route(user_did: str):
    # Retrieve the session data for the given DID
    session_data = get_session(user_did)
    return {"session_data": session_data}


@router.get("/balance/{user_did}")
async def get_user_balance_route(user_did: str):
    # Retrieve the user's token balance from the ICP canister
    balance = get_user_balance(user_did)
    return {"balance": balance}
