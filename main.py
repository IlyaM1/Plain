import sys

from PyQt5 import QtWidgets, QtGui, QtCore, Qt
from des import Ui_MainWindow

from Database import Database
from Dialogs.AuthorizationDialog import AuthorizationDialog
from Dialogs.NewNoteDialog import NewNoteDialog
from Dialogs.noteViewDialog import noteViewDialog
from Structures.Item import Item
from Dialogs.ErrorDialog import ErrorDialog


class main_window(QtWidgets.QMainWindow):
    def __init__(self, user):
        super(main_window, self).__init__()
        self.user = user
        try:
            self.db = Database.get_instance()
        except:
            ErrorDialog("Can't connect to Database")
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.dict = {}
        self.ui.listWidget.setCurrentRow(5)
        try:
            self.allNotes = list(self.db.User[self.user.username].find())
        except:
            ErrorDialog("Can't find notes")
        self.notesUpdate()

    def notesUpdate(self):
        try:
            self.allNotes = list(self.db.User[self.user.username].find())
        except:
            ErrorDialog("Can't find notes")
        self.ui.listWidget.clear()
        for i in self.allNotes:
            item = Item(i['name'], i)
            self.ui.listWidget.addItem(item)
        self.ui.listWidget.itemDoubleClicked.connect(self.slot_click_in_item)
        self.ui.pushButton.clicked.connect(self.new_note_click)

    def new_note_click(self):
        new_note = QtWidgets.QListWidgetItem()
        dialog = NewNoteDialog()

        dialog.show()
        dialog.exec()

        new_note_dict = dialog.noteDict
        self.db.User[self.user.username].insert_one(new_note_dict)
        self.notesUpdate()

    def slot_click_in_item(self, item):
        needed_note = None
        for i in self.allNotes:
            if i['_id'] == item.note['_id']:
                needed_note = i

        dialog = noteViewDialog(needed_note, self.user)

        dialog.show()
        dialog.exec()

        self.notesUpdate()


app = QtWidgets.QApplication([])
auth = AuthorizationDialog()
auth.show()
auth.exec()
application = main_window(auth.user)
application.show()
sys.exit(app.exec())
