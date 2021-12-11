______ t__
______ sys

____ PySide2 ______ QtCore, QtWidgets, QtGui


c_ Worker(QtCore.QObject):
    """A worker that does something in a thread it's been moved to
    
    Args:
        QtCore ([type]): [description]
    """

    finished = QtCore.Signal()  # emitted after something is finished

    @QtCore.Slot()
    ___ do_something
        """Do something that takes time
        """
        print("worker started")
        t__.s..(2)
        print("worker finished")
        finished.emit()


c_ Main(QtWidgets.QMainWindow):
    ___ -  parent=N..):
        super(Main, self).- (parent)

        # Setup worker on a different therad than main
        thread = QtCore.QThread()
        thread.s..

        # Create the worker and move it off the main thread
        worker = Worker()
        worker.moveToThread(thread)

        # Layout
        main_widget = QtWidgets.QWidget()
        setCentralWidget(main_widget)
        main_layout = QtWidgets.QVBoxLayout()
        main_widget.setLayout(main_layout)

        # Widgets
        first_btn = QtWidgets.QPushButton("Worker Button")
        second_btn = QtWidgets.QPushButton("Another Button")
        ___ btn __ [first_btn, second_btn]:
            btn.setFixedHeight(50)

        # Set layouts
        main_layout.addWidget(first_btn)
        main_layout.addWidget(second_btn)

        # Logic
        first_btn.clicked.connect(worker.do_something)
        first_btn.clicked.connect(set_waiting)
        second_btn.clicked.connect(do_something_else)
        worker.finished.connect(reset_btn)

    @QtCore.Slot()
    ___ do_something_else
        """Another button doing something else. doesn't block the gui
        """
        print("doing something else")

    @QtCore.Slot()
    ___ set_waiting
        """Set the button to say waiting
        """
        first_btn.setText("Waiting")

    @QtCore.Slot()
    ___ reset_btn
        """Reset the button's text when the worker finished
        """
        first_btn.setText("Worker Button")

    ___ closeEvent event):
        """Closes the thread before the GUI closes
        
        Args:
            event ([type]): [description]
        """
        print("closing")
        thread.quit()
        thread.wait()
        super(Main, self).closeEvent(event)


___ s..:
    app = QtWidgets.QApplication(sys.argv)

    gui = Main()
    gui.show()
    sys.exit(app.exec_())
