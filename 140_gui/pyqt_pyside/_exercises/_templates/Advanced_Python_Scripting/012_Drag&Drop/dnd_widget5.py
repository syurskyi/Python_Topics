_____ ___
_____ os
____ PySide.?C.. _____ _
____ PySide.?G.. _____ _

c_ listWidgetClass(QListWidget
    ___  -  
        super(listWidgetClass, self). - ()
        setWindowFlags(Qt.WindowStaysOnTopHint)
        setDragDropMode(QAbstractItemView.DropOnly)
        setSelectionMode(QAbstractItemView.ExtendedSelection)
        files _ []                            # eto peremenaja sozdajotsja dlja izbezanija sozdanija dyblikatov

    ___ dropEvent , event
        # print 'DROP', type(event)
        mimedata _ event.mimeData()
        __ mimedata.hasUrls(
            for f in mimedata.urls(
                addFile(f.toLocalFile())       # KOgda mu polychaem pyt' mu vuzuvaem fynkcijy addFile()

    ___ dragEnterEvent , event
        mimedata _ event.mimeData()
        __ mimedata.hasUrls(
            event.accept()
        ____
            event.ignore()

    ___ dragMoveEvent , event
        mimedata _ event.mimeData()
        __ mimedata.hasUrls(
            event.accept()
        ____
            event.ignore()

    ___ startDrag , dropAction
        drag _ QDrag
        mimedata _ QMimeData()
        url _ []
        for i in selectedItems(
            url.append(i.data(Qt.UserRole))
        print url

    ___ addFile , path                              # fynkcija kotoraja prinimaet pyt', pyt' mu polychaem s Drop Event
        __ not path in files:                        # hranitsja byfer yze dobavlennuh fajlov
            item _ QListWidgetItem                  # mu sozdajom novuj Item
            item.sT..(os.path.basename(path))          # otpravljaem imja fajla
            item.setData(Qt.UserRole, path)               # polnuj pyt' fajla polozim v kastomnujy daty etogo fajla
            files.append(path)

__ __name__ __ '__main__':
    app _ ?A..([])
    w _ listWidgetClass()
    w.s..
    app.exec_()