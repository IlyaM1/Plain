from PyQt5 import QtWidgets
from Widgets.NewRow import NewRow
from Database import Database


class SignUpDialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()

        self.db = Database.get_instance()
        self.layoutAuth = QtWidgets.QVBoxLayout()

        self.login = NewRow("Username(will be used as login)")
        self.layoutAuth.addLayout(self.login)

        self.password = NewRow("Password")
        self.layoutAuth.addLayout(self.password)

        self.repeat_password = NewRow("Repeat Password")
        self.layoutAuth.addLayout(self.repeat_password)

        buttonSign = QtWidgets.QPushButton("Sign Up")
        buttonSign.clicked.connect(self.signUpButtonPush)
        self.layoutAuth.addWidget(buttonSign)

        self.setLayout(self.layoutAuth)

    def signUpButtonPush(self):
        if self.password.newInput.text() == self.repeat_password.newInput.text():
            new_user = {
                'username': self.login.newInput.text(),
                'password': self.password.newInput.text()
            }
            new_user_id = self.db.User.User.insert_one(new_user)
            # self.db.User.createCollection(new_user['username'])
            self.db.User[new_user['username']].insert_one({'name': 'Data of creation user'})
            self.close()
