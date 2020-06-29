import os
import ?

if ?.NUKE_VERSION_MAJOR < 11:
    from PySide.QtGui import *
    from PySide.QtCore import *
else:
    from PySide2.QtWidgets import *
    from PySide2.QtCore import *
    from PySide2.QtGui import *

class Global_clipboard(QDialog):
    def __init__(self, parent=None):
        super(Global_clipboard, self).__init__(parent)

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

    def get_data(self):
        if os.name == "nt":
            self.repo = "R:/Global_Clipboard/"
        else:
            self.repo = "/Volumes/Resources/Global_Clipboard/"
            if os.path.exists(self.repo) == False:
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

    def paste(self):
        loadPath = "{}{}_{}.nk".format(self.repo, self.saveName, self.edit.text())
        if os.path.exists(loadPath):
            ?.nodePaste(loadPath)
            self.close()
        else:
            ?.message("{}\ndoesn't exists".format(loadPath))

def main():
    # Create and show the form
    clipboard = Global_clipboard()
    clipboard.exec_()