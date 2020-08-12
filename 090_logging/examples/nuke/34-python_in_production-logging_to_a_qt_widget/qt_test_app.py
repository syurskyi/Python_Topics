import sys

from PySide2 import QtWidgets

from qt_logger import QtLogger


class StandaloneWindow(QtWidgets.QWidget):

    def __init__(self):
        super(StandaloneWindow, self).__init__(parent=None)

        self.setWindowTitle("Standalone App")
        self.setMinimumSize(400, 300)

        self.plain_text_edit = QtWidgets.QPlainTextEdit()

        self.warning_btn = QtWidgets.QPushButton("Warning")
        self.warning_btn.clicked.connect(self.print_warning)

        self.error_btn = QtWidgets.QPushButton("Error")
        self.error_btn.clicked.connect(self.print_error)

        button_layout = QtWidgets.QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(self.warning_btn)
        button_layout.addWidget(self.error_btn)

        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.addWidget(self.plain_text_edit)
        main_layout.addLayout(button_layout)

        QtLogger.signal_handler().emitter.message_logged.connect(self.plain_text_edit.appendPlainText)

    def print_warning(self):
        QtLogger.warning("warning message")

    def print_error(self):
        QtLogger.error("error message")


if __name__ == "__main__":
    # Create the main Qt application
    app = QtWidgets.QApplication(sys.argv)

    window = StandaloneWindow()
    window.show()

    # Enter Qt main loop (start event handling)
    app.exec_()

