____ PySide.QtGui _____ *
____ PySide.?C.. _____ *
_____ os
path = os.path.dirname(os.path.dirname(__file__))


c_ simpleWindow(?W..
    ___  -
        super(simpleWindow, self). - ()
        ly = QHBoxLayout()
        setLayout(ly)
        tree = QTreeWidget()
        ly.addWidget(tree)
        tree.header().hide()
        # connect
        tree.itemChanged.c..(action)
        # start
        resize(500, 400)
        updateTree()

    ___ updateTree
        tree.blockSignals(T..)
        fillTree()
        tree.blockSignals(False)

    ___ fillTree , parent=None, root=None
        __ not parent:
            parent = tree.invisibleRootItem()
        __ not root:
            root = path
        for f in os.listdir(root
            __ f[0] in ['.', '_']: continue
            item = QTreeWidgetItem()
            item.sT..(0, f)
            parent.addChild(item)
            fullpath = os.path.join(root, f)
            __ os.path.isdir(fullpath
                fillTree(item, fullpath)
                item.setExpanded(1)
            else:
                item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsEditable)
                item.setData(0, Qt.UserRole, {'path':os.path.normpath(fullpath)})

    ___ action , item
        print item.text(0)
        s = item.data(0, Qt.UserRole)
        print s


__ __name__ __ '__main__':
    app = ?A..([])
    w = simpleWindow()
    w.s..
    app.exec_()