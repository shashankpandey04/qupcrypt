# encryption.py
import base64
import hashlib
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

class SimpleEncryptor:
    def __init__(self, key: str):
        self.key = hashlib.sha256(key.encode()).digest()

    def pad(self, data: bytes) -> bytes:
        return data + b'\0' * (AES.block_size - len(data) % AES.block_size)

    def encrypt(self, data: str) -> str:
        data = self.pad(data.encode())
        iv = get_random_bytes(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        encrypted = cipher.encrypt(data)
        return base64.b64encode(iv + encrypted).decode('utf-8')

    def decrypt(self, encrypted: str) -> str:
        encrypted = base64.b64decode(encrypted)
        iv = encrypted[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        data = cipher.decrypt(encrypted[AES.block_size:]).rstrip(b'\0')
        return data.decode('utf-8')
