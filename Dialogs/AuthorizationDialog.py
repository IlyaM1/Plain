from PyQt5 import QtWidgets
from Widgets.NewRow import NewRow
from Database import Database
from Dialogs.SignUpDialog import SignUpDialog

class AuthorizationDialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()

        self.db = Database.get_instance()
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
        all_users = self.db.User.User.find()
        for user in all_users:
            if self.login.newInput.text() == user['username'] and self.password.newInput.text() == user['password']:
                print("Entered")
                print(user)
            else:
                print("Wrong Password")

    def signUpButtonPush(self):
        sign_up = SignUpDialog()
        sign_up.show()
        sign_up.exec()
