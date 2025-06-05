import hashlib
import time

# class to make single block 
class Block:
    def __init__(self, index, timestamp, data, prev_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.prev_hash = prev_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_data = str(self.index) + self.timestamp + self.data + self.prev_hash
        return hashlib.sha256(block_data.encode()).hexdigest()

# class for complete blockchain
class MyBlockchain:
    def __init__(self):
        self.chain = []
        self.make_first_block()  # Genesis block

    def make_first_block(self):
        first = Block(0, str(time.time()), "Genesis Block", "0")
        self.chain.append(first)

    def get_last_block(self):
        return self.chain[-1]

    def add_new_block(self, data):
        last_block = self.get_last_block()
        new_block = Block(
            index=last_block.index + 1,
            timestamp=str(time.time()),
            data=data,
            prev_hash=last_block.hash
        )
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            curr = self.chain[i]
            prev = self.chain[i - 1]

            if curr.hash != curr.calculate_hash():
                print("⚠️ Block", i, "has been tampered!")
                return False
            if curr.prev_hash != prev.hash:
                print("⚠️ Block", i, "is not linked properly!")
                return False
        return True

# Testing the blockchain
if __name__ == "__main__":
    my_chain = MyBlockchain()

    # Add blocks
    my_chain.add_new_block("This is my first block after genesis")
    my_chain.add_new_block("Adding another block with some data")

    # Print blockchain
    for block in my_chain.chain:
        print("Block #", block.index)
        print("Time:", block.timestamp)
        print("Data:", block.data)
        print("Prev Hash:", block.prev_hash)
        print("Hash:", block.hash)
        print("-" * 50)

    # Check if everything is good
    if my_chain.is_chain_valid():
        print("✅ The blockchain is valid!")
    else:
        print("❌ The blockchain has some issues.")
