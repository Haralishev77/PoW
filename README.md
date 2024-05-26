# PoW - Blockchain Consensus Algorithm

## Overview

This repository contains an implementation of the Proof of Work (PoW) consensus algorithm used in blockchain technology. The program simulates the mining process where a valid nonce is found such that the resulting hash meets specific criteria. The code is written in Python and incorporates Merkle trees for transaction integrity and the SHA-256 hashing algorithm for security.

## Features

- **Block Creation:** Generate a new block with a specified size, nonce, and timestamp.
- **Proof of Work:** Perform the mining process to find a nonce such that the hash of the block header starts with four zero bytes.
- **Merkle Tree:** Ensure the integrity of transactions using a Merkle tree structure.
- **Transaction Generation:** Create random transactions to be included in the block.
- **Block Serialization:** Serialize and deserialize block headers for storage and transmission.
- **File Operations:** Read and write blocks to and from files.
- **Command Line Interface:** Provide a CLI for users to interact with the program and specify parameters.

## Usage

To run the program, use the following command with the appropriate options:

```sh
python main.py [options]
```

### Command Line Options

- `-bs`, `--block_size`: Size of the block in bytes.
- `-n`, `--nonce`: Nonce value for the block.
- `-t`, `--timestamp`: Timestamp for the block.
- `-gt`, `--generate_transactions`: Generate random user transactions.
- `-pow`, `--proof_of_work`: Perform the proof of work to find a nonce such that the first 4 bytes of the hash are 0.
- `-sb`, `--showblock`: Display the generated block.

### Example Commands

Сreate a block with proof of work:

```sh
python main.py -bs 1024 -pow
```

Generate transactions and create a block:

```sh
python main.py -bs 1024 -gt
```

Show the created block:

```sh
python main.py -bs 1024 -sb
```
