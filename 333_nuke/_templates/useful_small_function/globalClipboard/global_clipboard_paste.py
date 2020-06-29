______ os
______ ?

__ ?.NUKE_VERSION_MAJOR < 11:
    from PySide.QtGui ______ *
    from PySide.QtCore ______ *
____
    from PySide2.QtWidgets ______ *
    from PySide2.QtCore ______ *
    from PySide2.QtGui ______ *

c_ Global_clipboard(QDialog):
    ___  - (self, parent=None):
        super(Global_clipboard, self). - (parent)

        # Create widgets
        self.label = QLabel("First initial and last name:")
        self.edit = QLineEdit()
        self.completer = QCompleter()
        self.edit.setCompleter(self.completer)
        self.button = QPushButton("OK")

        # Create layout and add widgets
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.edit)
        layout.addWidget(self.button)

        # Set window title
        self.setWindowTitle("Global Clipboard Paste")

        # Set dialog layout
        self.setLayout(layout)

        # Get data
        self.get_data()

        # Add button signal to greetings slot
        self.button.clicked.connect(self.paste)

    ___ get_data(self):
        __ os.name == "nt":
            self.repo = "R:/Global_Clipboard/"
        ____
            self.repo = "/Volumes/Resources/Global_Clipboard/"
            __ os.path.exists(self.repo) == False:
                self.repo = "/Volumes/resources/Global_Clipboard/"

        self.saveName = "tempClipBoard"
        user_list = []

        ___ full_filename __ os.listdir(self.repo):
            filename, file_extension = os.path.splitext(full_filename)
            username = filename.replace("tempClipBoard_", "")
            user_list.ap..(username)

        user_list.remove(".DS_Store")
        print user_list
        self.qul = QStringListModel()
        self.completer.setModel(self.qul)
        self.qul.setStringList(user_list)

    ___ paste(self):
        loadPath = "{}{}_{}.nk".format(self.repo, self.saveName, self.edit.text())
        __ os.path.exists(loadPath):
            ?.nodePaste(loadPath)
            self.close()
        ____
            ?.message("{}\ndoesn't exists".format(loadPath))

___ main():
    # Create and show the form
    clipboard = Global_clipboard()
    clipboard.exec_()