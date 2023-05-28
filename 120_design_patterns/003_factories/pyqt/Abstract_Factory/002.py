from abc import ABC, abstractmethod
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout


class GUIFactory(ABC):
    """Abstract Factory for creating GUI elements."""

    @abstractmethod
    def create_label(self, text: str) -> QLabel:
        pass

    @abstractmethod
    def create_textbox(self) -> QLineEdit:
        pass

    @abstractmethod
    def create_button(self, text: str) -> QPushButton:
        pass


class QtGUIFactory(GUIFactory):
    """Concrete Factory for creating Qt GUI elements."""

    def create_label(self, text: str) -> QLabel:
        return QLabel(text)

    def create_textbox(self) -> QLineEdit:
        return QLineEdit()

    def create_button(self, text: str) -> QPushButton:
        return QPushButton(text)


class Window(QMainWindow):
    """Client code that uses the abstract factory to create GUI elements."""

    def __init__(self, factory: GUIFactory):
        super().__init__()
        self.factory = factory
        self.init_ui()

    def init_ui(self):
        self.label = self.factory.create_label("Enter your name:")
        self.textbox = self.factory.create_textbox()
        self.button = self.factory.create_button("Submit")
        self.button.clicked.connect(self.submit)

        widget = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.textbox)
        layout.addWidget(self.button)
        widget.setLayout(layout)

        self.setCentralWidget(widget)
        self.show()

    def submit(self):
        name = self.textbox.text()
        print(f"Hello, {name}!")


if __name__ == '__main__':
    app = QApplication([])
    factory = QtGUIFactory()
    window = Window(factory)
    app.exec_()
