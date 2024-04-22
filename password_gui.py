import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
import os
from password import *

class PasswordManager(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Password Manager")
        self.layout = QVBoxLayout()
        self.current_password = None
        self.setup_ui()

    def setup_ui(self):
        if not os.path.exists("password.txt"):
            self.set_password_ui()
        else:
            self.authenticate_password_ui()

        self.setLayout(self.layout)

    def set_password_ui(self):
        self.password_label = QLabel("Create a new password:")
        self.password_input = QLineEdit()
        self.submit_button = QPushButton("Submit")
        self.submit_button.clicked.connect(self.submit_password)
        
        self.layout.addWidget(self.password_label)
        self.layout.addWidget(self.password_input)
        self.layout.addWidget(self.submit_button)

    def authenticate_password_ui(self):
        self.password_label = QLabel("Enter your password:")
        self.password_input = QLineEdit()
        self.submit_button = QPushButton("Submit")
        self.submit_button.clicked.connect(self.authenticate)

        self.reset_button = QPushButton("Reset Password")
        self.reset_button.clicked.connect(self.reset_password)

        self.layout.addWidget(self.password_label)
        self.layout.addWidget(self.password_input)
        self.layout.addWidget(self.submit_button)
        self.layout.addWidget(self.reset_button)

    def reset_password_ui(self):
        self.password_label = QLabel("Create a new password:")
        self.password_input = QLineEdit()
        self.submit_button = QPushButton("Submit")
        self.submit_button.clicked.connect(self.submit_password)

        self.layout.addWidget(self.password_label)
        self.layout.addWidget(self.password_input)
        self.layout.addWidget(self.submit_button)

    def submit_password(self):
        key = generate_key()
        password = self.password_input.text()
        encrypted_password = encrypt_password(password, key)
        with open("password.txt", "wb") as file:
            file.write(encrypted_password)
        with open("key.txt", "wb") as file:
            file.write(key)
        self.current_password = password
        self.layout.removeWidget(self.password_label)
        self.layout.removeWidget(self.password_input)
        self.layout.removeWidget(self.submit_button)
        self.reset_password_ui()

    def authenticate(self):
        try:
            with open("password.txt", "rb") as file:
                encrypted_password = file.read()
            with open("key.txt", "rb") as file:
                key = file.read()
            password = self.password_input.text()
            decrypted_password = decrypt_password(encrypted_password, key)
            if password == decrypted_password:
                print("Authentication successful.")
                self.layout.removeWidget(self.password_label)
                self.layout.removeWidget(self.password_input)
                self.layout.removeWidget(self.submit_button)
                self.layout.removeWidget(self.reset_button)
                print("Welcome to AIVA!")
                TaskExe()
            else:
                print("Authentication failed. Incorrect password.")
        except FileNotFoundError:
            print("Password has not been set yet.")

    def reset_password(self):
        os.remove("password.txt")
        os.remove("key.txt")
        self.layout.removeWidget(self.password_label)
        self.layout.removeWidget(self.password_input)
        self.layout.removeWidget(self.submit_button)
        self.layout.removeWidget(self.reset_button)
        self.set_password_ui()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PasswordManager()
    window.show()
    sys.exit(app.exec_())
