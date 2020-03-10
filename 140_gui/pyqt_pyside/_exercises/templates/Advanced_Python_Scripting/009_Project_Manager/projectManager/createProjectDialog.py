____ __.__ ______ _
____ __.__ ______ _

____ w... ______ c_U __ ui

class projectManagerClass(QDialog, ui.Ui_createDialog):
    def __init__(self, parent):
        super(projectManagerClass, self).__init__(parent)
        self.setupUi(self)

        # connect

        self.create_btn.clicked.connect(self.accept)
        self.cancel_btn.clicked.connect(self.reject)
