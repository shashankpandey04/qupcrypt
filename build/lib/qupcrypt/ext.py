# custom_aes.py

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

class CustomAES:
    def __init__(self, key):
        # Ensure the key is processed to a valid AES key length
        self.key = self._process_key(key)

    def _process_key(self, key):
        # Example: using SHA-256 to derive a 32-byte key if necessary
        if len(key) < 16:
            key = key.ljust(16, b'\0')  # Pad with null bytes
        elif len(key) < 24:
            key = key.ljust(24, b'\0')  # Pad with null bytes
        elif len(key) < 32:
            key = key.ljust(32, b'\0')  # Pad with null bytes
        elif len(key) > 32:
            # Truncate if longer than 32 bytes
            key = key[:32]

        return key

    def _calculate_shift_value(self, key):
        # Get the last character of the key
        last_char = str(key[-1])  # Ensure last_char is a string representation
        
        # Determine shift value based on the type of last character
        if last_char.isdigit():
            shift_value = int(last_char)
        elif last_char.isalpha():
            # Use the ASCII value of the character
            shift_value = ord(last_char)
        else:
            # Default to a safe value if not a digit or alphabet
            shift_value = 0
        
        # Add the length of the key to the shift value
        shift_value += len(key)

        return shift_value

    def _shift_ciphertext(self, data: bytes, shift_value: int) -> bytes:
        return bytes((byte + shift_value) % 256 for byte in data)

    def _unshift_ciphertext(self, data: bytes, shift_value: int) -> bytes:
        return bytes((byte - shift_value) % 256 for byte in data)

    def encrypt(self, data):
        cipher = AES.new(self.key, AES.MODE_CBC, self.key[:16])
        encrypted_data = cipher.encrypt(pad(data.encode('utf-8'), AES.block_size))
        shift_value = self._calculate_shift_value(self.key)
        encrypted_data_shifted = self._shift_ciphertext(encrypted_data, shift_value)
        encrypted_data_base64 = base64.b64encode(encrypted_data_shifted)
        return encrypted_data_base64

    def decrypt(self, encrypted_data_base64):
        encrypted_data_shifted = base64.b64decode(encrypted_data_base64)
        shift_value = self._calculate_shift_value(self.key)
        encrypted_data = self._unshift_ciphertext(encrypted_data_shifted, shift_value)
        cipher = AES.new(self.key, AES.MODE_CBC, self.key[:16])
        decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)
        return decrypted_data.decode('utf-8', errors='ignore')
