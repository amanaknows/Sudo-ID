import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend

# ------------------------------
# Secure Encryption and Decryption System
# For Blackbox Implementation
# ------------------------------

# Function to generate a secure encryption key
def generate_key():
    """
    Generates a 256-bit (32-byte) key for AES encryption.
    Key must be stored securely for decryption.
    """
    return os.urandom(32)  # Generates a random 256-bit key

# Function to encrypt source code
def encrypt_code(source_code, key):
    """
    Encrypts the provided source code using AES encryption in CBC mode.

    Parameters:
        source_code (str): The source code to be encrypted.
        key (bytes): A 256-bit key used for encryption.

    Returns:
        bytes: The encrypted data with IV prepended.
    """
    iv = os.urandom(16)  # Initialization vector (16 bytes)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    # Pad source code to align with AES block size
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(source_code.encode()) + padder.finalize()

    # Encrypt the padded data
    encrypted_code = encryptor.update(padded_data) + encryptor.finalize()
    return iv + encrypted_code  # Return IV + encrypted data

# Function to decrypt source code
def decrypt_code(encrypted_code, key):
    """
    Decrypts the encrypted source code using AES encryption in CBC mode.

    Parameters:
        encrypted_code (bytes): The encrypted data (IV prepended).
        key (bytes): A 256-bit key used for decryption.

    Returns:
        str: The decrypted source code.
    """
    iv = encrypted_code[:16]  # Extract IV (first 16 bytes)
    encrypted_code = encrypted_code[16:]  # Extract the encrypted data

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()

    # Decrypt the data
    decrypted_padded_code = decryptor.update(encrypted_code) + decryptor.finalize()

    # Unpad the decrypted data
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    decrypted_code = unpadder.update(decrypted_padded_code) + unpadder.finalize()

    return decrypted_code.decode()

# Main execution for blackbox environment
if __name__ == "__main__":
    # Original source code to be encrypted
    source_code = """
# Blackbox Secure Script
def hello_sunshine():
    print("Hello, Lord Sunshine! This script is encrypted for your safety.")

if __name__ == "__main__":
    hello_sunshine()
"""

    # Step 1: Generate an encryption key
    key = generate_key()

    # Step 2: Encrypt the source code
    encrypted_code = encrypt_code(source_code, key)

    # Step 3: Save the encrypted code and key to secure files
    encrypted_file_path = "blackbox_encrypted_script.bin"
    key_file_path = "blackbox_encryption_key.bin"

    # Save encrypted code
    with open(encrypted_file_path, "wb") as encrypted_file:
        encrypted_file.write(encrypted_code)

    # Save the encryption key (must be stored securely)
    with open(key_file_path, "wb") as key_file:
        key_file.write(key)

    print(f"Encryption complete. Encrypted script saved to {encrypted_file_path}")
    print(f"Encryption key saved to {key_file_path} (store securely)")

    # Step 4: (Optional) Decrypt the code and execute
    with open(encrypted_file_path, "rb") as encrypted_file:
        encrypted_code = encrypted_file.read()

    with open(key_file_path, "rb") as key_file:
        key = key_file.read()

    decrypted_code = decrypt_code(encrypted_code, key)
    print("Decrypted Code Executing Below:")
    exec(decrypted_code)
