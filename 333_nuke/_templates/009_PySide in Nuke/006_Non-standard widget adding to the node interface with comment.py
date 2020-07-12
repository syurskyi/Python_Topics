
###############################################################################

# vsjo shto mu vidim v interfejse nodu eto setka

____ ?.?C.. ______ _
____ ?.?G.. ______ _

___ getMainWindow():
    app = ?A...ins..)
    ___ widget __ app.tLW..
        __ widget.mO.. .cN.. __ 'Foundry::UI::DockMainWindow':
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
c = ?CW..
t.insertTab(0, c, 'Calendar')
t.setCurrentIndex(0)

###############################################

w = qnuke.findChild(?W.., 'Transform1')
t = w.findChild(QTabWidget)
tw = t.widget(0)
gl = tw.children()[0]
gl.rowCount()
s = QSlider()
s.setOrientation(__.Horizontal)
gl.aW..(s, 12, 1)
lb = ?L..('SYURSKYI')
gl.aW..(lb, 12, 0, __.AlignRight)

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
