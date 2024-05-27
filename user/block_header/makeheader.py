import user.block_header.block_header_pb2 as block_header_pb2


# Функция создания заголовка блока
def create_block_header(block_size, previous_block_hash, merkle_root_hash, nonce, timestamp):
    block_header = block_header_pb2.BlockHeader()
    block_header.block_size = block_size
    block_header.previous_block_hash = previous_block_hash
    block_header.merkle_root_hash = merkle_root_hash
    block_header.timestamp = timestamp
    block_header.nonce = nonce
    return block_header
