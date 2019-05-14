import hashlib
import time


class Block:
    def __init__(self, index: int, data: str, prevHash: str) -> None:
        self.index = index
        self.data = data
        self.timestamp = int(round(time.time() * 1000))
        self.prevHash = prevHash
        self.blockHash = self.generateHash(index, data, prevHash)

    def checkBlockValidity(self, prevBlock, currBlock) -> bool:
        if (prevBlock.blockHash != currBlock.prevHash):
            return False
        if (currBlock.index != prevBlock.index + 1):
            return False
        if (currBlock.blockHash != self.generateHash(currBlock.index,
                                                     currBlock.data,
                                                     currBlock.prevHash)):
            return False
        return True

    def generateBlock(self, prevBlock, data: str):
        newBlock = Block(prevBlock.index + 1, data, prevBlock.blockHash)
        return newBlock

    def generateHash(self, index, data, prevHash) -> str:
        message = str(index) + data + prevHash
        blockHash = hashlib.sha256(message.encode('utf8')).hexdigest()
        return blockHash
