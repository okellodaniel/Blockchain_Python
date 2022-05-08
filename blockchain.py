import hashlib
from hashlib import sha256
from time import time as t
from block import Block


class Blockchain:
    def __init__(self):
        self.unconfirmed_transactions = []
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block(0, [], t(),"0")
        genesis_block.hash = genesis_block.compute_hash()
        self.chain.append(genesis_block)
    
    @property
    def last_block(self):
        return self.chain[-1]
    
    difficulty = 2

    def proof_of_work(self):
        block.nonce = computed_hash = block.compute_hash()

        while not computed_hash.startswith('0'*Blockchain.difficulty):
        block.nonce += 1
        computed_hash = block.compute_hash
        
        return computed_hash