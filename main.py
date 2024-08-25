import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from password_gui import PasswordManager
from facerecognition_gui import FaceRecognition

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Aysha's Intelligent Virtual Assistant")
        self.layout = QVBoxLayout()

        self.password_button = QPushButton("Password")
        self.password_button.clicked.connect(self.open_password_manager)

        self.face_recognition_button = QPushButton("Face Recognition")
        self.face_recognition_button.clicked.connect(self.open_face_recognition)

        self.layout.addWidget(self.password_button)
        self.layout.addWidget(self.face_recognition_button)

        self.setLayout(self.layout)

    def open_password_manager(self):
        self.password_manager = PasswordManager()
        self.password_manager.show()

    def open_face_recognition(self):
        self.face_recognition = FaceRecognition()
        self.face_recognition.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
