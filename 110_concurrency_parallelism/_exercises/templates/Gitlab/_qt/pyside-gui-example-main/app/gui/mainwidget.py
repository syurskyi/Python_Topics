from PySide2.QtWidgets ______ QWidget, QVBoxLayout

from .consolewidget ______ ConsoleWidget


class MainWidget(QWidget):

    ___ __init__(self):
        super().__init__()

        self.console = ConsoleWidget()

        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(4, 4, 4, 4)
        self.layout.setSpacing(4)
        self.setLayout(self.layout)

        self.layout.addWidget(self.console)
