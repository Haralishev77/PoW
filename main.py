import os
import argparse
import time
import sys
from MerkleTree.MerkleTree import MerkleTree
from SHA256.sha256 import SHA256
from user.block_header.makeheader import block_header_pb2, create_block_header
from user.block.makeblock import create_block, write_block_to_file, read_block_from_file
from user.makerandominput import read_data_from_file, generate_random_226_bits
from termcolor import cprint

def main():
    parser = argparse.ArgumentParser(description='Парсер для пользовательского ввода')
    parser.add_argument('-bs', '--block_size', type=int, help='Размер блока в байтах')
    parser.add_argument('-n', '--nonce', type=int, help='Nonce')
    parser.add_argument('-t', '--timestamp', type=int, help='Метка времени')
    parser.add_argument('-gt', '--generate_transactions', action='store_true', help='Сгенерировать транзакции пользователя')
    parser.add_argument('-pow', '--proof_of_work', action='store_true', help='Будет искать такой nonce, чтобы первые 4 символа хэша равнялись 0')
    parser.add_argument('-sb', '--showblock', action='store_true', help='Показать полученный блок')
    
    args = parser.parse_args()

    block_size = args.block_size if args.block_size else 1024
    nonce = args.nonce if args.nonce else 0
    timestamp = args.timestamp if args.timestamp else int(time.time())

    if args.generate_transactions:
        generate_random_226_bits()
        cprint("Сгенерировано 4 новых транзакции", "yellow")

    data = read_data_from_file()
    previous_block_hash = os.urandom(32)
    merkle_root_hash = MerkleTree(data, SHA256()).get_root()

    if args.proof_of_work:
        for nonce in range(100**100):
            block_header = create_block_header(block_size, previous_block_hash, merkle_root_hash, nonce, timestamp)
            serialized_block_header = block_header.SerializeToString()
            hash = SHA256().hexdigest(serialized_block_header)
            sys.stdout.write(f"\rПробуем nonce - {nonce}")
            sys.stdout.flush()
            if hash[:4] == "0000":
                break
        deserialized_block_header = block_header_pb2.BlockHeader()
        deserialized_block_header.ParseFromString(serialized_block_header)
    else:
        block_header = create_block_header(block_size, previous_block_hash, merkle_root_hash, nonce, timestamp)
        serialized_block_header = block_header.SerializeToString()
        deserialized_block_header = block_header_pb2.BlockHeader()
        deserialized_block_header.ParseFromString(serialized_block_header)

    sys.stdout.write("\r" + " " * 20 + "\r")
    sys.stdout.flush()

    cprint(f"Размер блока: {deserialized_block_header.block_size}", "blue")
    cprint(f"Хэш заголовка прошлого блока: {deserialized_block_header.previous_block_hash.hex()}", "blue")
    cprint(f"Хэш корня Меркла транзакций: {deserialized_block_header.merkle_root_hash.hex()}", "blue")
    cprint(f"Метка времени: {deserialized_block_header.timestamp}", "blue")
    cprint(f"Nonce: {deserialized_block_header.nonce}", "blue")
    cprint(f"Заголовок блока: {serialized_block_header.hex()}", "green")
    cprint(f"Хэш заголовка блока: {SHA256().hexdigest(serialized_block_header)}", "green")

    write_block_to_file(create_block(block_size, previous_block_hash, merkle_root_hash, timestamp, nonce, data))
    
    if args.showblock:
        print("\n")
        print(read_block_from_file())

if __name__ == "__main__":
    main()
