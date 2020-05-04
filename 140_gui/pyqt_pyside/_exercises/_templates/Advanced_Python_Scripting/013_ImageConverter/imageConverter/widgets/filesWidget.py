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
        sSM..(?AIV...ES..)
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
            mimedata _ event.mD..
            __ ?.hU..(
                event.a..
            ____
                event.i..

    ___ dragMoveEvent , event
        __ event.source __ self:
            event.i..
        ____
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
        ?.sU..([?U__.fLF..(x) ___ x __ url])
        drag.sMD..(mimedata)
        pix _ ?P..(icon)
        drag.sP..(pix)
        r _ drag.e..
        __ r __ __.DA...MA..:
            deleteSelected

    ___ aF.. , path
        __ no. path __ files:
            item _ ?LWI..
            item.sT..(__.path.b..(path))
            item.sD..(__.UR.., path)
            files.ap..(path)

    ___ deleteSelected
        ___ s in sI..(
            files.r..(s.data(32))
            tI..(iFI..(s).r..())

    ___ mPE.. , event
        __ event.button __ __.MB__.RB..:
            p..
        ____ event.button __ __.MB__.LB..:
            sDDM..(?AIV...NDD..)
            s__(listWidgetClass, self).mPE..(event)
        ____
            sDDM..(?AIV...DD..)
            s__(listWidgetClass, self).mPE..(event)

    ___ mouseReleaseEvent , event
        sDDM..(?AIV...DD..)
        s__(listWidgetClass, self).mRE..(event)

