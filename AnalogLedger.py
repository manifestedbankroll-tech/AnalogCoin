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
        self.create_block(proof = 100, previous_hash = 1) 
    def add_transaction(self, sender, recipient, amount):
        self.transactions.append({'sender':sender, 'recipient':recipient, 'amount':amount})
        self.transactions.append({'sender': sender, 'recipient': DEV_ADDRESS, 'amount': amount * REVENUE_SHARE})
    def get_chain(self):
        return self.chain
    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys = True)
    def create_block(self, proof, previous_hash):
        block = {
        "index":1,
        "proof":proof,
        "previous_hash":previous_hash,
        "timestamp": time.time(),
        "transactions": self.transactions} 
        self.chain.append(block) 
        return block
ledger = AnalogLedger()
ledger.add_transaction("Alice", "Bob", 50)
print(ledger.create_block(proof=100, previous_hash='1'))
print(ledger.get_chain())
ledger.add_transaction("Bob", "Charlie", 30)
print(ledger.create_block(proof=200, previous_hash='2'))
print("My Address", DEV_ADDRESS)
def proof_of_work(self, last_proof):
    proof = 0
    while self.hash(proof)[:4]!= "0000":
        proof += 1
    return proof 


     