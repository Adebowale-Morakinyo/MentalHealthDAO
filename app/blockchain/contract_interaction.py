from web3 import Web3

# Interact with a deployed smart contract (ERC-20 or custom on ICP)
w3 = Web3(Web3.HTTPProvider("https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"))

contract_address = "0xYourContractAddress"
abi = [...]  # Contract ABI

contract = w3.eth.contract(address=contract_address, abi=abi)


def get_balance(address):
    return contract.functions.balanceOf(address).call()


def transfer_tokens(to_address, amount):
    tx_hash = contract.functions.transfer(to_address, amount).transact({"from": "0xYourAddress"})
    return tx_hash
