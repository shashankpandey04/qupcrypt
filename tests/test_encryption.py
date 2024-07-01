# test_encryption.py
import unittest
from qupcrypt.encryption import SimpleEncryptor

class TestSimpleEncryptor(unittest.TestCase):
    def test_encryption_decryption(self):
        key = "test_key"
        encryptor = SimpleEncryptor(key)
        data = "Hello, World!"
        encrypted = encryptor.encrypt(data)
        decrypted = encryptor.decrypt(encrypted)
        self.assertEqual(data, decrypted)

if __name__ == '__main__':
    unittest.main()
