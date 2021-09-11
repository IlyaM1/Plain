from PyQt5 import QtWidgets, QtGui, QtCore, Qt
from des import Ui_MainWindow  # импорт нашего сгенерированного файла
from getDatabase import Database
import sys


class NewRow(QtWidgets.QHBoxLayout):
    def __init__(self, text1):
        super().__init__()
        print("yes")
        # self.newLayout = QtWidgets.QHBoxLayout()

        self.newLabel = QtWidgets.QLabel(text1)
        self.newInput = QtWidgets.QLineEdit("")

        self.addWidget(self.newLabel)
        self.addWidget(self.newInput)


class User():
    def __init__(self):
        self.notes = {}


class Note():
    def __init__(self, name, content):
        self.name = name
        self.content = content


"""
name:""
content: ""
data: ""
"""


class NewRowDialog(QtWidgets.QDialog):
    def __init__(self, noteDict):
        super().__init__()

        self.title = 'Тест'
        self.resize(400, 400)
        self.setFont(QtGui.QFont('Times', 13))
        self.layout = QtWidgets.QVBoxLayout()
        self.noteDict = noteDict

        self.nameLayout = NewRow("Name: ")
        self.layout.addLayout(self.nameLayout)

        self.contentLayout = NewRow("Content: ")
        self.layout.addLayout(self.contentLayout)

        button = QtWidgets.QPushButton()
        button.setText('Сохранить')
        button.clicked.connect(self.new_save_row)
        self.layout.addWidget(button)

        self.setLayout(self.layout)

    def save_row(self):
        self.noteDict[self.nameLayout.newLabel.text()] = self.nameLayout.newInput.text()
        self.noteDict[self.contentLayout.newLabel.text()] = self.contentLayout.newInput.text()
        print("2: ", self.noteDict)
        self.close()


class NewNoteDialog(QtWidgets.QDialog):
    def __init__(self, noteDict):
        super().__init__()
        self.title = 'Тест'
        self.resize(400, 400)
        self.setFont(QtGui.QFont('Times', 13))
        self.layout = QtWidgets.QVBoxLayout()
        self.noteDict = noteDict

        nameLayout = NewRow("Name")
        self.layout.addLayout(nameLayout)

        button = QtWidgets.QPushButton()
        button.setText('Добавить новое поле')
        button.clicked.connect(self.new_save_row)
        self.layout.addWidget(button)

        button = QtWidgets.QPushButton()
        button.setText('Сохранить')
        # button.clicked.connect(self.newNoteClick)
        self.layout.addWidget(button)

        self.setLayout(self.layout)

    def new_save_row(self):
        # newNote = QtWidgets.QListWidgetItem()
        print(self.noteDict)
        dialog = NewRowDialog(self.noteDict)
        print(self.noteDict)
        dialog.show()
        dialog.exec()

        # newNote.setText("id: content")
        # newNote.setFont(QtGui.QFont("Times New Roman", 32))
        # self.layout.addWidget(newNote)

    def newNoteClick(self):
        newNote = QtWidgets.QListWidgetItem()
        dialog = NewNoteDialog(self.noteDict)

        dialog.show()
        dialog.exec()

        newNote.setText("id: content")
        newNote.setFont(QtGui.QFont("Times New Roman", 32))
        self.ui.listWidget.addItem(newNote)


class Main_window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main_window, self).__init__()
        self.db = Database.get_instance()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.noteDict = {}
        self.ui.pushButton.clicked.connect(self.new_note_click)

    def new_note_click(self):
        new_note = QtWidgets.QListWidgetItem()
        dialog = NewNoteDialog(self.noteDict)

        dialog.show()
        dialog.exec()

        new_note.setText("id: content")
        new_note.setFont(QtGui.QFont("Times New Roman", 32))
        self.ui.listWidget.addItem(new_note)


# dbname = getDatabase()
print("Connected to MongoDB Atlas")

app = QtWidgets.QApplication([])
application = Main_window()
application.show()

sys.exit(app.exec())
