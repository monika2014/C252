from web3 import Web3
 

ganache_url = 'http://127.0.0.1:7545'

web3_ganache_connection = Web3(Web3.HTTPProvider(ganache_url))

Alice_account = '0xce1bF1Caa01Ac6707D313a44DdBd98E870e46d9F'
James_account = '0x1037C926a62E4b71ee72C9feBb7723A52aF45Ff5'

nonce = web3_ganache_connection.eth.get_transaction_count(Alice_account)

transaction_data = {
    'nonce':nonce,
    'to':James_account,
    'value':web3_ganache_connection.to_wei(1, 'ether'),
    'gas':21000,
    'gasPrice':web3_ganache_connection.to_wei(50,'gwei')
}

private_key = '0x276da95ce68c13685d52a484df623cd5c471728bf5a56dbf34d7adfe4866af1a'

singed_transaction = web3_ganache_connection.eth.account.sign_transaction(transaction_data,private_key)
transaction_hash = web3_ganache_connection.eth.send_raw_transaction(singed_transaction.rawTransaction)

print(web3_ganache_connection.to_hex(transaction_hash))


 