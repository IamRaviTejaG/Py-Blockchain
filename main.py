import json
import sys
import time

from blocks.block import Block

blockChain = []

genesisBlock = Block(0, f'Genesis block created at height 0.', f'')
sys.stdout.write(f'New block created at height: {genesisBlock.index}!\n')


blockChain.append(genesisBlock)
n = 100

oldBlock = genesisBlock

while(n):
    data = f'New block created at block height: {oldBlock.index+1}'
    newBlock = oldBlock.generateBlock(oldBlock, data)
    sys.stdout.write(f'Block at height {newBlock.index} is valid:
                     {newBlock.checkBlockValidity(oldBlock, newBlock)}')
    blockChain.append(newBlock)
    oldBlock = newBlock
    n -= 1

jsonDumps = []

for block in blockChain:
    newObject = dict()
    newObject['index'] = block.index
    newObject['data'] = block.data
    newObject['timestamp'] = block.timestamp
    newObject['prevHash'] = block.prevHash
    newObject['blockHash'] = block.blockHash
    jsonDumps.append(newObject)

a = json.dumps(jsonDumps)
with open('blockchain.json', 'w+') as f:
    f.write(a)
