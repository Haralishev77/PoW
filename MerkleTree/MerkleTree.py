from math import log2, ceil


class MerkleTree:
    def __init__(self, data_list, hash_function):
        self.hash_function = hash_function
        self.leaves = []

        # Заполняем листья
        for data in data_list:
            self.leaves.append(self.hash_function.digest(data))

        # Дополняем пустыми элементами до 2^n
        while len(self.leaves) != 2 ** ceil(log2(len(data_list))):
            self.leaves.append(None)

        # Строим дерево
        self.tree = self._build_tree(self.leaves)

    # Функция построения дерева
    def _build_tree(self, leaves):
        tree = [leaves]
        while len(tree[-1]) > 1:
            current_level = tree[-1]
            next_level = []
            for i in range(0, len(current_level), 2):
                # Записываем хэш детей, если они есть
                if current_level[i] and current_level[i + 1]:
                    combined_hash = self.hash_function.digest(current_level[i] + current_level[i + 1])
                # Записываем в узел None, если дети None 
                elif current_level[i] == None and current_level[i + 1] == None:
                    combined_hash = None
                # Записываем в узел ребенка, если второй None
                else:
                    combined_hash = current_level[i]
                next_level.append(combined_hash)
            tree.append(next_level)
        return tree

    # Функция возврата корня дерева
    def get_root(self):
        return self.tree[-1][0] if self.tree else None

    # Функция возврата массива из элементов с которыми был сделан хэш
    def get_proof(self, index):
        proof = []
        for level in range(len(self.tree) - 1):
            level_nodes = self.tree[level]
            is_right_node = index % 2
            sibling_index = index - 1 if is_right_node else index + 1
            if sibling_index < len(level_nodes):
                proof.append(level_nodes[sibling_index])
            index //= 2
        return proof

    # Функция проверки результата get_proof 
    def verify_proof(self, proof, target_hash, root_hash, index):
        current_hash = target_hash
        path = bin(index)[2:].zfill(int(log2(len(self.leaves))))
        for i in range(len(proof)):
            if proof[i]:
                if path[-i - 1] == "0":
                    current_hash = self.hash_function.digest(current_hash + proof[i])
                else:
                    current_hash = self.hash_function.digest(proof[i] + current_hash)
        return current_hash == root_hash
