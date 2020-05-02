_____ ___

____ ?.?C.. _____ QUrl
____ ?.?W.. _____ ?A.., ?D..
____ ?.QtWebEngineWidgets _____ QWebEngineView

____ showGoogleMap _____ *

c_ MyForm(?D..
    ___  -  
        s__. - ()
        ui = Ui_Dialog()
        ui.setupUi
        ui.pushButtonShowMap.clicked.c..(dispSite)
        s..


    ___ dispSite 
        lng = float(ui.lineEditLongitude.text())
        lat = float(ui.lineEditLatitude.text())
        URL="https://www.google.com/maps/@"+ui.lineEditLatitude.text()+","+ui.lineEditLongitude.text()+",9z"
        ui.widget.load(QUrl(URL))
        
__ __name____"__main__":    
    app = ?A..(___.argv)
    w = MyForm()
    w.s..
    ___.e..(app.exec_())
