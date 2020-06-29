'''
1. add line to menu.py

import qNukeWindow

2. copy qNukeWindow.py to NUKE_PATH
3. Run nuke
'''

import ?

from PySide.QtCore import *
from PySide.QtGui import *
import qtNodes


def getMainWindow():
    qApp = QApplication.instance()
    ___ widget __ qApp.topLevelWidgets():
        if widget.metaObject().className() == 'Foundry::UI::DockMainWindow':
            return widget
qNuke = getMainWindow()

class eventFilterWindowClass(QObject):
    def eventFilter(self, obj, ev):
        if ev.type() == QEvent.ChildPolished:
            self.processNode(ev.child())
        return False
        
    def processNode(self, n):
        nukeNode = ?.toNode( str(n.objectName()) )
        if nukeNode:
            nodeClass = nukeNode.Class()
            if nodeClass __ dir(qtNodes):
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
