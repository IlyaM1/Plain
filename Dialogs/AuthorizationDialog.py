from PyQt5 import QtWidgets
from Widgets.NewRow import NewRow
from Database import Database


class AuthorizationDialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.layoutAuth = QtWidgets.QVBoxLayout()

        login = NewRow("Login")
        self.layoutAuth.addLayout(login)

        password = NewRow("Password")
        self.layoutAuth.addLayout(password)

        buttonLog = QtWidgets.QPushButton("Log In")
        # buttonLog.clicked.connect(self.logInButtonPush)
        self.layoutAuth.addWidget(buttonLog)

        buttonSign = QtWidgets.QPushButton("Sign Up")
        # buttonSign.clicked.connect(self.logInButtonPush)
        self.layoutAuth.addWidget(buttonSign)

        self.setLayout(self.layoutAuth)

    # def logInButtonPush(self):
    #     pass
    #
    # def signUpButtonPush(self):
    #     db = Database.get_instance()
    #     pass
