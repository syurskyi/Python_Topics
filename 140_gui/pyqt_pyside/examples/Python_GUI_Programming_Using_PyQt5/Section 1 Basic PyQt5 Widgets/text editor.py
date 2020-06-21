import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont

font = QFont("Times", 14)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Using Text editor")
        self.setGeometry(250, 150, 500, 500)
        self.ui()

    def ui(self):
        self.editor = QTextEdit(self)
        self.editor.move(150, 80)
        button = QPushButton("Send", self)
        self.editor.setAcceptRichText(False)
        button.move(330, 280)
        button.clicked.connect(self.get_value)

        self.show()

    def get_value(self):
        text = self.editor.toPlainText()
        print(text)


def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()