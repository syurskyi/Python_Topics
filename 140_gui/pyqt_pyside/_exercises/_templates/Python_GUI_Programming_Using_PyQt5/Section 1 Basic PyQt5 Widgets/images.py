import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Using Labels")
        self.setGeometry(50, 50, 500, 500)
        self.ui()

    def ui(self):
        self.image =QLabel(self)
        self.image.setPixmap(QPixmap('images/nuke.png'))
        self.image.move(150, 50)
        remove_button = QPushButton("Remove", self)
        remove_button.move(150, 220)
        remove_button.clicked.connect(self.remove_img)
        show_button = QPushButton("Show", self)
        show_button.clicked.connect(self.show_img)
        show_button.move(260, 220)
        self.show()

    def remove_img(self):
        self.image.close()

    def show_img(self):
        self.image.show()


def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
