______ sys

____ PySide2 ______ QtWidgets

____ qt_logger ______ QtLogger


c_ StandaloneWindow(QtWidgets.QWidget):

    ___  -
        super(StandaloneWindow, self). - (parent_None)

        setWindowTitle("Standalone App")
        setMinimumSize(400, 300)

        plain_text_edit _ QtWidgets.QPlainTextEdit()

        warning_btn _ QtWidgets.QPushButton("Warning")
        warning_btn.clicked.connect(print_warning)

        error_btn _ QtWidgets.QPushButton("Error")
        error_btn.clicked.connect(print_error)

        button_layout _ QtWidgets.QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(warning_btn)
        button_layout.addWidget(error_btn)

        main_layout _ QtWidgets.QVBoxLayout(self)
        main_layout.addWidget(plain_text_edit)
        main_layout.addLayout(button_layout)

        QtLogger.signal_handler().emitter.message_logged.connect(plain_text_edit.appendPlainText)

    ___ print_warning
        QtLogger.w..("warning m..")

    ___ print_error
        QtLogger.e..("error m..")


__  -n __ "__main__":
    # Create the main Qt application
    app _ QtWidgets.QApplication(sys.argv)

    window _ StandaloneWindow()
    window.show()

    # Enter Qt main loop (start event handling)
    app.exec_()

