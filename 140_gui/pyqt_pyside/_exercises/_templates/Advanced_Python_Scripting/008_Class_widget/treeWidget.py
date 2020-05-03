____ PySide.?G.. _____ _
____ PySide.?C.. _____ _
_____ os
path _ os.path.dirname(os.path.dirname(__file__))


c_ simpleWindow(?W..
    ___  -
        super(simpleWindow, self). - 
        ly _ QHBoxLayout
        setLayout(ly)
        tree _ QTreeWidget
        ly.addWidget(tree)
        tree.header.hide
        # connect
        tree.itemChanged.c..(action)
        # start
        resize(500, 400)
        updateTree

    ___ updateTree
        tree.blockSignals(T..)
        fillTree
        tree.blockSignals(F..)

    ___ fillTree , parent_None, root_None
        __ not parent:
            parent _ tree.invisibleRootItem
        __ not root:
            root _ path
        ___ f __ os.listdir(root
            __ f[0] __ ['.', '_']: continue
            item _ QTreeWidgetItem
            item.sT..(0, f)
            parent.addChild(item)
            fullpath _ os.path.j..(root, f)
            __ os.path.isdir(fullpath
                fillTree(item, fullpath)
                item.setExpanded(1)
            ____
                item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsEditable)
                item.setData(0, Qt.UserRole, {'path':os.path.normpath(fullpath)})

    ___ action , item
        print item.t..(0)
        s _ item.data(0, Qt.UserRole)
        print s


__ __name__ __ '__main__':
    app _ ?A..([])
    w _ simpleWindow
    w.s..
    app.exec_