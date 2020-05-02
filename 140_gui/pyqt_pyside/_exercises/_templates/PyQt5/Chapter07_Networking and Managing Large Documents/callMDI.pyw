_____ ___

____ ?.?W.. _____ QMainWindow, ?A.., QAction, QFileDialog

____ demoMDI _____ *

c_ MyForm(QMainWindow
    ___  -
        s__. - ()
        ui _ Ui_MainWindow()
        ui.setupUi
        ui.mdiArea.addSubWindow(ui.subwindow)
        ui.mdiArea.addSubWindow(ui.subwindow_2)
        ui.actionSubWindow_View.triggered.c..(SubWindow_View)
        ui.actionTabbed_View.triggered.c..(Tabbed_View)
        ui.actionCascade_View.triggered.c..(cascadeArrange)
        ui.actionTile_View.triggered.c..(tileArrange)
        s..

    ___ SubWindow_View
        #self.ui.mdiArea.activateNextSubWindow()
        ui.mdiArea.setViewMode(0)

    ___ Tabbed_View
        ui.mdiArea.setViewMode(1)

    ___ cascadeArrange
        ui.mdiArea.cascadeSubWindows()

    ___ tileArrange
        ui.mdiArea.tileSubWindows()

__ _ ____ __ _____
    app _ ?A..(___.argv)
    w _ MyForm()
    w.s..
    ___.e..(app.exec_())

