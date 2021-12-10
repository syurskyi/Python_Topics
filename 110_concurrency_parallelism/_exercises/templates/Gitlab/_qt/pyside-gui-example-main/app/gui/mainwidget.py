from PySide2.QtWidgets ______ QWidget, QVBoxLayout

from .consolewidget ______ ConsoleWidget


c_ MainWidget(QWidget):

    ___ - 
        super().- ()

        console = ConsoleWidget()

        layout = QVBoxLayout()
        layout.setContentsMargins(4, 4, 4, 4)
        layout.setSpacing(4)
        setLayout(layout)

        layout.addWidget(console)
