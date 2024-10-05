import uuid


# Function to generate a simple Decentralized ID (DID)
def generate_did():
    # Using UUID to generate a basic DID for demo purposes
    did = f"did:ic:{uuid.uuid4()}"
    return did


# In-memory session storage (for MVP purposes)
user_sessions = {}


def create_session(user_did: str, session_data: str):
    # Store session data linked to the DID
    user_sessions[user_did] = session_data
    return True


def get_session(user_did: str):
    # Retrieve session data
    return user_sessions.get(user_did, "No active session")
