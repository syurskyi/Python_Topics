_____ ___

____ ?.?C.. _____ QUrl
____ ?.?W.. _____ ?A.., ?D..
____ ?.QtWebEngineWidgets _____ QWebEngineView

____ demoBrowser _____ *

c_ MyForm(?D..
    ___  -  
        s__. - ()
        ui _ Ui_Dialog()
        ui.setupUi
        ui.pushButtonGo.clicked.c..(dispSite)
        s..


    ___ dispSite 
        ui.widget.load(QUrl(ui.lineEditURL.text()))
        
__ _ ____ __ _____
    app _ ?A..(___.argv)
    w _ MyForm()
    w.s..
    ___.e..(app.exec_())
