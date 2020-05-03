_____ ___

____ ?.?W.. _____ QMainWindow, ?A.., ?A__, ?FD__

____ demoMDI _____ _

c_ MyForm(QMainWindow
    ___  -
        s__. -
        ui _ Ui_MainWindow
        ?.sU..
        ?.mdiArea.addSubWindow(?.subwindow)
        ?.mdiArea.addSubWindow(?.subwindow_2)
        ?.actionSubWindow_View.t__.c..(SubWindow_View)
        ?.actionTabbed_View.t__.c..(Tabbed_View)
        ?.actionCascade_View.t__.c..(cascadeArrange)
        ?.actionTile_View.t__.c..(tileArrange)
        s..

    ___ SubWindow_View
        #self.?.mdiArea.activateNextSubWindow()
        ?.mdiArea.setViewMode(0)

    ___ Tabbed_View
        ?.mdiArea.setViewMode(1)

    ___ cascadeArrange
        ?.mdiArea.cascadeSubWindows

    ___ tileArrange
        ?.mdiArea.tileSubWindows

__ _ ____ __ _____
    app _ ?A..
    w _ ?
    w.s..
    ___.e.. ?.e

