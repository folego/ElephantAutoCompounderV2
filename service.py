import json
import contract

elephant_contract_addr = "0x6839e295a8f13864A2830fA0dCC0F52e71a82DbF" # DO NOT CHANGE IT
wallet_public_addr = "0x98C4Ac9C24C2971e5e2C085cA424a061D0A9020D" # PUT YOUR WALLET ADDRESS HERE

# load private key
wallet_private_key = open('key.txt', "r").readline()

# load abi
f = open('stampede_abi.json')
contract_abi = json.load(f)

# create contract
elephant_contract = contract.connect_to_contract(elephant_contract_addr, contract_abi)

# def get_user_bonds(addr):
#     return elephant_contract.functions.userInfo(addr).call()

def get_user_rewards():
    # print("get_user_rewards", elephant_contract.functions.claimsAvailable(wallet_public_addr).call())
    return elephant_contract.functions.claimsAvailable(wallet_public_addr).call()

def get_user_deposits():
    return elephant_contract.functions.userInfo(wallet_public_addr).call()

def roll():
    txn = elephant_contract.functions.roll().buildTransaction(contract.get_tx_options(wallet_public_addr))
    return contract.send_txn(txn, wallet_private_key)

def withdraw():
    txn = elephant_contract.functions.claim().buildTransaction(contract.get_tx_options(wallet_public_addr))
    return contract.send_txn(txn, wallet_private_key)

