
###############################################################################

# vsjo shto mu vidim v interfejse nodu eto setka

____ PySide.QtCore ______ *
____ PySide.QtGui ______ *

___ getMainWindow():
    app = QApplication.instance()
    ___ widget __ app.topLevelWidgets():
        __ widget.metaObject().className() __ 'Foundry::UI::DockMainWindow':
            r_ widget

qnuke = getMainWindow()
w = qnuke.findChild(?W.., 'Transform1')
w.sQT..('Transform11')
t = w.findChild(QTabWidget)
t.count()
nw = ?W..()
ly = ?VB..
nw.sL..(ly)
___ i __ ra..(5):
    ly.aW..(?PB..())
t.addTab(nw, 'My Tab')
c = QCalendarWidget()
t.insertTab(0, c, 'Calendar')
t.setCurrentIndex(0)

###############################################

w = qnuke.findChild(?W.., 'Transform1')
t = w.findChild(QTabWidget)
tw = t.widget(0)
gl = tw.children()[0]
gl.rowCount()
s = QSlider()
s.setOrientation(Qt.Horizontal)
gl.aW..(s, 12, 1)
lb = ?L..('SYURSKYI')
gl.aW..(lb, 12, 0, Qt.AlignRight)

###############################################

w = qnuke.findChild(?W.., 'Transform1')
t = w.findChild(QTabWidget)
tw = t.widget(0)
gl = tw.children()[0]

w2 = ?W..()
w2.sL..(gl)
ly = ?VB..
tw.sL..(ly)
btn = ?PB..('SYURSKYI')
ly.aW..(btn)
ly.aW..(w2)
