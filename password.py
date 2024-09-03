from aiva import *
from cryptography.fernet import Fernet
import getpass

# Generate a key for encryption/decryption
def generate_key():
    return Fernet.generate_key()

# Encrypt the password using the provided key
def encrypt_password(password, key):
    cipher_suite = Fernet(key)
    encrypted_password = cipher_suite.encrypt(password.encode())
    return encrypted_password

# Decrypt the password using the provided key
def decrypt_password(encrypted_password, key):
    cipher_suite = Fernet(key)
    decrypted_password = cipher_suite.decrypt(encrypted_password).decode()
    return decrypted_password

# Function to set the password
def set_password():
    key = generate_key()
    password = getpass.getpass(prompt="Enter your new password: ")
    encrypted_password = encrypt_password(password, key)
    with open("password.txt", "wb") as file:
        file.write(encrypted_password)
    with open("key.txt", "wb") as file:
        file.write(key)
    print("Password set successfully.")

# Function to reset the password
def reset_password():
    set_password()

# Function to authenticate the user
def authenticate_password():
    try:
        with open("password.txt", "rb") as file:
            encrypted_password = file.read()
        with open("key.txt", "rb") as file:
            key = file.read()
        password = getpass.getpass(prompt="Enter your password: ")
        decrypted_password = decrypt_password(encrypted_password, key)
        if password == decrypted_password:
            print("Authentication successful.")
            return True
        else:
            print("Authentication failed. Incorrect password.")
            return False
    except FileNotFoundError:
        print("Password has not been set yet.")
        return False


