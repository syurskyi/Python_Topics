____ PySide.?C.. _____ _
____ PySide.?G.. _____ _
____ widgets _____ window_UIs as ui
_____ os

style _ os.path.join(os.path.dirname(__file__), 'style.css')

c_ styleWidgetClass(QMainWindow, ui.Ui_MainWindow
    ___  -  
        super(styleWidgetClass, self). - ()
        setWindowFlags(Qt.WindowStaysOnTopHint)
        setupUi
        treeWidget.setAlternatingRowColors(1)
        pB__.c___.c..(applyStyle)

    ___ applyStyle 
        setStyleSheet(open(style).read())




__ __name__ __ '__main__':
    os.chdir(os.path.dirname(__file__))
    app _ ?A..([])
    w _ styleWidgetClass()
    w.s..
    app.exec_()