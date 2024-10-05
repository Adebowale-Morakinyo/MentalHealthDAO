from kybra import query, update, void

# Token balance for each user
token_balances: dict = {}

@query
def get_balance(user: str) -> int:
    return token_balances.get(user, 0)

@update
def create_token(user: str, amount: int) -> void:
    global token_balances
    token_balances[user] = token_balances.get(user, 0) + amount
