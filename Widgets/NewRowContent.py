from PyQt5 import QtWidgets


class NewRowContent(QtWidgets.QHBoxLayout):
    def __init__(self, name, content):
        super().__init__()
        # self.newLayout = QtWidgets.QHBoxLayout()

        self.newLabelName = QtWidgets.QLabel(name)
        self.newLabelContent = QtWidgets.QLineEdit(content)

        self.addWidget(self.newLabelName)
        self.addWidget(self.newLabelContent)
