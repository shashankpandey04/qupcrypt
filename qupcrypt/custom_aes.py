from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

class CustomAES:
    def __init__(self, key: bytes):
        self.key = pad(key, AES.block_size)
        self.cipher = AES.new(self.key, AES.MODE_CBC)

    def _shift_ciphertext(self, data: bytes, shift_value: int) -> bytes:
        return bytes((byte + shift_value) % 256 for byte in data)

    def _unshift_ciphertext(self, data: bytes, shift_value: int) -> bytes:
        return bytes((byte - shift_value) % 256 for byte in data)

    def _calculate_shift_value(self, key: bytes) -> int:
        last_char_value = ord(key[-1])
        numeric_sum = sum(int(char) for char in key.decode() if char.isdigit())
        shift_value = (last_char_value + numeric_sum + len(key)) % 256
        return shift_value

    def encrypt(self, data: str) -> str:
        data = pad(data.encode(), AES.block_size)
        encrypted_data = self.cipher.encrypt(data)
        shift_value = self._calculate_shift_value(self.key)
        shifted_data = self._shift_ciphertext(encrypted_data, shift_value)
        return base64.b64encode(self.cipher.iv + shifted_data).decode()

    def decrypt(self, encrypted_data: str) -> str:
        encrypted_data = base64.b64decode(encrypted_data)
        iv = encrypted_data[:AES.block_size]
        shifted_data = encrypted_data[AES.block_size:]
        shift_value = self._calculate_shift_value(self.key)
        unshifted_data = self._unshift_ciphertext(shifted_data, shift_value)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return unpad(cipher.decrypt(unshifted_data), AES.block_size).decode()
