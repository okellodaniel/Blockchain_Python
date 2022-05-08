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
  