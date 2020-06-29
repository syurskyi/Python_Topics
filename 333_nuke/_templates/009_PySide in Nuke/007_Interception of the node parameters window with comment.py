# Na samoj node nigde nezapisana informacija, shto nyzno dobavljat' vkladki
# Kak nam sdelat'  ak shto bu vsjo vostanavlivalos' pri otkrutii nodu
# Delaetsja eto opjat' ze s pomochjy PySide, s pomochjy sredstv etogo Framework
# v teorii vugljadit sledyjychim obrazom, vsjakij raz, kogda v Nuke otkruvaetsja novoe okno mu dolznu proverit'
# javljaetsja eto okno interfejsom nodu i esli da,  vjzat'  ego i obrabotat'  kak trebyetsja,
# to est'  dobavit' nyznue elementu interfejsa
# Dlja realizacii nam potrebyetsja specialnuj fynkcional QT framework, kotoruj nazuvaetsja eventFilter.
# v prilozenii vsegda proishodja kakie to eventu i otkrutie okna eto odin iz etih eventov

from PySide.QtCore ______ *
from PySide.QtGui ______ *

c_ eventFilterClass(QObject):
    ___ eventFilter(self, obj, ev):
        print ev.type()
        return False

f = eventFilterClass()
qnuke.installEventFilter(f)
qnuke.removeEventFilter(f)

# ne rabotaet na rabote, proverit'  doma

########################################################################################################################

from PySide.QtCore ______ *
from PySide.QtGui ______ *

c_ eventFilterClass(QObject):
    ___ eventFilter(self, obj, ev):
        __ ev.type() == QEvent.ChildPolished:
            w = ev.child()
            w.setWindowTitle('NUKE')
        return False

f = eventFilterClass()
qnuke.installEventFilter(f)
qnuke.removeEventFilter(f)