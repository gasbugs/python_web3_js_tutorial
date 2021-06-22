from web3 import Web3

ganache_url = "http://59.17.82.162:7545"
print("try connect to ", ganache_url)
web3 = Web3(Web3.HTTPProvider(ganache_url))
print(web3.isConnected())
print(web3.eth.blockNumber)

balance = web3.eth.getBalance('0x84a49798c6B2375F6B2e44D31a0715E740fB6A7c')
print(balance)
print(web3.fromWei(balance, 'ether'))