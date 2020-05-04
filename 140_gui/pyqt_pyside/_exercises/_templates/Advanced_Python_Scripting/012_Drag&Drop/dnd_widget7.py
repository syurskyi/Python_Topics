_____ ___
_____ __
____ ?.?C.. _____ _
____ ?.?G.. _____ _

icon _ __.path.j..(__.path.d_n..(__file__), 'drag.png')

c_ listWidgetClass(?LW..
    ___  -  
        s__(listWidgetClass, self). -
        sWF..(__.WSOTH..)
        sDDM..(?AIV...DD..)
        sSM..(?AIV...ES..  # vjlychaet vozmoznost' vudeljat' neskol'ko fajlov
        files _ []

    ___ dropEvent , event
        # print 'DROP', type(event)
        mimedata _ event.mD..
        __ ?.hU..(
            ___ f __ ?.u..(
                aF..(f.tLF..())

    ___ dragEnterEvent , event
        __ event.source __ self:
            event.i..
        ____
            ? _ event.mD..
            __ ?.hU..(
                event.a..
            ____
                event.i..

    ___ dragMoveEvent , event
        __ event.source __ self:
            event.i..
        ____
            ? _ event.mD..
            __ ?.hU..(
                event.a..
            ____
                event.i..

    ___ startDrag , dropAction     # pereopredeljaem method kotoruj otvechaet za to shto proishodit kogda mu nachinaem shto to peretaskivat'
                                         # dropAction odin iz rezimov peretaskivanija
        drag _ ?D..               # nyzno sozdat' klass kotoruj otvechaet za peretaskivanie dannuh i eto ne mimedata a klass QDrag. QDrag dolzen znat' komy on prenadlezit
        mimedata _ ?MD..           # i sootvestvenno mimedata kotorue bydyt tam lezat'
        url _ []                         # potom nado sobrat' danue kotorue mu hotim pomestit' v ety mimedata a eto y nas pyti k fajlam iz vudelenuh fajlov
        ___ i __ sI..(   # dlja vudelenuh elementov mu zabiraem pyt' i kladjom v url
            url.ap..(i.data(__.UR..))
        print url
        ?.sU..([?U__.fLF..(x) ___ x __ url])  # kogda mu polychili pyti nam nado ih polozit' v mimedata. preobrazovuvaem strochky v klass QUrls
                                                                # kazduj pyt' kotoruj est' v spiske preobrazovuvaetsja v QUrl. Generator vernjot nam spisok etih klassov
        drag.sMD..(mimedata)                              # polychennue dannue mu lozim v objekt draga, toest' v etot kontejner dlja peretaskivanija
        pix _ ?P..(icon)
        drag.sP..(pix)
        r _ drag.e..                                        # exec_ kak iv dialogah vozvrachaet kakoj to rezyl'tat
        print r
        __ r __ __.DA...MA..:                       # esli y nas yspesho proizvedeno peretaskivanie to mu ydaljaem nashi vudelenue items
            deleteSelected                               # metod deleteSelected

    ___ aF.. , path
        __ no. path __ files:
            item _ ?LWI..
            item.sT..(__.path.b..(path))
            item.sD..(__.UR.., path)
            files.ap..(path)

    ___ deleteSelected 
        ___ s __ sI..(                          # perebiraem vse vudelenue elementu
            files.r..(s.data(32))                       # zabirajy pyt' kotoruj lezit v data i ydaljay iz svoego byfera
            tI..(iFI..(s).r..())          # posle chego ydaljay sam item

__ _____ __ ______
    app _ ?A..
    w _ listWidgetClass
    w.s..
    app.e..