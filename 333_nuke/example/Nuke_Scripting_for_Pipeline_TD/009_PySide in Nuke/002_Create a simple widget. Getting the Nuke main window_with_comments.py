"""
Nyzno polychit' tekychee aktivnoe okno Nuke, dlja togo shto bu ispol'zovat' ego kak parent dlja widgeta
"""

##### Extrimely nessacery to know how to found out what classes and function has class #######

from PySide.QtCore import *
from PySide.QtGui import *

qnuke = QApplication.activeWindow()
w = QWidget()
w.show()

print qnuke
############################################################################################################
from PySide.QtCore import *
from PySide.QtGui import *

qnuke = QApplication.activeWindow()
w = QWidget(qnuke)
w.show()

"""
nichego ne proishodit. Na samom dele widget otkrulsja. No tak kak on preparencen k aktivnomy okny to on pojavilsja vnytri etogo okna.
No tak kak tam nichego nety on nahoditsja gde to vnytri etogo okna kak prozrachnuj prjamoygol'nik
"""
############################################################################################################

from PySide.QtCore import *
from PySide.QtGui import *

qnuke = QApplication.activeWindow()
w = QWidget(qnuke, Qt.Tool)
w.show()

"""
Takoj poisk parenta on ne sovsem odnoznachnuj
"""

############################################################################################################

from PySide.QtCore import *
from PySide.QtGui import *

qnuke = QApplication.activeWindow()
w = QWidget(qnuke, Qt.Tool)
w.show()

def active():
    print QApplication.activeWindow()

QTimer.singleShot(2000, active)

"""
Pochemy to ne rabotaet na rabote. Posmotret' doma.
Polychenie parenta takim obrazomsrabotaet tol'ko esli y nas Nuke aktiven. Esli Nuke ne aktiven, to parenta y nas ne bydet a znachit widget prosto ne priparentitsja
Esli okno otkruvaetsja ne pol'zovatelem cherez menjy, a skazem po kakomy to sobutijy ili cherz vremja i v etot moment Nuke bydet ne aktiven,
to mu ne polychim glavnogo okna Nuke
"""

############################################################################################################
from PySide.QtCore import *
from PySide.QtGui import *

app = QApplication.instance() # vozvrachaet tekychee aktivnoe prilozenie
# app.topLevelWidgets() # mu polychaem spisok vseh widzetov. kotorue est'  na samom verhnem yrovne

for w in app.topLevelWidgets():
    print w.windowTitle()
############################################################################################################

from PySide.QtCore import *
from PySide.QtGui import *

app = QApplication.instance() # vozvrachaet tekychee aktivnoe prilozenie
# app.topLevelWidgets() # mu polychaem spisok vseh widzetov. kotorue est'  na samom verhnem yrovne

for w in app.topLevelWidgets():
    print w.metaObject().className() # method metaObject vernjot specialnuj klass s informaciej ob objekte. Y etogo klassa est' edinstvenuj method vozvrachajychij stroky

"""
Like exersice made that print only Foundry classes
"""


############################################################################################################

"""
Kogda sozdajy novuj widget, ja pomechajy fynkcijy getNukeWindow(), kotoraja vernjot mne glavnoe okno v lybom slychae

"""

from PySide.QtCore import *
from PySide.QtGui import *

def getNukeWindow():
    app = QApplication.instance()

    for w in app.topLevelWidgets():
        if w.metaObject().className() == 'Foundry::UI::DockMainWindow'
            return w

qnuke = getNukeWindow()
qnuke.setWindowTitle('Nuke')

############################################################################################################

w = QWidget(getNukeWindow(), Qt.Tool)
w.show()
############################################################################################################

from PySide.QtCore import *
from PySide.QtGui import *

def getNukeWindow():
    app = QApplication.instance()

    for w in app.topLevelWidgets():
        if w.metaObject().className() == 'Foundry::UI::DockMainWindow':
            return w

qnuke = getNukeWindow()
qnuke.setWindowTitle('Nuke')

w = QWidget(getNukeWindow(), Qt.Tool)
w.setWindowFlags(QtCore.Qt.Window |
                      QtCore.Qt.FramelessWindowHint)
w.show()
w.close()