import sys
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Table Widget")
        self.setGeometry(350, 150, 400, 400)
        self.ui()

    def ui(self):
        vbox = QVBoxLayout()
        self.table = QTableWidget()
        btn = QPushButton("Get")
        self.table.setRowCount(5)
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderItem(0, QTableWidgetItem("Name"))
        self.table.setHorizontalHeaderItem(1, QTableWidgetItem("Surname"))
        self.table.setHorizontalHeaderItem(2, QTableWidgetItem("Address"))
        # self.table.horizontalHeader().hide()
        # self.table.verticalHeader().hide()
        self.table.setItem(0, 0, QTableWidgetItem("First Item"))
        self.table.setItem(0, 1, QTableWidgetItem("2th Item"))
        self.table.setItem(1, 2, QTableWidgetItem("3th Item"))
        self.table.setItem(4, 2, QTableWidgetItem("4t Item"))
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.doubleClicked.connect(self.double_clicked)
        btn.clicked.connect(self.get_value)
        vbox.addWidget(self.table)
        vbox.addWidget(btn)
        self.setLayout(vbox)
        self.show()

    def get_value(self):
        for item in self.table.selectedItems():
            print(item.text(), item.row(), item.column())

    def double_clicked(self):
        for item in self.table.selectedItems():
            print(item.text(), item.row(), item.column())


def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

