import sys

from PyQt5 import QtWidgets, QtGui, QtCore, Qt
from des import Ui_MainWindow  # импорт нашего сгенерированного файла

from Database import Database
from Dialogs.AuthorizationDialog import AuthorizationDialog
from Dialogs.NewNoteDialog import NewNoteDialog


class Main_window(QtWidgets.QMainWindow):
    def __init__(self, user):
        super(Main_window, self).__init__()
        self.user = user
        print(self.user.username)
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


app = QtWidgets.QApplication([])
auth = AuthorizationDialog()
auth.show()
auth.exec()
application = Main_window(auth.user)
application.show()

sys.exit(app.exec())
