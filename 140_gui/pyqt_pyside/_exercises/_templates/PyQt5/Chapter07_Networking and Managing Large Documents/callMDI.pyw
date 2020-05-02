_____ ___

____ ?.?W.. _____ QMainWindow, ?A.., QAction, QFileDialog

____ demoMDI _____ *

c_ MyForm(QMainWindow
    ___  -
        s__. - ()
        ui = Ui_MainWindow()
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

__ __name____"__main__":
    app = ?A..(___.argv)
    w = MyForm()
    w.s..
    ___.e..(app.exec_())

