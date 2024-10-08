import requests

# Canister ID (replace this with the actual canister ID)
CANISTER_ID = "bkyz2-fmaaa-aaaaa-qaaaq-cai"
ID = "bkyz2-fmaaa-aaaaa-qaaaq-cai"


# Function to interact with an ICP canister via HTTP
def call_icp_canister(method_name: str, payload: dict):
    canister_url = f"http://127.0.0.1:4943/?canisterId={CANISTER_ID}"

    try:
        response = requests.post(canister_url, json={
            "method": method_name,
            "args": payload
        })
        response.raise_for_status()  # Ensure the request was successful
        return response.json()
    except requests.RequestException as e:
        print(f"Error calling canister: {e}")
        return {"error": str(e)}


# Function to get user balance
def get_user_balance(user: str):
    return call_icp_canister("get_balance", {"user": user})


# Function to create tokens for a user
def create_user_tokens(user: str, amount: int):
    return call_icp_canister("create_token", {"user": user, "amount": amount})
