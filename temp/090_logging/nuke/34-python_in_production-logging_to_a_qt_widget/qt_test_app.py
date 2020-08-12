______ sys

from PySide2 ______ QtWidgets

from qt_logger ______ QtLogger


class StandaloneWindow(QtWidgets.QWidget):

    ___ __init__(self):
        super(StandaloneWindow, self).__init__(parent_None)

        self.setWindowTitle("Standalone App")
        self.setMinimumSize(400, 300)

        self.plain_text_edit _ QtWidgets.QPlainTextEdit()

        self.warning_btn _ QtWidgets.QPushButton("Warning")
        self.warning_btn.clicked.connect(self.print_warning)

        self.error_btn _ QtWidgets.QPushButton("Error")
        self.error_btn.clicked.connect(self.print_error)

        button_layout _ QtWidgets.QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(self.warning_btn)
        button_layout.addWidget(self.error_btn)

        main_layout _ QtWidgets.QVBoxLayout(self)
        main_layout.addWidget(self.plain_text_edit)
        main_layout.addLayout(button_layout)

        QtLogger.signal_handler().emitter.message_logged.connect(self.plain_text_edit.appendPlainText)

    ___ print_warning(self):
        QtLogger.warning("warning m..")

    ___ print_error(self):
        QtLogger.error("error m..")


if  -n == "__main__":
    # Create the main Qt application
    app _ QtWidgets.QApplication(sys.argv)

    window _ StandaloneWindow()
    window.show()

    # Enter Qt main loop (start event handling)
    app.exec_()

