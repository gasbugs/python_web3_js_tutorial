import json
from web3 import Web3

ganache_url = 'http://59.17.82.162:7545'
web3 = Web3(Web3.HTTPProvider(ganache_url))

web3.eth.defaultAccount = web3.eth.accounts[0]

abi = '[{"constant":false,"inputs":[{"name":"_greeting","type":"string"}],"name":"setGreeting","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"greet","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"greeting","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"}]'
abi = json.loads(abi)
address = web3.toChecksumAddress('0xB81164E44BBA8b78172F1463772f66819afb0bc2')

contract = web3.eth.contract(address=address, abi=abi)
print(contract.functions.greet().call())

tx_hash = contract.functions.setGreeting('123asdzxcasd!!!').transact()
print(tx_hash)

web3.eth.waitForTransactionReceipt(tx_hash)

print('Updated greeting: {}'.format(
    contract.functions.greet().call()
))


