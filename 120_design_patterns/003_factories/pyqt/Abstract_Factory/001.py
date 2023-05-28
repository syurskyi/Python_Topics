from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel
from PyQt5.QtGui import QIcon, QFont


class AbstractButtonFactory:
    def create_button(self, text):
        pass


class FlatButtonFactory(AbstractButtonFactory):
    def create_button(self, text):
        button = QPushButton(text)
        button.setStyleSheet("background-color: #3498db; color: #ffffff;")
        return button


class RoundedButtonFactory(AbstractButtonFactory):
    def create_button(self, text):
        button = QPushButton(text)
        button.setStyleSheet("background-color: #2ecc71; color: #ffffff; border-radius: 10px;")
        return button


class ButtonCreator:
    def __init__(self, factory):
        self.factory = factory

    def create_button(self, text):
        return self.factory.create_button(text)


class MyWidget(QWidget):
    def __init__(self, parent=None):
        super(MyWidget, self).__init__(parent)
        self.setWindowTitle("Abstract Factory Example")
        self.setGeometry(300, 300, 300, 200)

        layout = QVBoxLayout()

        label = QLabel("Choose a button style:")
        label.setFont(QFont('Arial', 16))
        layout.addWidget(label)

        flat_button_creator = ButtonCreator(FlatButtonFactory())
        flat_button = flat_button_creator.create_button("Flat Button")
        layout.addWidget(flat_button)

        rounded_button_creator = ButtonCreator(RoundedButtonFactory())
        rounded_button = rounded_button_creator.create_button("Rounded Button")
        layout.addWidget(rounded_button)

        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication([])
    widget = MyWidget()
    widget.show()
    app.exec_()
