_____ ___, __
____ ?.?C.. _____ _
____ ?.?G.. _____ _

c_ fileListClass(?LW..
    ___  -  , parent
        s__(fileListClass, self). - (parent)
        setAcceptDrops(T..)
        pathList _ []

    ___ appendImage , path
        path _ path.replace('/','\\')
        __ no.  path __ pathList:
            name _ __.path.b..(path)
            item _ ?LWI..
            item.sT..(name)
            item.sD..(32, path)
            aI..(item)
            pathList.ap..(path)

    ___ dragEnterEvent , event
        __ event.mD...hU..(
            event.a..
        ____
            event.i..

    ___ dragMoveEvent , event
        __ event.mD...hU..(
            event.a..
        ____
            event.i..

    ___ dropEvent , event
        __ event.mD...hU..(
            event.a..
            ___ url __ event.mD...u..(
                appendImage(url.tLF..())
        ____
            event.i..

    ___ keyPressEvent , event
        __ event.key __ __.Key_Delete:
            sel _ selectedIndexes
            ___ i __ reversed(sel
                __ i.data(32) in pathList:
                    pathList.r..(i.data(32))
                tI..(i.r..())

c_ resourceCompileClass(?M..
    ___  -
        s__(resourceCompileClass, self). -
        setWindowTitle('Resource Compiler')
        r..(250,300)
        w _ ?W..
        setCentralWidget(w)
        ly _ QVBoxLayout
        w.setLayout(ly)
        list _ fileListClass
        ly.addWidget(list)
        run_btn _ ?PB..('RUN')
        ly.addWidget(run_btn)
        run_btn.c___.c..(runCompile)
        __ le. __ 2:
            image _ ___.argv[1]
            list.appendImage(image)

    ___ compileQrc , qrc
        workDir _ __.path.d_n..(qrc)
        __.chdir(workDir)
        #PySide
        compiled _ __.path.j..(__.path.d_n..(qrc), 'icons_rcs.py')
        rcc _ 'C:/Python27/Lib/site-packages/PySide/pyside-rcc.exe'
        cmd _ ' '.j..([rcc, qrc, '-o', compiled])
        __.system(cmd)
        #PyQt
        compiled _ __.path.j..(__.path.d_n..(qrc), 'icons_rc.py')
        rcc _ 'C:/Python27/Lib/site-packages/PyQt4/pyrcc4.exe '
        cmd _ ' '.j..([rcc, qrc, '-o', compiled])
        __.system(cmd)
        r_ T..

    ___ runCompile
        files _ [list.item(i).data(32) ___ i in ra..(list.count())]
        qrc _ __.path.j..(__.path.d_n..(files[0]), 'resource.qrc')
        __ writeFile(qrc, files
            compileQrc(qrc)


    ___ writeFile , qrc, files
        w__ o..(qrc, 'w') __ f:
            f.w..('<RCC>\n\t<qresource>\n')
            ___ ico in files:
                f.w..('\t\t<file>%s</file>\n' % __.path.b..(ico))
            f.w..('\t</qresource>\n</RCC>')
        r_ T..

app _ ?A..
window _ resourceCompileClass
window.s..
___.e.. ?.e



    

