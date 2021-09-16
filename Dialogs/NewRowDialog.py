from PyQt5 import QtWidgets, QtGui
from Widgets.NewRow import NewRow


class NewRowDialog(QtWidgets.QDialog):
    def __init__(self, noteDict):
        super().__init__()
        print(1)

        self.title = 'Тест'
        self.resize(400, 400)
        self.setFont(QtGui.QFont('Times', 13))
        self.layout = QtWidgets.QVBoxLayout()
        self.noteDict = noteDict
        print(2)

        self.nameLayout = NewRow("Name: ")
        self.layout.addLayout(self.nameLayout)
        print(3)

        self.contentLayout = NewRow("Content: ")
        self.layout.addLayout(self.contentLayout)
        print(4)

        button = QtWidgets.QPushButton()
        button.setText('Сохранить')
        button.clicked.connect(self.save_row)
        self.layout.addWidget(button)
        print(5)

        self.setLayout(self.layout)
        print(6)

    def save_row(self):
        self.noteDict[self.nameLayout.newLabel.text()] = self.nameLayout.newInput.text()
        self.noteDict[self.contentLayout.newLabel.text()] = self.contentLayout.newInput.text()
        print("2: ", self.noteDict)
        self.close()
