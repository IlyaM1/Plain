from PyQt5 import QtWidgets, QtGui
from Widgets.NewRow import NewRow


class NewRowDialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()

        self.title = 'Тест'
        self.resize(400, 400)
        self.setFont(QtGui.QFont('Times', 13))
        self.layout = QtWidgets.QVBoxLayout()
        self.name = ''
        self.content = ''

        self.nameLayout = NewRow("Name: ")
        self.layout.addLayout(self.nameLayout)

        self.contentLayout = NewRow("Content: ")
        self.layout.addLayout(self.contentLayout)

        button = QtWidgets.QPushButton()
        button.setText('Сохранить')
        button.clicked.connect(self.save_row)
        self.layout.addWidget(button)

        self.setLayout(self.layout)

    def save_row(self):
        self.name = self.nameLayout.newInput.text()
        self.content = self.contentLayout.newInput.text()
        self.close()
