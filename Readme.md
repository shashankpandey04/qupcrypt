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

