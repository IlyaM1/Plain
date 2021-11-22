from PyQt5.QtWidgets import QMessageBox


class ErrorDialog:
    def __init__(self, text):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText(text)
        msgBox.setWindowTitle("Error")
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.show()
        msgBox.exec()
