_____ ___
_____ os
____ PySide.?C.. _____ _
____ PySide.?G.. _____ _

icon _ os.path.j..(os.path.dirname(__file__), 'drag.png')

c_ listWidgetClass(QListWidget
    ___  -  
        super(listWidgetClass, self). -
        setWindowFlags(__.WindowStaysOnTopHint)
        setDragDropMode(QAbstractItemView.DragDrop)
        setSelectionMode(QAbstractItemView.ExtendedSelection  # vjlychaet vozmoznost' vudeljat' neskol'ko fajlov
        files _ []

    ___ dropEvent , event
        # print 'DROP', type(event)
        mimedata _ event.mimeData
        __ mimedata.hasUrls(
            ___ f __ mimedata.urls(
                addFile(f.toLocalFile())

    ___ dragEnterEvent , event
        __ event.source is self:
            event.ignore
        ____
            mimedata _ event.mimeData
            __ mimedata.hasUrls(
                event.accept
            ____
                event.ignore

    ___ dragMoveEvent , event
        __ event.source is self:
            event.ignore
        ____
            mimedata _ event.mimeData
            __ mimedata.hasUrls(
                event.accept
            ____
                event.ignore

    ___ startDrag , dropAction     # pereopredeljaem method kotoruj otvechaet za to shto proishodit kogda mu nachinaem shto to peretaskivat'
                                         # dropAction odin iz rezimov peretaskivanija
        drag _ QDrag               # nyzno sozdat' klass kotoruj otvechaet za peretaskivanie dannuh i eto ne mimedata a klass QDrag. QDrag dolzen znat' komy on prenadlezit
        mimedata _ QMimeData           # i sootvestvenno mimedata kotorue bydyt tam lezat'
        url _ []                         # potom nado sobrat' danue kotorue mu hotim pomestit' v ety mimedata a eto y nas pyti k fajlam iz vudelenuh fajlov
        ___ i __ selectedItems(   # dlja vudelenuh elementov mu zabiraem pyt' i kladjom v url
            url.ap..(i.data(__.UserRole))
        print url
        mimedata.setUrls([?U__.fromLocalFile(x) ___ x __ url])  # kogda mu polychili pyti nam nado ih polozit' v mimedata. preobrazovuvaem strochky v klass QUrls
                                                                # kazduj pyt' kotoruj est' v spiske preobrazovuvaetsja v QUrl. Generator vernjot nam spisok etih klassov
        drag.setMimeData(mimedata)                              # polychennue dannue mu lozim v objekt draga, toest' v etot kontejner dlja peretaskivanija
        pix _ QPixmap(icon)
        drag.setPixmap(pix)
        r _ drag.exec_                                        # exec_ kak iv dialogah vozvrachaet kakoj to rezyl'tat
        print r
        __ r __ __.DropAction.MoveAction:                       # esli y nas yspesho proizvedeno peretaskivanie to mu ydaljaem nashi vudelenue items
            deleteSelected                               # metod deleteSelected

    ___ addFile , path
        __ not path __ files:
            item _ ?LWI..
            item.sT..(os.path.basename(path))
            item.setData(__.UserRole, path)
            files.ap..(path)

    ___ deleteSelected 
        ___ s __ selectedItems(                          # perebiraem vse vudelenue elementu
            files.remove(s.data(32))                       # zabirajy pyt' kotoruj lezit v data i ydaljay iz svoego byfera
            tI..(indexFromItem(s).row())          # posle chego ydaljay sam item

__ __name__ __ '__main__':
    app _ ?A..([])
    w _ listWidgetClass
    w.s..
    app.exec_