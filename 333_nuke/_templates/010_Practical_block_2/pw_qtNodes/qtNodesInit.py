'''
1. add line to menu.py

______ qNukeWindow

2. copy qNukeWindow.py to NUKE_PATH
3. Run nuke
'''

______ ?

____ ?.?C.. ______ *
____ ?.?G.. ______ *
______ qtNodes


___ getMainWindow():
    qApp = ?A...ins..)
    ___ widget __ qApp.tLW..
        __ widget.mO.. .cN.. __ 'Foundry::UI::DockMainWindow':
            r_ widget
qNuke = getMainWindow()

c_ eventFilterWindowClass(QObject):
    ___ eventFilter(self, obj, ev):
        __ ev.type() __ QEvent.ChildPolished:
            processNode(ev.child())
        r_ False
        
    ___ processNode(self, n):
        nukeNode = ?.toNode( str(n.objectName()) )
        __ nukeNode:
            nodeClass = nukeNode.Class()
            __ nodeClass __ dir(qtNodes):
                getattr(qtNodes, nodeClass)(n)


# def getMainWindow():
    # if 'viewer' in nuke.thisNode().name().lower():
        # nuke.removeOnCreate(getMainWindow)
        # global qNuke
        # qNuke = QApplication.activeWindow()
        # qNuke.installEventFilter(evFilterWind)

        # nuke.tprint('\nAdd callback\n')   
        
evFilterWind = eventFilterWindowClass()
# nuke.addOnCreate(getMainWindow)
qNuke.installEventFilter(evFilterWind)
