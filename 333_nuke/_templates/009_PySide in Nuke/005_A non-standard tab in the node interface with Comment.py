# Esli mu vstavljaem widget v nodu s pompocjiy PyQt, to on ne ostavljaet nikakih sledov na samoj node
# To est'  nam ne nyzno sozdavat' knob, mu prosto sozdajom widget i vstavljaem ego v imejychijsja interfais
# Esli vu sozdajote knob  Tab to pri pereotkrutii Nuke etot knob"Tab" tak ze bydet nahoditsja na node, no esli vu delaete eto skriptom
# To esli vash skript ne zagryzen to vasha taba prosto ne bydyt pojavitsja
# Nachat' nado s polychenija widgeta okna ili nodu kak QT  objekta. Y lybogo okna, lyboj nodu on prisytstvyet i on ravnjaetsja imeni etoj nodu

____ ?.?C.. ______ _
____ ?.?G.. ______ _

___ getMainWindow():
    app = ?A...ins..)
    ___ widget __ app.tLW..
        __ widget.mO.. .cN.. __ 'Foundry::UI::DockMainWindow':
            r_ widget

qnuke = getMainWindow()
qnuke.findChildren(?W.., 'Transform1')

#####################################################################################################################################################

____ ?.?C.. ______ *
____ ?.?G.. ______ *

___ getMainWindow():
    app = ?A...ins..)
    ___ widget __ app.tLW..
        __ widget.mO.. .cN.. __ 'Foundry::UI::DockMainWindow':
            r_ widget

qnuke = getMainWindow()
w = qnuke.findChildren(?W.., 'Transform1')
w.sQT..('Transform11')


#####################################################################################################################################################

____ ?.?C.. ______ *
____ ?.?G.. ______ *

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