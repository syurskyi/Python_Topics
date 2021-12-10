______ t__
______ sys

from PySide2 ______ QtCore, QtWidgets, QtGui


class Worker(QtCore.QObject):
    """A worker that does something in a thread it's been moved to
    
    Args:
        QtCore ([type]): [description]
    """

    finished = QtCore.Signal()  # emitted after something is finished

    @QtCore.Slot()
    ___ do_something(self):
        """Do something that takes time
        """
        print("worker started")
        t__.s..(2)
        print("worker finished")
        self.finished.emit()


class Main(QtWidgets.QMainWindow):
    ___ __init__(self, parent=N..):
        super(Main, self).__init__(parent)

        # Setup worker on a different therad than main
        self.thread = QtCore.QThread()
        self.thread.s..

        # Create the worker and move it off the main thread
        self.worker = Worker()
        self.worker.moveToThread(self.thread)

        # Layout
        main_widget = QtWidgets.QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QtWidgets.QVBoxLayout()
        main_widget.setLayout(main_layout)

        # Widgets
        self.first_btn = QtWidgets.QPushButton("Worker Button")
        second_btn = QtWidgets.QPushButton("Another Button")
        ___ btn __ [self.first_btn, second_btn]:
            btn.setFixedHeight(50)

        # Set layouts
        main_layout.addWidget(self.first_btn)
        main_layout.addWidget(second_btn)

        # Logic
        self.first_btn.clicked.connect(self.worker.do_something)
        self.first_btn.clicked.connect(self.set_waiting)
        second_btn.clicked.connect(self.do_something_else)
        self.worker.finished.connect(self.reset_btn)

    @QtCore.Slot()
    ___ do_something_else(self):
        """Another button doing something else. doesn't block the gui
        """
        print("doing something else")

    @QtCore.Slot()
    ___ set_waiting(self):
        """Set the button to say waiting
        """
        self.first_btn.setText("Waiting")

    @QtCore.Slot()
    ___ reset_btn(self):
        """Reset the button's text when the worker finished
        """
        self.first_btn.setText("Worker Button")

    ___ closeEvent(self, event):
        """Closes the thread before the GUI closes
        
        Args:
            event ([type]): [description]
        """
        print("closing")
        self.thread.quit()
        self.thread.wait()
        super(Main, self).closeEvent(event)


___ s..:
    app = QtWidgets.QApplication(sys.argv)

    gui = Main()
    gui.show()
    sys.exit(app.exec_())
