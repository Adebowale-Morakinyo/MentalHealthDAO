import requests


# Function to interact with an ICP canister via HTTP
def call_icp_canister(canister_id: str, method_name: str, payload: dict):
    # Canister public API endpoint
    canister_url = f"https://{canister_id}.ic0.app"

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
