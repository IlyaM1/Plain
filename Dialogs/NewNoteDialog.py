from PyQt5 import QtWidgets, QtGui
from Widgets.NewRow import NewRow
from Dialogs.NewRowDialog import NewRowDialog


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
