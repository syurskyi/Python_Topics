import sys
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Text Edit")
        self.setGeometry(50, 50, 500, 500)
        self.ui()


    def ui(self):

        self.addItem = QLineEdit(self)
        self.addItem.move(100, 50)
        self.listWidget = QListWidget(self)
        self.listWidget.move(100, 80)

        btn_add = QPushButton("Add", self)
        btn_add.move(360, 80)
        btn_add.clicked.connect(self.func_add)

        btn_delete = QPushButton("Delete", self)
        btn_delete.move(360, 110)
        btn_delete.clicked.connect(self.delete_item)

        btn_get = QPushButton("Get Item", self)
        btn_get.move(360, 140)
        btn_get.clicked.connect(self.get_item)

        btn_delete_all = QPushButton("Delete All", self)
        btn_delete_all.move(360, 170)
        btn_delete_all.clicked.connect(self.delete_all)

        list1 = ["Batman", "Superman", "Spiderman"]
        self.listWidget.addItems(list1)
        self.listWidget.addItem("Heman")
        self.show()

    def get_item(self):
        value = self.listWidget.currentItem().text()
        print(value)

    def delete_all(self):
        self.listWidget.clear()

    def delete_item(self):
        index = self.listWidget.currentRow()
        print(index)
        self.listWidget.takeItem(index)

    def func_add(self):
        val = self.addItem.text()
        self.listWidget.addItem(val)
        self.addItem.setText("")


def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
