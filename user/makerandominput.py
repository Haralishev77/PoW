import os
import user.transactions.transactions_pb2 as transactions_pb2

def generate_random_226_bits():
    user_data = transactions_pb2.Transactions()
    for _ in range(4):
        user_data.user_transaction.append(os.urandom(226))

    serialized_data = user_data.SerializeToString()

    with open('user/input.proto', 'wb') as f:
        f.write(serialized_data)


def read_data_from_file():
    with open('user/input.proto', 'rb') as f:
        serialized_data = f.read()

    user_data = transactions_pb2.Transactions()
    user_data.ParseFromString(serialized_data)
    data_array = list(user_data.user_transaction)

    return data_array

if __name__ == "__main__":
    generate_random_226_bits()