from PyQt5 import QtWidgets, QtGui
from Widgets.NewRow import NewRow
from Dialogs.NewRowDialog import NewRowDialog
from Widgets.NewRowContent import NewRowContent
from PyQt5.QtWidgets import QMessageBox


class noteViewDialog(QtWidgets.QDialog):
    def __init__(self, note, user):
        super().__init__()
        self.title = 'Тест'
        self.resize(400, 400)
        self.setFont(QtGui.QFont('Times', 13))
        self.layout = QtWidgets.QVBoxLayout()
        self.noteDict = note
        self.amountOfRows = 1
        self.user = user
        # print(self.noteDict)

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
        # name_text = self.nameLayout.newInput.text()
        # if not name_text or name_text == '':
        #     noteViewDialog.__show_empty_message_error()
        # else:
        #     self.noteDict["name"] = name_text
        k = 0
        # print('list of inputs: ', self.list_of_inputs)
        for i in self.list_of_inputs:
            print(self.noteDict)
            if i.newLabelContent.text() != self.noteDict[i.newLabelName.text()]:
                self.db.User[self.user.username].replaceOne({'name': self.noteDict['name']}, self.noteDict)
        self.close()

    @staticmethod
    def __show_empty_message_error():
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Empty name")
        msgBox.setWindowTitle("Error")
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.show()
        msgBox.exec()
