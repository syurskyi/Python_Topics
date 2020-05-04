____ ?.?G.. _____ _
____ ?.?C.. _____ _
_____ __
path _ __.path.d_n..(__.path.d_n..(__file__))


c_ simpleWindow(?W..
    ___  -
        s__(simpleWindow, self). -
        ly _ QHBoxLayout
        setLayout(ly)
        tree _ QTreeWidget
        ly.addWidget(tree)
        tree.header.h..
        # connect
        tree.itemChanged.c..(action)
        # start
        r..(500, 400)
        updateTree

    ___ updateTree
        tree.blockSignals(T..)
        fillTree
        tree.blockSignals(F..)

    ___ fillTree , parent_None, root_None
        __ no. parent:
            parent _ tree.invisibleRootItem
        __ no. root:
            root _ path
        ___ f __ __.listdir(root
            __ f[0] __ ['.', '_']: continue
            item _ QTreeWidgetItem
            item.sT..(0, f)
            parent.addChild(item)
            fullpath _ __.path.j..(root, f)
            __ __.path.isdir(fullpath
                fillTree(item, fullpath)
                item.setExpanded(1)
            ____
                item.setFlags(__.ItemIsEnabled | __.ItemIsSelectable | __.ItemIsEditable)
                item.sD..(0, __.UR.., {'path':__.path.normpath(fullpath)})

    ___ action , item
        print item.t..(0)
        s _ item.data(0, __.UR..)
        print s


__ _____ __ ______
    app _ ?A..
    w _ simpleWindow
    w.s..
    app.e..