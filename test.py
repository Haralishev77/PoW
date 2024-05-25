from SHA256.sha256 import SHA256
from hashlib import sha256
import unittest
from test_sha256.testcases import TEST1, TEST2, TEST3, TEST4, TEST5, \
    TEST6, TEST7, TEST8, TEST9, TEST10, \
    TEST11, TEST12, TEST13


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

    # def test11(self):
    #     self.sha256_hash.update(TEST11)
    #     self.sha256_hash_custom.update(TEST11)
    #     self.assertEqual(self.sha256_hash_custom.hexdigest(), self.sha256_hash.hexdigest())

    # def test12(self):
    #     self.sha256_hash.update(TEST12)
    #     self.sha256_hash_custom.update(TEST12)
    #     self.assertEqual(self.sha256_hash_custom.hexdigest(), self.sha256_hash.hexdigest())
    #
    # def test13(self):
    #     self.sha256_hash.update(TEST13)
    #     self.sha256_hash_custom.update(TEST13)
    #     self.assertEqual(self.sha256_hash_custom.hexdigest(), self.sha256_hash.hexdigest())


if __name__ == "__main__":
    unittest.main()
