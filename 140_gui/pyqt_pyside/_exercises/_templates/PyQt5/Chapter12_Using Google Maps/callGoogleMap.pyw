_____ ___

____ ?.?C.. _____ QUrl
____ ?.?W.. _____ ?A.., ?D..
____ ?.QtWebEngineWidgets _____ QWebEngineView

____ showGoogleMap _____ *

c_ MyForm(?D..
    ___  -  
        s__. - ()
        ui _ Ui_Dialog()
        ui.sU..
        ui.pushButtonShowMap.c___.c..(dispSite)
        s..


    ___ dispSite 
        lng _ float(ui.lineEditLongitude.t..())
        lat _ float(ui.lineEditLatitude.t..())
        URL_"https://www.google.com/maps/@"+ui.lineEditLatitude.t..()+","+ui.lineEditLongitude.t..()+",9z"
        ui.widget.load(QUrl(URL))
        
__ _ ____ __ _____
    app _ ?A..(___.argv)
    w _ ?
    w.s..
    ___.e..(app.e
