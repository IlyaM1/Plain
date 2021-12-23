from PyQt5 import QtWidgets, QtGui
from Widgets.NewRow import NewRow
from Dialogs.NewRowDialog import NewRowDialog
from Widgets.NewRowContent import NewRowContent
from PyQt5.QtWidgets import QMessageBox
from Dialogs.ErrorDialog import ErrorDialog


class NewNoteDialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.title = 'Тест'
        self.resize(400, 400)
        self.setFont(QtGui.QFont('Times', 13))
        self.layout = QtWidgets.QVBoxLayout()
        self.noteDict = {"name": ""}
        self.amountOfRows = 1

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
        dialog = NewRowDialog()
        dialog.show()
        dialog.exec()
        self.noteDict[dialog.name] = dialog.content
        new_row = NewRowContent(dialog.name, dialog.content)
        self.layout.insertLayout(self.amountOfRows, new_row)
        self.amountOfRows += 1

    def save_note(self):
        try:
            name_text = self.nameLayout.newInput.text()
            if not name_text or name_text == '':
                raise ValueError
            else:
                self.noteDict["name"] = name_text
            self.close()
        except ValueError:
            ErrorDialog('Empty message')
