# Esli mu vstavljaem widget v nodu s pompocjiy PyQt, to on ne ostavljaet nikakih sledov na samoj node
# To est'  nam ne nyzno sozdavat' knob, mu prosto sozdajom widget i vstavljaem ego v imejychijsja interfais
# Esli vu sozdajote knob  Tab to pri pereotkrutii Nuke etot knob"Tab" tak ze bydet nahoditsja na node, no esli vu delaete eto skriptom
# To esli vash skript ne zagryzen to vasha taba prosto ne bydyt pojavitsja
# Nachat' nado s polychenija widgeta okna ili nodu kak QT  objekta. Y lybogo okna, lyboj nodu on prisytstvyet i on ravnjaetsja imeni etoj nodu

____ PySide.QtCore ______ *
____ PySide.QtGui ______ *

___ getMainWindow():
    app = QApplication.instance()
    ___ widget __ app.topLevelWidgets():
        __ widget.metaObject().className() == 'Foundry::UI::DockMainWindow':
            return widget

qnuke = getMainWindow()
qnuke.findChildren(?W.., 'Transform1')

#####################################################################################################################################################

____ PySide.QtCore ______ *
____ PySide.QtGui ______ *

___ getMainWindow():
    app = QApplication.instance()
    ___ widget __ app.topLevelWidgets():
        __ widget.metaObject().className() == 'Foundry::UI::DockMainWindow':
            return widget

qnuke = getMainWindow()
w = qnuke.findChildren(?W.., 'Transform1')
w.setWindowTitle('Transform11')


#####################################################################################################################################################

____ PySide.QtCore ______ *
____ PySide.QtGui ______ *

___ getMainWindow():
    app = QApplication.instance()
    ___ widget __ app.topLevelWidgets():
        __ widget.metaObject().className() == 'Foundry::UI::DockMainWindow':
            return widget

qnuke = getMainWindow()
w = qnuke.findChild(?W.., 'Transform1')
w.setWindowTitle('Transform11')
t = w.findChild(QTabWidget)
t.count()
nw = ?W..()
ly = ?VB..
nw.sL..(ly)
___ i __ ra..(5):
    ly.aW..(QPushButton())
t.addTab(nw, 'My Tab')
c = QCalendarWidget()
t.insertTab(0, c, 'Calendar')
t.setCurrentIndex(0)