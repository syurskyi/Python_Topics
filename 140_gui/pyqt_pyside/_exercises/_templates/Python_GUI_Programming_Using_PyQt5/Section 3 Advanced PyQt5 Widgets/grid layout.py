import sys
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Grid Layout")
        self.setGeometry(350, 150, 600, 600)
        self.ui()

    def ui(self):
        self.grid_layout = QGridLayout()
        # btn1=QPushButton("Button1")
        # btn2=QPushButton("Button2")
        # btn3=QPushButton("Button3")
        # btn4=QPushButton("Button4")
        # self.gridLayout.addWidget(btn1,0,0)
        # self.gridLayout.addWidget(btn2,0,1)
        # self.gridLayout.addWidget(btn3,1,0)
        # self.gridLayout.addWidget(btn4,1,1)
        for i in range(0, 3):
            for j in range(0, 3):
                btn = QPushButton("Button{}{}".format(i, j))
                self.grid_layout.addWidget(btn, i, j)
                btn.clicked.connect(self.click_me)

        self.setLayout(self.grid_layout)
        self.show()

    def click_me(self):
        button_id = self.sender().text()
        if button_id == "Button00":
            print("Button1 was clicked")
        elif button_id == "Button01":
            print("Button2 was clicked")
        elif button_id == "Button02":
            print("Button3 was clicked")


def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

