from fastapi import APIRouter
from app.services.auth_service import generate_did

router = APIRouter()


@router.get("/wallet/did")
async def generate_did_route():
    # Generate Decentralized ID (DID) for ICP user
    did = generate_did()
    return {"status": "DID generated", "did": did}
