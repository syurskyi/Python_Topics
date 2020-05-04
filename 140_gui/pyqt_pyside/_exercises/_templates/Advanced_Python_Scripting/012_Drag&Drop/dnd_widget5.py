_____ ___
_____ __
____ ?.?C.. _____ _
____ ?.?G.. _____ _

c_ listWidgetClass(?LW..
    ___  -  
        s__(listWidgetClass, self). -
        sWF..(__.WSOTH..)
        sDDM..(?AIV...DO..)
        sSM..(?AIV...ES..)
        files _ []                            # eto peremenaja sozdajotsja dlja izbezanija sozdanija dyblikatov

    ___ dropEvent , event
        # print 'DROP', type(event)
        mimedata _ event.mD..
        __ ?.hU..(
            ___ f __ ?.u..(
                aF..(f.tLF..())       # KOgda mu polychaem pyt' mu vuzuvaem fynkcijy addFile()

    ___ dragEnterEvent , event
        mimedata _ event.mD..
        __ ?.hU..(
            event.a..
        ____
            event.i..

    ___ dragMoveEvent , event
        mimedata _ event.mD..
        __ ?.hU..(
            event.a..
        ____
            event.i..

    ___ startDrag , dropAction
        drag _ ?D..
        mimedata _ ?MD..
        url _ []
        ___ i __ sI..(
            url.ap..(i.data(__.UR..))
        print url

    ___ aF.. , path                              # fynkcija kotoraja prinimaet pyt', pyt' mu polychaem s Drop Event
        __ no. path __ files:                        # hranitsja byfer yze dobavlennuh fajlov
            item _ ?LWI..                  # mu sozdajom novuj Item
            item.sT..(__.path.b..(path))          # otpravljaem imja fajla
            item.sD..(__.UR.., path)               # polnuj pyt' fajla polozim v kastomnujy daty etogo fajla
            files.ap..(path)

__ _____ __ ______
    app _ ?A..([])
    w _ listWidgetClass
    w.s..
    app.exec_