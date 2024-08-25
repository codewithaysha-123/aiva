import sys
import cv2
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget
from aiva import *
from win10toast import ToastNotifier

class FaceRecognition(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Face Recognition")
        self.layout = QVBoxLayout()
        self.label = QLabel(self)
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)

        self.recognizer = cv2.face.LBPHFaceRecognizer_create()
        self.recognizer.read('trainer/trainer.yml')
        cascadePath = 'haarcascade_frontalface_default.xml'
        self.faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + cascadePath)

        self.font = cv2.FONT_HERSHEY_SIMPLEX

        self.id = 2
        self.names = ['', 'aysha']

        self.camer = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        self.camer.set(3, 640)
        self.camer.set(4, 480)

        self.minW = 0.1 * self.camer.get(3)
        self.minH = 0.1 * self.camer.get(4)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(10)

    def update_frame(self):
        ret, img = self.camer.read()

        converted_image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        height, width, channel = converted_image.shape
        bytesPerLine = 3 * width
        qImg = QImage(converted_image.data, width, height, bytesPerLine, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(qImg)
        self.label.setPixmap(pixmap)

        faces = self.faceCascade.detectMultiScale(
            converted_image,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(int(self.minW), int(self.minH)),
        )

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

            id, accuracy = self.recognizer.predict(converted_image[y:y + h, x:x + w])

            if accuracy < 100:
                accuracy = "  {0}%".format(round(100 - accuracy))
                permission = takeCommand()
                if "wake up" in permission:
                    TaskExe()

                elif 'goodbye' in permission:
                    speak("Thanks for Using Me Ma'am, have a great day...")
                    toast = ToastNotifier()
                    toast.show_toast("Aiva", "The Aiva is Now Deactivated!!!", duration=5)
                    sys.exit()

            else:
                id = "unknown"
                accuracy = "  {0}%".format(round(100 - accuracy))
                speak("Unauthorized Access!!")
                sys.exit()

            cv2.putText(img, str(id), (x + 5, y - 5), self.font, 1, (255, 255, 255), 2)
            cv2.putText(img, str(accuracy), (x + 5, y + h - 5), self.font, 1, (255, 255, 0), 1)

    def closeEvent(self, event):
        self.camer.release()
        cv2.destroyAllWindows()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Advanced Face Recognition Manager")
        self.setGeometry(100, 100, 640, 480)
        self.face_recognition_window = FaceRecognition()
        self.setCentralWidget(self.face_recognition_window)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
