_____ ___

____ ?.?C.. _____ QUrl
____ ?.?W.. _____ ?A.., ?D..
____ ?.QtWebEngineWidgets _____ QWebEngineView

____ showGoogleMap _____ *

c_ MyForm(?D..
    ___  -  
        s__. - ()
        ui _ Ui_Dialog()
        ui.setupUi
        ui.pushButtonShowMap.clicked.c..(dispSite)
        s..


    ___ dispSite 
        lng _ float(ui.lineEditLongitude.text())
        lat _ float(ui.lineEditLatitude.text())
        URL_"https://www.google.com/maps/@"+ui.lineEditLatitude.text()+","+ui.lineEditLongitude.text()+",9z"
        ui.widget.load(QUrl(URL))
        
__ _ ____ __ _____
    app _ ?A..(___.argv)
    w _ MyForm()
    w.s..
    ___.e..(app.exec_())
