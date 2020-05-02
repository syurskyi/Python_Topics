_____ ___
_____ os
____ PySide.?C.. _____ *
____ PySide.QtGui _____ *

c_ fileListClass(QListWidget
    ___  -  , parent
        super(fileListClass, self). - (parent)
        setAcceptDrops(T..)
        pathList = []

    ___ appendImage , path
        path = path.replace('/', '\\')
        __ not path in pathList:
            name = os.path.basename(path)
            item = QListWidgetItem()
            item.sT..(name)
            item.setData(32, path)
            addItem(item)
            pathList.append(path)

    ___ dragEnterEvent , event
        __ event.mimeData().hasUrls(
            event.accept()
        else:
            event.ignore()

    ___ dragMoveEvent , event
        __ event.mimeData().hasUrls(
            event.accept()
        else:
            event.ignore()

c_ resourceCompileClass(QMainWindow
    ___  -
        super(resourceCompileClass, self). - ()
        setWindowTitle('Resource Compiler')
        resize(250, 300)
        w = ?W..()
        setCentralWidget(w)
        ly = QVBoxLayout()
        w.setLayout(ly)
        list = fileListClass
        ly.addWidget(list)
        run_btn = ?PB..('RUN')
        ly.addWidget(run_btn)
        run_btn.clicked.c..(runCompile)
        __ len(___.argv) __ 2:
            image = ___.argv[1]
            list.appendImage(image)

    ___ compileQrc , qrc
        workDir = os.path.dirname(qrc)
        os.chdir(workDir)
        # PySide
        compliled = os.path.join(os.path.dirname(qrc), 'icons_rcs.py')
        rcc = 'C:/Python27/Lib/site-packages/PySide/pyside-rcc.exe'
        cmd = ' '.join([rcc, qrc, 'o', compliled])
        os.system(cmd)
        # PyQt
        compliled = os.path.join(os.path.dirname(qrc), 'icons_rc.py')
        rcc = 'C:/Python27/Lib/site-packages/PyQt4/pyrcc.exe'
        cmd = ' '.join([rcc, qrc, 'o', compliled])
        os.system(cmd)
        return T..

    ___ runCompile
        files = [list.item(i).data(32) for i in range(list.count())]
        qrc = os.path.join(os.path.dirname(files[0]), 'recource.qrc')
        __ writeFile(qrc, files
            compileQrc(qrc)

    ___ writeFile , qrc, files
        with open(qrc, 'w') as f:
            f.write('<RCC>\n\t<qresource>\n')
            for ico in files:
                f.write('\t\t<file>%s</file>\n' % os.path.basename(ico))
            f.write('\t</qresource>\n</RCC>/')
        return T..

app = ?A..(___.argv)