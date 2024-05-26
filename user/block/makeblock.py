from user.block import block_pb2

def create_block(block_size, previous_block_hash, merkle_root_hash, timestamp, nonce, transactions):
    block = block_pb2.Block()
    block.BlockHeader.block_size = block_size
    block.BlockHeader.previous_block_hash = previous_block_hash
    block.BlockHeader.merkle_root_hash = merkle_root_hash
    block.BlockHeader.timestamp = timestamp
    block.BlockHeader.nonce = nonce

    for transaction in transactions:
        block.Transactions.user_transaction.append(transaction)

    return block

def write_block_to_file(block):
    with open('user/output.proto', 'wb') as f:
        f.write(block.SerializeToString())

def read_block_from_file():
    block = block_pb2.Block()
    with open('user/output.proto', 'rb') as f:
        block.ParseFromString(f.read())
    return block