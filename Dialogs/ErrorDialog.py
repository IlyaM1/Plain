from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QFont


class ErrorDialog:
    def __init__(self, text):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText(text)
        msgBox.setFont(QFont("Times", 10))
        msgBox.setWindowTitle("Error")
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.show()
        msgBox.exec()
