from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

class WebCryption:
    def __init__(self, key):
        self.key = self._process_key(key)
        self.processed_key_bytes = self.key.encode('utf-8')

    def _process_key(self, key):
        key = key.encode('utf-8')  # Ensure key is in bytes

        if len(key) < 16:
            key = key.ljust(16, b'\0')
        elif len(key) < 24:
            key = key.ljust(24, b'\0')
        elif len(key) < 32:
            key = key.ljust(32, b'\0')
        elif len(key) > 32:
            key = key[:32]
        
        return key.decode('utf-8')  # Decode back to Unicode string

    def _calculate_shift_value(self):
        last_char = str(self.key[-1])  # Ensure last_char is a string representation

        if last_char.isdigit():
            shift_value = int(last_char)
        elif last_char.isalpha():
            shift_value = ord(last_char)
        else:
            shift_value = 0
        
        shift_value += len(self.key)
        return shift_value

    def _shift_ciphertext(self, data: bytes, shift_value: int) -> bytes:
        return bytes((byte + shift_value) % 256 for byte in data)

    def _unshift_ciphertext(self, data: bytes, shift_value: int) -> bytes:
        return bytes((byte - shift_value) % 256 for byte in data)

    def create(self, identifier: str) -> str:
        # Encrypt the identifier using AES CBC mode
        cipher = AES.new(self.processed_key_bytes, AES.MODE_CBC, self.processed_key_bytes[:16])
        encrypted_data = cipher.encrypt(pad(identifier.encode('utf-8'), AES.block_size))
        
        # Calculate shift value based on the processed key
        shift_value = self._calculate_shift_value()
        
        # Shift the ciphertext
        encrypted_data_shifted = self._shift_ciphertext(encrypted_data, shift_value)
        
        # Encode to base64 for output
        encrypted_data_base64 = base64.b64encode(encrypted_data_shifted).decode('utf-8')
        
        return encrypted_data_base64

    def decrypt(self, encrypted_token: str) -> str:
        # Decode from base64
        encrypted_data_shifted = base64.b64decode(encrypted_token.encode('utf-8'))
        
        # Calculate shift value based on the processed key
        shift_value = self._calculate_shift_value()
        
        # Unshift the ciphertext
        encrypted_data = self._unshift_ciphertext(encrypted_data_shifted, shift_value)
        
        # Decrypt using AES CBC mode
        cipher = AES.new(self.processed_key_bytes, AES.MODE_CBC, self.processed_key_bytes[:16])
        decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size).decode('utf-8', errors='ignore')
        
        return decrypted_data

    def verify(self, encrypted_token: str) -> bool:
        try:
            self.decrypt(encrypted_token)
            return True
        except Exception as e:
            print(f"Token verification failed: {str(e)}")
            return False

#web_cryption = WebCryption("your_secret_key")
#token = web_cryption.create("any_parameter_request_body")
#decrypt = web_cryption.decrypt(token)
#is_valid = web_cryption.verify(token)
#if is_valid:
#    print(f"Token is valid. Access granted.")
#else:
#    print(f"Token is invalid. Access denied.")
#
# This code snippet demonstrates how to use the WebCryption class to create, decrypt, and verify tokens. 
# The WebCryption class provides methods for creating encrypted tokens, decrypting tokens, and verifying the validity of tokens. 
# The create method encrypts an identifier using AES CBC mode, the decrypt method decrypts an encrypted token, 
# and the verify method checks the validity of a token by attempting to decrypt it. 
# The class uses a key to process the encryption and decryption operations, 
# ensuring that the tokens are secure and tamper-proof. 
# The example code shows how to create a WebCryption instance with a secret key, create an encrypted token, decrypt the token,
# and verify its validity. The output of the verification process determines whether the token is valid 
# and can be used for access control or authentication purposes.