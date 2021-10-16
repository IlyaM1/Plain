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

        self.nameLayout = NewRow("Name")
        self.layout.addLayout(self.nameLayout)

        self.button_new_row = QtWidgets.QPushButton()
        self.button_new_row.setText('Добавить новое поле')
        self.button_new_row.clicked.connect(self.new_save_row)
        self.layout.addWidget(self.button_new_row)

        button_save = QtWidgets.QPushButton()
        button_save.setText('Сохранить')
        button_save.clicked.connect(self.save_note)
        self.layout.addWidget(button_save)

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

    def save_note(self):
        # newNote = QtWidgets.QListWidgetItem()
        # dialog = NewNoteDialog(self.noteDict)
        #
        # dialog.show()
        # dialog.exec()
        #
        # newNote.setText("id: content")
        # newNote.setFont(QtGui.QFont("Times New Roman", 32))
        # self.ui.listWidget.addItem(newNote)
        self.noteDict.append({'name': self.nameLayout.newInput.text()})
        print("Exited New Note")
        self.close()
