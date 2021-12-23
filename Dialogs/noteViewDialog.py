from PyQt5 import QtWidgets, QtGui
from Widgets.NewRow import NewRow
from Dialogs.NewRowDialog import NewRowDialog
from Widgets.NewRowContent import NewRowContent
from PyQt5.QtWidgets import QMessageBox
from Database import Database


class noteViewDialog(QtWidgets.QDialog):
    def __init__(self, note, user):
        super().__init__()
        # self.db.User[self.user.username].deleteMany({})
        # self.db = Database.get_instance()
        self.title = 'Тест'
        self.resize(400, 400)
        self.setFont(QtGui.QFont('Times', 13))
        self.layout = QtWidgets.QVBoxLayout()
        self.noteDict = note
        self.amountOfRows = 1
        self.id = note['_id']
        self.user = user

        self.nameLayout = NewRowContent("Name", self.noteDict['name'])
        self.layout.addLayout(self.nameLayout)

        self.list_of_inputs = []
        for i in note:
            if i != '_id' and i != 'name':
                inputItem = NewRowContent(i, note[i])
                self.list_of_inputs.append(inputItem)
                self.layout.addItem(inputItem)

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
        self.noteDict['name'] = self.nameLayout.newLabelContent.text()
        for i in self.list_of_inputs:
            self.noteDict[i.newLabelName.text()] = i.newLabelContent.text()
        try:
            Database.replace_one_note(self.user, self.id, self.noteDict)
        except Exception:
            print("Error: ", Exception)
        finally:
            self.close()
