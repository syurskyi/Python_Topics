_____ ___

____ ?.?C.. _____ QUrl
____ ?.?W.. _____ ?A.., ?D..
____ ?.QtWebEngineWidgets _____ QWebEngineView

____ demoBrowser _____ *

c_ MyForm(?D..
    ___  -  
        s__. - ()
        ui = Ui_Dialog()
        ui.setupUi
        ui.pushButtonGo.clicked.c..(dispSite)
        s..


    ___ dispSite 
        ui.widget.load(QUrl(ui.lineEditURL.text()))
        
__ __name____"__main__":    
    app = ?A..(___.argv)
    w = MyForm()
    w.s..
    ___.e..(app.exec_())
