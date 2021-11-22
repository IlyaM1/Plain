from PyQt5.QtWidgets import QListWidgetItem


class Item(QListWidgetItem):
    def __init__(self, text, note):
        super(Item, self).__init__(text)
        self.note = note
