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
