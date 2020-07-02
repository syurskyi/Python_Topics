______ __
______ ?

__ ?.NUKE_VERSION_MAJOR < 11:
    ____ PySide.QtGui ______ *
    ____ PySide.QtCore ______ *
____
    ____ ?.?W.. ______ *
    ____ ?.QtCore ______ *
    ____ ?.QtGui ______ *

c_ Global_clipboard(QDialog):
    ___  - (self, parent=None):
        s_(Global_clipboard, self). - (parent)

        # Create widgets
        label = ?L..("First initial and last name:")
        edit = QLineEdit()
        completer = QCompleter()
        edit.setCompleter(completer)
        button = ?PB..("OK")

        # Create layout and add widgets
        layout = ?VB..
        layout.aW..(label)
        layout.aW..(edit)
        layout.aW..(button)

        # Set window title
        sQT..("Global Clipboard Paste")

        # Set dialog layout
        sL..(layout)

        # Get data
        get_data()

        # Add button signal to greetings slot
        button.c__.c..(paste)

    ___ get_data
        __ __.name == "nt":
            repo = "R:/Global_Clipboard/"
        ____
            repo = "/Volumes/Resources/Global_Clipboard/"
            __ __.path.exists(repo) == False:
                repo = "/Volumes/resources/Global_Clipboard/"

        saveName = "tempClipBoard"
        user_list = []

        ___ full_filename __ __.listdir(repo):
            filename, file_extension = __.path.splitext(full_filename)
            username = filename.replace("tempClipBoard_", "")
            user_list.ap..(username)

        user_list.remove(".DS_Store")
        print user_list
        qul = QStringListModel()
        completer.setModel(qul)
        qul.setStringList(user_list)

    ___ paste
        loadPath = "{}{}_{}.nk".format(repo, saveName, edit.text())
        __ __.path.exists(loadPath):
            ?.nodePaste(loadPath)
            c__
        ____
            ?.message("{}\ndoesn't exists".format(loadPath))

___ main():
    # Create and show the form
    clipboard = Global_clipboard()
    clipboard.exec_()