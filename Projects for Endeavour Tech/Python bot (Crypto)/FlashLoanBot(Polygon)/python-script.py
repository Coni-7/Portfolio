from pickle import FALSE
from web3 import Web3
from web3.middleware import geth_poa_middleware
# Connect to Polygon network
w3 = Web3(Web3.HTTPProvider('https://polygon-rpc.com'))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)

# Ensure connected
if not w3.is_connected():
    print("Not connected to blockchain")
    exit()

# Set up your wallet
my_account = '0x0f797C19527c4D8322A73e7c5075462390471ED2'
w3.eth.default_account = my_account

# FlashLoan contract ABI (replace with actual ABI)
contract_abi = 

# Address of deployed FlashLoan contract (replace with actual address)
contract_address = '0x398eC7346DcD622eDc5ae82352F02bE94C62d119'

flashloan_contract = w3.eth.contract(address=contract_address, abi=contract_abi)

# Initiate a flash loan (example, replace with actual token and amount)
token_address = '0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174'
loan_amount = 1000 * 10**18  # Example amount, adjust based on token decimals

tx_hash = flashloan_contract.functions.flashLoan(token_address, loan_amount).transact()
receipt = w3.eth.waitForTransactionReceipt(tx_hash)
print(receipt)