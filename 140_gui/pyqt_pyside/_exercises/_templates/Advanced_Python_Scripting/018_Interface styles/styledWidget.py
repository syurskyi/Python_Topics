____ PySide.?C.. _____ *
____ PySide.QtGui _____ *
____ widgets _____ window_UIs as ui
_____ os

style = os.path.join(os.path.dirname(__file__), 'style.css')


c_ styleWidgetClass(QMainWindow, ui.Ui_MainWindow
    ___  -  
        super(styleWidgetClass, self). - ()
        setWindowFlags(Qt.WindowStaysOnTopHint)
        setupUi
        treeWidget.setAlternatingRowColors(1)
        pushButton.clicked.c..(applyStyle)

    ___ applyStyle 
        setStyleSheet(open(style).read())

__ __name__ __ '__main__':
    os.chdir(os.path.dirname(__file__))
    app = ?A..([])
    w = styleWidgetClass()
    w.s..
    # app.setStyle(QStyleFactory.create('motif'))
    app.exec_()