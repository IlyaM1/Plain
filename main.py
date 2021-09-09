from PyQt5 import QtWidgets, QtGui, QtCore, Qt
from des import Ui_MainWindow  # импорт нашего сгенерированного файла
from getDatabase import getDatabase
import sys


class newRow(QtWidgets.QHBoxLayout):
    def __init__(self, text1):
        super().__init__()
        print("yes")
        # self.newLayout = QtWidgets.QHBoxLayout()

        self.newLabel = QtWidgets.QLabel(text1)
        self.newInput = QtWidgets.QLineEdit("")

        self.addWidget(self.newLabel)
        self.addWidget(self.newInput)



class newRowDialog(QtWidgets.QDialog):
    def __init__(self, noteDict):
        super().__init__()

        self.title = 'Тест'
        self.resize(400, 400)
        self.setFont(QtGui.QFont('Times', 13))
        self.layout = QtWidgets.QVBoxLayout()
        self.noteDict = noteDict

        self.nameLayout = newRow("Name: ")
        self.layout.addLayout(self.nameLayout)

        self.contentLayout = newRow("Content: ")
        self.layout.addLayout(self.contentLayout)

        button = QtWidgets.QPushButton()
        button.setText('Сохранить')
        button.clicked.connect(self.saveRow)
        self.layout.addWidget(button)

        self.setLayout(self.layout)

    def saveRow(self):
        # self.noteDict[self.layout.nameLayout.newLabel.text()] = self.layout.nameLayout.newInput.text()
        print((self.nameLayout.newLabel.text()))
        print("2: ", self.noteDict)


class newNoteDialog(QtWidgets.QDialog):
    def __init__(self, noteDict):
        super().__init__()
        self.title = 'Тест'
        self.resize(400, 400)
        self.setFont(QtGui.QFont('Times', 13))
        self.layout = QtWidgets.QVBoxLayout()
        self.noteDict = noteDict

        nameLayout = self.newRow("Name")
        self.layout.addLayout(nameLayout)

        button = QtWidgets.QPushButton()
        button.setText('Добавить новое поле')
        button.clicked.connect(self.newSaveRow)
        self.layout.addWidget(button)

        button = QtWidgets.QPushButton()
        button.setText('Добавить новую запись')
        button.clicked.connect(self.newNoteClick)
        self.layout.addWidget(button)

        button = QtWidgets.QPushButton()
        button.setText('Сохранить')
        # button.clicked.connect(self.newNoteClick)
        self.layout.addWidget(button)

        self.setLayout(self.layout)

    def newRow(self, text1):
        newLayout = QtWidgets.QHBoxLayout()

        newLabel = QtWidgets.QLabel(text1)
        newInput = QtWidgets.QLineEdit("")

        newLayout.addWidget(newLabel)
        newLayout.addWidget(newInput)

        # self.addWidget(newLayout)
        return newLayout

    def newSaveRow(self):
        # newNote = QtWidgets.QListWidgetItem()
        print(self.noteDict)
        dialog = newRowDialog(self.noteDict)
        print(self.noteDict)
        dialog.show()
        dialog.exec()

        # newNote.setText("id: content")
        # newNote.setFont(QtGui.QFont("Times New Roman", 32))
        # self.layout.addWidget(newNote)

    def newNoteClick(self):
        newNote = QtWidgets.QListWidgetItem()
        dialog = newNoteDialog(self.noteDict)

        dialog.show()
        dialog.exec()

        newNote.setText("id: content")
        newNote.setFont(QtGui.QFont("Times New Roman", 32))
        self.ui.listWidget.addItem(newNote)


class myWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(myWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.noteDict = {}
        self.ui.pushButton.clicked.connect(self.newNoteClick)

    def newNoteClick(self):
        newNote = QtWidgets.QListWidgetItem()
        dialog = newNoteDialog(self.noteDict)

        dialog.show()
        dialog.exec()

        newNote.setText("id: content")
        newNote.setFont(QtGui.QFont("Times New Roman", 32))
        self.ui.listWidget.addItem(newNote)


dbname = getDatabase()
print("Connected to MongoDB Atlas")

app = QtWidgets.QApplication([])
application = myWindow()
application.show()

sys.exit(app.exec())
