import sys
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Vertical Box Layout")
        self.setGeometry(350, 150, 400, 400)
        self.ui()

    def ui(self):
        vbox = QVBoxLayout()
        button1 = QPushButton("Save")
        button2 = QPushButton("Exit")
        button3 = QPushButton("Hello")
        vbox.addStretch()
        vbox.addWidget(button1)
        vbox.addWidget(button2)
        vbox.addWidget(button3)
        vbox.addStretch()
        self.setLayout(vbox)

        self.show()


def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

