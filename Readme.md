# Qupcrypt

Qupcrypt is a custom encryption library designed to provide a simple and secure way to encrypt and decrypt data using the AES (Advanced Encryption Standard) algorithm. This library is easy to use, making it suitable for both beginners and advanced users who need to secure their data.

## Features

- **AES Encryption**: Uses AES-256-CBC for strong encryption.
- **Simple API**: Easy-to-use API for encrypting and decrypting data.
- **Secure Key Management**: Utilizes SHA-256 to derive a secure key from a passphrase.
- **Padding and Unpadding**: Automatically handles padding and unpadding of data.
- **Base64 Encoding**: Encodes encrypted data in Base64 for easy storage and transmission.

## Installation

You can install Qupcrypt using pip:

```sh
pip install qupcrypt
```
## Usage
- Here is a quick example of how to use Qupcrypt to encrypt and decrypt data:

- WebCryption
``` python
from qupcrypt.WebCrypt import WebCryption  # Assuming WebCrypt.py contains your WebCryption class implementation

def test_web_cryption():
    # Initialize WebCryption with a key
    web_cryption = WebCryption("your_secret_key")

    # Test case 1: Create and decrypt a token
    identifier = "any_parameter_from_request_body"
    encrypted_token = web_cryption.create(identifier)
    decrypted_data = web_cryption.decrypt(encrypted_token)
    
    assert decrypted_data == identifier
    print(f"Test case 1 passed. Encrypted Token: {encrypted_token}, Decrypted Data: {decrypted_data}")

    # Test case 2: Verify a valid token
    is_valid = web_cryption.verify(encrypted_token)
    assert is_valid is True
    print("Test case 2 passed. Token is valid.")

    # Test case 3: Verify an invalid token (modify token to simulate invalidity)
    invalid_token = encrypted_token[:-1] + '0'  # Modify the last character to invalidate
    is_valid = web_cryption.verify(invalid_token)
    assert is_valid is False
    print("Test case 3 passed. Token is invalid.")

if __name__ == "__main__":
    test_web_cryption()
```

- CustomAES
``` python
from qupcrypt.ext import CustomAES

key = b'shashankpandey04'
custom_aes = CustomAES(key)

# Encrypt data
encrypted_data = custom_aes.encrypt("Hello, World!")
print("Encrypted",encrypted_data)

# Decrypt data
decrypted_data = custom_aes.decrypt(encrypted_data)
print("Decrypted:", decrypted_data)

```

- SimpleEncryptor
``` python

from qupcrypt import SimpleEncryptor

# Initialize the encryptor with a secret key
key = "your_secret_key"
encryptor = SimpleEncryptor(key)

# Encrypt data
data = "Hello, World!"
encrypted = encryptor.encrypt(data)
print(f"Encrypted: {encrypted}")

# Decrypt data
decrypted = encryptor.decrypt(encrypted)
print(f"Decrypted: {decrypted}")
```

## How It Works
- **Key Derivation:** The provided passphrase is hashed using SHA-256 to create a secure key.
- **Data Padding:** The data is padded to make its length a multiple of the AES block size.
- **Encryption:** The padded data is encrypted using AES-256-CBC with a randomly generated initialization vector (IV).
- **Encoding:** The IV and encrypted data are concatenated and encoded in Base64 for easy storage and transmission.
- **Decryption:** The process is reversed to decrypt the data back to its original form.

## Contributing
Contributions are welcome! If you have any ideas, suggestions, or bug reports, please create an issue or submit a pull request on GitHub.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Disclaimer
While Qupcrypt aims to provide strong encryption, it is important to note that cryptography is a complex field and improper use can lead to security vulnerabilities. Always make sure to follow best practices and consult with security experts when in doubt.

