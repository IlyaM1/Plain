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
        print(self.user.username)
        self.db = Database.get_instance()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.noteDict = {}
        self.ui.pushButton.clicked.connect(self.new_note_click)

    def new_note_click(self):
        new_note = QtWidgets.QListWidgetItem()
        checkDict  = self.noteDict
        dialog = NewNoteDialog()

        dialog.show()
        dialog.exec()

        if dialog.noteDict != checkDict:
            print("Not same")

        print("Same")
        self.noteDict = dialog.noteDict
        print(self.noteDict)
        # new_note.setText("id: content")
        # new_note.setFont(QtGui.QFont("Times New Roman", 32))
        # self.ui.listWidget.addItem(new_note)


app = QtWidgets.QApplication([])
auth = AuthorizationDialog()
auth.show()
auth.exec()
print("Start Main Window")
print(auth.user)
application = main_window(auth.user)
application.show()
sys.exit(app.exec())
