from web3 import Web3

# Connect to Polygon Network using the provided RPC URL
w3 = Web3(Web3.HTTPProvider('https://polygon-rpc.com'))

# Ensure connection to Polygon Network
if not w3.is_connected():
    print("Failed to connect to Polygon Network")
    exit()

# Your MetaMask wallet address
wallet_address = '0x0f797C19527c4D8322A73e7c5075462390471ED2'

# Get MATIC (Polygon's native token) balance
balance_wei = w3.eth.get_balance(wallet_address)
balance_matic = w3.from_wei(balance_wei, 'ether')

print(f"Balance for {wallet_address}: {balance_matic} MATIC")

# NOTE: If you have other tokens in your wallet and you want to check their balances, you'd need the ABI of the token's contract and then interact with the contract directly.