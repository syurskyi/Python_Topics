_____ ___

____ ?.?W.. _____ QMainWindow, ?A.., QAction, QFileDialog

____ demoFileDialog _____ _

c_ MyForm(QMainWindow
    ___  -
        s__. - ()
        ui _ Ui_MainWindow()
        ui.sU..
        ui.actionOpen.triggered.c..(openFileDialog)
        ui.actionSave.triggered.c..(saveFileDialog)
        s..

    ___ openFileDialog

        fname _ QFileDialog.getOpenFileName , 'Open file', '/home')

        __ fname[0]:
            f _ open(fname[0], 'r')

            with f:
                data _ f.read()
                ui.tE__.sT..(data)

    ___ saveFileDialog
        options _ QFileDialog.Options()
        options |_ QFileDialog.DontUseNativeDialog
        fileName, _ _ QFileDialog.getSaveFileName ,"QFileDialog.getSaveFileName()","","All Files (*);;Text Files (*.txt)", options_options)
        f _ open(fileName,'w')
        t.. _ ui.tE__.toPlainText()
        f.write(t..)
        f.close()

__ _ ____ __ _____
    app _ ?A..
    w _ ?
    w.s..
    ___.e..(app.e

