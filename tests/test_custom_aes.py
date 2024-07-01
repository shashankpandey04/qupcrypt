import unittest
from qupcrypt.custom_aes import CustomAES

class TestCustomAES(unittest.TestCase):
    def test_encryption_decryption(self):
        key = b"my_secret_key_123"
        cipher = CustomAES(key)
        data = "Hello, World!"
        encrypted = cipher.encrypt(data)
        decrypted = cipher.decrypt(encrypted)
        self.assertEqual(data, decrypted)

    def test_encryption_decryption_with_numeric_key(self):
        key = b"my_s3cr3t_k3y"
        cipher = CustomAES(key)
        data = "Hello, World!"
        encrypted = cipher.encrypt(data)
        decrypted = cipher.decrypt(encrypted)
        self.assertEqual(data, decrypted)

if __name__ == '__main__':
    unittest.main()
