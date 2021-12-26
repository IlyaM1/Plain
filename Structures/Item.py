from PyQt5.QtWidgets import QListWidgetItem
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QFont


class Item(QListWidgetItem):
    def __init__(self, text, note):
        super(Item, self).__init__(text)
        self.note = note
        self.setSizeHint(QSize(0, 25))
        self.setFont(QFont("Times", 10))
