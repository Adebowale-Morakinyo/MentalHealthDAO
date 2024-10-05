import requests


def call_icp_canister(canister_id: str, method_name: str, payload: dict):
    # Define the URL for the canister API
    canister_url = f"https://{canister_id}.ic0.app"
    response = requests.post(canister_url, json={
        "method": method_name,
        "args": payload
    })
    return response.json()


def create_token_incentive(user: str, amount: int):
    canister_id = "abcdefg-12345"  # Replace with actual canister ID
    method_name = "create_token"
    payload = {"user": user, "amount": amount}
    return call_icp_canister(canister_id, method_name, payload)
