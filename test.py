from SHA256.sha256 import SHA256
from MerkleTree.MerkleTree import MerkleTree
from hashlib import sha256
import unittest
from testcases.testcases import TEST1, TEST2, TEST3, TEST4, TEST5,\
                                TEST6, TEST7, TEST8, TEST9, TEST10


class TestSHA256(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sha256_hash = sha256()
        cls.sha256_hash_custom = SHA256()

    def setUp(self):
        self.sha256_hash = sha256()
        self.sha256_hash_custom.reset()

    def test01(self):
        self.sha256_hash.update(TEST1)
        self.sha256_hash_custom.update(TEST1)
        self.assertEqual(self.sha256_hash_custom.hexdigest(), self.sha256_hash.hexdigest())

    def test02(self):
        self.sha256_hash.update(TEST2)
        self.sha256_hash_custom.update(TEST2)
        self.assertEqual(self.sha256_hash_custom.hexdigest(), self.sha256_hash.hexdigest())

    def test03(self):
        self.sha256_hash.update(TEST3)
        self.sha256_hash_custom.update(TEST3)
        self.assertEqual(self.sha256_hash_custom.hexdigest(), self.sha256_hash.hexdigest())

    def test04(self):
        self.sha256_hash.update(TEST4)
        self.sha256_hash_custom.update(TEST4)
        self.assertEqual(self.sha256_hash_custom.hexdigest(), self.sha256_hash.hexdigest())

    def test05(self):
        self.sha256_hash.update(TEST5)
        self.sha256_hash_custom.update(TEST5)
        self.assertEqual(self.sha256_hash_custom.hexdigest(), self.sha256_hash.hexdigest())

    def test06(self):
        self.sha256_hash.update(TEST6)
        self.sha256_hash_custom.update(TEST6)
        self.assertEqual(self.sha256_hash_custom.hexdigest(), self.sha256_hash.hexdigest())

    def test07(self):
        self.sha256_hash.update(TEST7)
        self.sha256_hash_custom.update(TEST7)
        self.assertEqual(self.sha256_hash_custom.hexdigest(), self.sha256_hash.hexdigest())

    def test08(self):
        self.sha256_hash.update(TEST8)
        self.sha256_hash_custom.update(TEST8)
        self.assertEqual(self.sha256_hash_custom.hexdigest(), self.sha256_hash.hexdigest())

    def test09(self):
        self.sha256_hash.update(TEST9)
        self.sha256_hash_custom.update(TEST9)
        self.assertEqual(self.sha256_hash_custom.hexdigest(), self.sha256_hash.hexdigest())

    def test10(self):
        self.sha256_hash.update(TEST10)
        self.sha256_hash_custom.update(TEST10)
        self.assertEqual(self.sha256_hash_custom.hexdigest(), self.sha256_hash.hexdigest())


class TestMerkleTree(unittest.TestCase):

    def setUp(self):
        self.data_list = [bytes([0xbd]), bytes([0xdd]), bytes([0xad]), bytes([0xcd]), bytes([0x00])]
        self.hash_list = [sha256(data).digest() for data in self.data_list]
        self.hash_function = SHA256()

    def test_build_tree(self):
        merkle_tree = MerkleTree(self.data_list, self.hash_function)
        self.assertIsNotNone(merkle_tree.tree)
        self.assertEqual(len(merkle_tree.tree), 4)

    def test_get_root(self):
        merkle_tree = MerkleTree(self.data_list, self.hash_function)
        root_hash = merkle_tree.get_root()
        expected_root_hash = sha256(sha256(self.hash_list[0]+ self.hash_list[1]).digest() +
                                    sha256(self.hash_list[2] + self.hash_list[3]).digest()
                                    ).digest() + self.hash_list[4]
        self.assertEqual(root_hash, sha256(expected_root_hash).digest())

    def test_get_proof(self):
        merkle_tree = MerkleTree(self.data_list, self.hash_function)
        proof_data2 = merkle_tree.get_proof(1)
        self.assertEqual(len(proof_data2), 3)

        expected_proof_data2 = [
            self.hash_list[0],
            sha256(self.hash_list[2] + self.hash_list[3]).digest(),
            self.hash_list[4]
        ]
        self.assertEqual(proof_data2, expected_proof_data2)

    def test_verify_proof(self):
        merkle_tree = MerkleTree(self.data_list, self.hash_function)
        target_hash = self.hash_list[1]
        proof_data2 = [
            self.hash_list[0],
            sha256(self.hash_list[2] + self.hash_list[3]).digest(),
            self.hash_list[4]
        ]
        root_hash = merkle_tree.get_root()
        self.assertTrue(merkle_tree.verify_proof(proof_data2, target_hash, root_hash, 1))


if __name__ == "__main__":
    unittest.main()
