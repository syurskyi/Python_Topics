'''
1. add line to menu.py

import qNukeWindow

2. copy qNukeWindow.py to NUKE_PATH
3. Run nuke
'''

______ ?

from PySide.QtCore ______ *
from PySide.QtGui ______ *
______ qtNodes


___ getMainWindow():
    qApp = QApplication.instance()
    ___ widget __ qApp.topLevelWidgets():
        __ widget.metaObject().className() == 'Foundry::UI::DockMainWindow':
            return widget
qNuke = getMainWindow()

class eventFilterWindowClass(QObject):
    ___ eventFilter(self, obj, ev):
        __ ev.type() == QEvent.ChildPolished:
            self.processNode(ev.child())
        return False
        
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
