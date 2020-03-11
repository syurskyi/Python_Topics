import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QTimer


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Using Timer")
        self.setGeometry(250, 150, 350, 350)
        self.ui()

    def ui(self):
        self.colorLabel = QLabel(self)
        self.colorLabel.resize(250, 250)
        self.colorLabel.setStyleSheet("background-color:green")
        self.colorLabel.move(40, 20)

        # #####################Buttons##################
        btn_start = QPushButton("Start", self)
        btn_start.move(80, 300)
        btn_start.clicked.connect(self.start)
        btn_stop = QPushButton("Stop", self)
        btn_stop.move(190, 300)
        btn_stop.clicked.connect(self.stop)

        # #################Timer########################
        self.timer = QTimer()
        self.timer.setInterval(500)
        self.timer.timeout.connect(self.change_color)
        self.value = 0

        self.show()

    def change_color(self):
        if self.value == 0:
            self.colorLabel.setStyleSheet("background-color:yellow")
            self.value = 1
        else:
            self.colorLabel.setStyleSheet("background-color:red")
            self.value = 0

    def start(self):
        self.timer.start()

    def stop(self):
        self.timer.stop()


def main():
    app = QApplication(sys.argv)
    window = Window()
    window.start()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()