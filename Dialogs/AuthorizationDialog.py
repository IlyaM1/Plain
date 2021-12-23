from PyQt5 import QtWidgets
from Widgets.NewRow import NewRow
from Database import Database
from Dialogs.SignUpDialog import SignUpDialog
from Structures.User import User
from Dialogs.ErrorDialog import ErrorDialog


class AuthorizationDialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()

        self.user = None
        # self.db = Database.get_instance()
        self.layoutAuth = QtWidgets.QVBoxLayout()

        self.login = NewRow("Login")
        self.layoutAuth.addLayout(self.login)

        self.password = NewRow("Password")
        self.layoutAuth.addLayout(self.password)

        buttonLog = QtWidgets.QPushButton("Log In")
        buttonLog.clicked.connect(self.logInButtonPush)
        self.layoutAuth.addWidget(buttonLog)

        buttonSign = QtWidgets.QPushButton("Sign Up")
        buttonSign.clicked.connect(self.signUpButtonPush)
        self.layoutAuth.addWidget(buttonSign)

        self.setLayout(self.layoutAuth)

    def logInButtonPush(self):
        all_users = Database.get_all_users()
        user_correct = False
        try:
            for user in all_users:
                if self.login.newInput.text() == user['username'] and self.password.newInput.text() == user['password']:
                    user_correct = True
                    self.user = User(self.login.newInput.text(), self.password.newInput.text())
                    self.close()
            if not user_correct:
                raise ValueError
        except ValueError:
            ErrorDialog('Wrong username or password')

    @staticmethod
    def signUpButtonPush():
        sign_up = SignUpDialog()
        sign_up.show()
        sign_up.exec()
