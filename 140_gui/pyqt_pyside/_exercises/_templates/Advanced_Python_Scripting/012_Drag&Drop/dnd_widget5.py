_____ ___
_____ os
____ ?.?C.. _____ _
____ ?.?G.. _____ _

c_ listWidgetClass(?LW..
    ___  -  
        s__(listWidgetClass, self). -
        sWF..(__.WSOTH..)
        sDDM..(QAbstractItemView.DO..)
        setSelectionMode(QAbstractItemView.ExtendedSelection)
        files _ []                            # eto peremenaja sozdajotsja dlja izbezanija sozdanija dyblikatov

    ___ dropEvent , event
        # print 'DROP', type(event)
        mimedata _ event.mimeData
        __ mimedata.hasUrls(
            ___ f __ mimedata.urls(
                addFile(f.toLocalFile())       # KOgda mu polychaem pyt' mu vuzuvaem fynkcijy addFile()

    ___ dragEnterEvent , event
        mimedata _ event.mimeData
        __ mimedata.hasUrls(
            event.a..
        ____
            event.ignore

    ___ dragMoveEvent , event
        mimedata _ event.mimeData
        __ mimedata.hasUrls(
            event.a..
        ____
            event.ignore

    ___ startDrag , dropAction
        drag _ QDrag
        mimedata _ QMimeData
        url _ []
        ___ i __ selectedItems(
            url.ap..(i.data(__.UserRole))
        print url

    ___ addFile , path                              # fynkcija kotoraja prinimaet pyt', pyt' mu polychaem s Drop Event
        __ no. path __ files:                        # hranitsja byfer yze dobavlennuh fajlov
            item _ ?LWI..                  # mu sozdajom novuj Item
            item.sT..(os.path.basename(path))          # otpravljaem imja fajla
            item.setData(__.UserRole, path)               # polnuj pyt' fajla polozim v kastomnujy daty etogo fajla
            files.ap..(path)

__ _____ __ ______
    app _ ?A..([])
    w _ listWidgetClass
    w.s..
    app.exec_