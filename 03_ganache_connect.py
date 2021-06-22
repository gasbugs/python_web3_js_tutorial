from web3 import Web3

ganache_url = 'http://175.198.224.248:7545'

web3 = Web3(Web3.HTTPProvider(ganache_url))

account_1= '0xe9901Fc4C5fFe7e7b0B0475d31f0Ee0518d15760'
account_2= '0xEb172C9A147d1DA3d7cbfc1C485eb4b17C27E0eF'

private_key = '221faf00af44b34a5a61d03646683950b7e3014b4799e316c28f706d35f297bb'

# get the nonce
nonce = web3.eth.getTransactionCount(account_1)

# build a transaction
tx = {
    'nonce': nonce,
    'to': account_2,
    'value': web3.toWei(1, 'ether'),
    'gas': 2000000,
    'gasPrice': web3.toWei('50', 'gwei')
}

# sign transaction
signed_tx = web3.eth.account.signTransaction(tx, private_key)

# send transaction
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
print(tx_hash)
