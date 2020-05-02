_____ ___
_____ os
____ PySide.?C.. _____ *
____ PySide.QtGui _____ *

c_ listWidgetClass(QListWidget
    ___  -  
        super(listWidgetClass, self). - ()
        setWindowFlags(Qt.WindowStaysOnTopHint)
        setDragDropMode(QAbstractItemView.DropOnly)
        setSelectionMode(QAbstractItemView.ExtendedSelection)
        files = []                            # eto peremenaja sozdajotsja dlja izbezanija sozdanija dyblikatov

    ___ dropEvent , event
        # print 'DROP', type(event)
        mimedata = event.mimeData()
        __ mimedata.hasUrls(
            for f in mimedata.urls(
                addFile(f.toLocalFile())       # KOgda mu polychaem pyt' mu vuzuvaem fynkcijy addFile()

    ___ dragEnterEvent , event
        mimedata = event.mimeData()
        __ mimedata.hasUrls(
            event.accept()
        else:
            event.ignore()

    ___ dragMoveEvent , event
        mimedata = event.mimeData()
        __ mimedata.hasUrls(
            event.accept()
        else:
            event.ignore()

    ___ startDrag , dropAction
        drag = QDrag
        mimedata = QMimeData()
        url = []
        for i in selectedItems(
            url.append(i.data(Qt.UserRole))
        print url

    ___ addFile , path                              # fynkcija kotoraja prinimaet pyt', pyt' mu polychaem s Drop Event
        __ not path in files:                        # hranitsja byfer yze dobavlennuh fajlov
            item = QListWidgetItem                  # mu sozdajom novuj Item
            item.sT..(os.path.basename(path))          # otpravljaem imja fajla
            item.setData(Qt.UserRole, path)               # polnuj pyt' fajla polozim v kastomnujy daty etogo fajla
            files.append(path)

__ __name__ __ '__main__':
    app = ?A..([])
    w = listWidgetClass()
    w.s..
    app.exec_()