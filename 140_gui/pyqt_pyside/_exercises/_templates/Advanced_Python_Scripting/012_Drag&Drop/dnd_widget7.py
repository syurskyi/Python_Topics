_____ ___
_____ os
____ PySide.?C.. _____ *
____ PySide.QtGui _____ *

icon _ os.path.join(os.path.dirname(__file__), 'drag.png')

c_ listWidgetClass(QListWidget
    ___  -  
        super(listWidgetClass, self). - ()
        setWindowFlags(Qt.WindowStaysOnTopHint)
        setDragDropMode(QAbstractItemView.DragDrop)
        setSelectionMode(QAbstractItemView.ExtendedSelection  # vjlychaet vozmoznost' vudeljat' neskol'ko fajlov
        files _ []

    ___ dropEvent , event
        # print 'DROP', type(event)
        mimedata _ event.mimeData()
        __ mimedata.hasUrls(
            for f in mimedata.urls(
                addFile(f.toLocalFile())

    ___ dragEnterEvent , event
        __ event.source() is self:
            event.ignore()
        else:
            mimedata _ event.mimeData()
            __ mimedata.hasUrls(
                event.accept()
            else:
                event.ignore()

    ___ dragMoveEvent , event
        __ event.source() is self:
            event.ignore()
        else:
            mimedata _ event.mimeData()
            __ mimedata.hasUrls(
                event.accept()
            else:
                event.ignore()

    ___ startDrag , dropAction     # pereopredeljaem method kotoruj otvechaet za to shto proishodit kogda mu nachinaem shto to peretaskivat'
                                         # dropAction odin iz rezimov peretaskivanija
        drag _ QDrag               # nyzno sozdat' klass kotoruj otvechaet za peretaskivanie dannuh i eto ne mimedata a klass QDrag. QDrag dolzen znat' komy on prenadlezit
        mimedata _ QMimeData()           # i sootvestvenno mimedata kotorue bydyt tam lezat'
        url _ []                         # potom nado sobrat' danue kotorue mu hotim pomestit' v ety mimedata a eto y nas pyti k fajlam iz vudelenuh fajlov
        for i in selectedItems(   # dlja vudelenuh elementov mu zabiraem pyt' i kladjom v url
            url.append(i.data(Qt.UserRole))
        print url
        mimedata.setUrls([QUrl.fromLocalFile(x) for x in url])  # kogda mu polychili pyti nam nado ih polozit' v mimedata. preobrazovuvaem strochky v klass QUrls
                                                                # kazduj pyt' kotoruj est' v spiske preobrazovuvaetsja v QUrl. Generator vernjot nam spisok etih klassov
        drag.setMimeData(mimedata)                              # polychennue dannue mu lozim v objekt draga, toest' v etot kontejner dlja peretaskivanija
        pix _ QPixmap(icon)
        drag.setPixmap(pix)
        r _ drag.exec_()                                        # exec_ kak iv dialogah vozvrachaet kakoj to rezyl'tat
        print r
        __ r __ Qt.DropAction.MoveAction:                       # esli y nas yspesho proizvedeno peretaskivanie to mu ydaljaem nashi vudelenue items
            deleteSelected()                               # metod deleteSelected

    ___ addFile , path
        __ not path in files:
            item _ QListWidgetItem
            item.sT..(os.path.basename(path))
            item.setData(Qt.UserRole, path)
            files.append(path)

    ___ deleteSelected 
        for s in selectedItems(                          # perebiraem vse vudelenue elementu
            files.remove(s.data(32))                       # zabirajy pyt' kotoruj lezit v data i ydaljay iz svoego byfera
            takeItem(indexFromItem(s).row())          # posle chego ydaljay sam item

__ __name__ __ '__main__':
    app _ ?A..([])
    w _ listWidgetClass()
    w.s..
    app.exec_()