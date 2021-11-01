import sys

from PyQt5 import QtWidgets, QtGui, QtCore, Qt
from des import Ui_MainWindow  # импорт нашего сгенерированного файла

from Database import Database
from Dialogs.AuthorizationDialog import AuthorizationDialog
from Dialogs.NewNoteDialog import NewNoteDialog


class main_window(QtWidgets.QMainWindow):
    def __init__(self, user):
        super(main_window, self).__init__()
        self.user = user
        self.db = Database.get_instance()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.dict = {}
        self.ui.pushButton.clicked.connect(self.new_note_click)

    def new_note_click(self):
        new_note = QtWidgets.QListWidgetItem()
        dialog = NewNoteDialog()

        dialog.show()
        dialog.exec()

        new_note_dict = dialog.noteDict
        self.db.User[self.user.username].insert_one(new_note_dict)


app = QtWidgets.QApplication([])
auth = AuthorizationDialog()
auth.show()
auth.exec()
application = main_window(auth.user)
application.show()
sys.exit(app.exec())
