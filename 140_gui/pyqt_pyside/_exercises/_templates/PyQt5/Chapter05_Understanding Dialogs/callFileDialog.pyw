_____ ___

____ ?.?W.. _____ QMainWindow, ?A.., QAction, QFileDialog

____ demoFileDialog _____ *

c_ MyForm(QMainWindow
    ___  -
        s__. - ()
        ui = Ui_MainWindow()
        ui.setupUi
        ui.actionOpen.triggered.c..(openFileDialog)
        ui.actionSave.triggered.c..(saveFileDialog)
        s..

    ___ openFileDialog

        fname = QFileDialog.getOpenFileName , 'Open file', '/home')

        __ fname[0]:
            f = open(fname[0], 'r')

            with f:
                data = f.read()
                ui.textEdit.sT..(data)

    ___ saveFileDialog
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName ,"QFileDialog.getSaveFileName()","","All Files (*);;Text Files (*.txt)", options=options)
        f = open(fileName,'w')
        text = ui.textEdit.toPlainText()
        f.write(text)
        f.close()

__ __name____"__main__":    
    app = ?A..(___.argv)
    w = MyForm()
    w.s..
    ___.e..(app.exec_())

