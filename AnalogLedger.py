import paypalcheckoutsdk
from paypalcheckoutsdk.orders import OrdersCreateRequest
import requests
import json
import os
def get_access_token():
    PAYPAL_CLIENT_ID = os.environ.get('PAYPAL_CLIENT_ID')
    client_id=os.environ.get('PAYPAL_CLIENT_ID')
    client_secret=os.environ.get('PAYPAL_SECRET')
    response=requests.post('https://api.paypal.com/v1/oauth2/token', auth=(client_id, client_secret), data={'grant_type': 'client_credentials'})
    return response.json['access_token']
PAYPAL_SECRET = os.environ.get('PAYPAL_SECRET')
DEV_ADDRESS = os.environ.get('DEV_ADDRESS')
import time
import hashlib
import ecdsa 
def generate_wallet():
    key = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
    return key.get_verifying_key().to_string().hex()
DEV_ADDRESS = "c86f36fab33f1f19c30f6cfc5741292c78f6be0dae26028a358a2e34928f89019c42292acaf715026d238d3c143198a332471ac3a910cc98b8423be5d29f0b31"
REVENUE_SHARE = 0.05
class AnalogLedger:
    def __init__(self):
        self.transactions = []
        self.chain = []
        self.create_block(proof=1, previous_hash='0')                         
    def create_block(self, proof, previous_hash): 
        self.chain.append(Block(index=len(self.chain), timestamp=time.time(), transactions=self.transactions, nonce=proof, previous_hash=previous_hash))
    def add_transactions(self, sender, recipient, amount):
        self.transactions.append({'sender':sender, 'recipient':recipient, 'amount':amount})
        self.transactions.append({'sender':sender, 'recipient': DEV_ADDRESS, 'amount': amount * REVENUE_SHARE})
    def get_chain(self):
        return self.chain
    def hash(self, block):
        encoded_block = json.dumps({'index': block.index, 'timestamp': block.timestamp, 'transactions': block.transactions, 'nonce': block.nonce, 'previous_hash': block.previous_hash}, sort_keys=True)
class Block:
    def __init__(self, index, timestamp, transactions, nonce, previous_hash):
        self.index = index
        self.timestamp = timestamp 
        self.transactions = transactions
        self.nonce = nonce 
        self.previous_hash = previous_hash
ledger = AnalogLedger()
ledger.add_transactions("Alice", "Bob", 50)
print(ledger.create_block(proof=100, previous_hash='1'))
print(ledger.get_chain())
ledger.add_transaction:("Bob", "Charlie", 30)
print (ledger.create_block),({'proof'==200,'previous_hash'=='2'})
print ( ledger.create_block)
print("My Address", DEV_ADDRESS)
def proof_of_work(self, last_proof):
    proof = 0
    while self.hash(proof)[:4]!= "0000":
        proof += 1
    return proof 
def create_paypal_order(amount, sender, recipient):
    request = OrdersCreateRequest() 
    request.prefer('return=representation')
    request.body = ("intent", "CAPTURE")
    amount = float(input("Enter amount:"))
    fee = amount*0.05
    ledger.add_transactions(sender, recipient, amount)
    print(f"Transaction of {amount} AnalogCoin from {sender} to {recipient} completed.")
    print("Complete Payment here:https://www.paypal.com/ncp/payment/8P22DGTGSPCZN") 
    proof = ledger.create_block(0,0)
    ledger.create_block(0,0)
    return ledger.chain
sender = 'Alice'
recipient = 'Bob'
def simulate_payment():
    amount = float(input("Enter amount:"))
    create_paypal_order(amount, sender, recipient)
    free = amount * 0.05
    ledger.add_transactions(sender, recipient, amount)
    print(f"Transaction of {amount} AnalogCoin completed")
    proof = ledger.create_block(1, ledger.hash(ledger.chain[-1])) if ledger.chain else '0'
    return ledger.chain