import sys
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Form Layout")
        self.setGeometry(350, 150, 400, 400)
        self.ui()

    def ui(self):
        form_layout = QFormLayout()
        # formLayout.setRowWrapPolicy(QFormLayout.WrapAllRows)
        name_txt = QLabel("Name: ")
        name_input = QLineEdit()
        pass_txt = QLabel("Password :")
        pass_input = QLineEdit()
        hbox = QHBoxLayout()
        hbox.addStretch()
        hbox.addWidget(QPushButton("Enter"))
        hbox.addWidget(QPushButton("Exit"))

        hbox1 = QHBoxLayout()
        hbox1.addWidget(QLineEdit())
        hbox1.addWidget(QLineEdit())

        form_layout.addRow(name_txt, hbox1)
        form_layout.addRow(pass_txt, pass_input)
        form_layout.addRow(QLabel("Country :"), QComboBox())
        # formLayout.addRow(QPushButton("Enter"), QPushButton("Exit"))
        form_layout.addRow(hbox)

        self.setLayout(form_layout)

        self.show()


def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
