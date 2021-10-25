from PyQt5 import QtWidgets


class NewRow(QtWidgets.QHBoxLayout):
    def __init__(self, text1):
        super().__init__()
        # self.newLayout = QtWidgets.QHBoxLayout()

        self.newLabel = QtWidgets.QLabel(text1)
        self.newInput = QtWidgets.QLineEdit("")

        self.addWidget(self.newLabel)
        self.addWidget(self.newInput)
