"""
Nyzno polychit' tekychee aktivnoe okno Nuke, dlja togo shto bu ispol'zovat' ego kak parent dlja widgeta
"""

##### Extrimely nessacery to know how to found out what classes and function has class #######

____ PySide.QtCore ______ *
____ PySide.QtGui ______ *

qnuke = QApplication.activeWindow()
w = ?W..()
w.s__

print qnuke
############################################################################################################
____ PySide.QtCore ______ *
____ PySide.QtGui ______ *

qnuke = QApplication.activeWindow()
w = ?W..(qnuke)
w.s__

"""
nichego ne proishodit. Na samom dele widget otkrulsja. No tak kak on preparencen k aktivnomy okny to on pojavilsja vnytri etogo okna.
No tak kak tam nichego nety on nahoditsja gde to vnytri etogo okna kak prozrachnuj prjamoygol'nik
"""
############################################################################################################

____ PySide.QtCore ______ *
____ PySide.QtGui ______ *

qnuke = QApplication.activeWindow()
w = ?W..(qnuke, Qt.Tool)
w.s__

"""
Takoj poisk parenta on ne sovsem odnoznachnuj
"""

############################################################################################################

____ PySide.QtCore ______ *
____ PySide.QtGui ______ *

qnuke = QApplication.activeWindow()
w = ?W..(qnuke, Qt.Tool)
w.s__

___ active():
    print QApplication.activeWindow()

QTimer.singleShot(2000, active)

"""
Pochemy to ne rabotaet na rabote. Posmotret' doma.
Polychenie parenta takim obrazomsrabotaet tol'ko esli y nas Nuke aktiven. Esli Nuke ne aktiven, to parenta y nas ne bydet a znachit widget prosto ne priparentitsja
Esli okno otkruvaetsja ne pol'zovatelem cherez menjy, a skazem po kakomy to sobutijy ili cherz vremja i v etot moment Nuke bydet ne aktiven,
to mu ne polychim glavnogo okna Nuke
"""

############################################################################################################
____ PySide.QtCore ______ *
____ PySide.QtGui ______ *

app = QApplication.instance() # vozvrachaet tekychee aktivnoe prilozenie
# app.topLevelWidgets() # mu polychaem spisok vseh widzetov. kotorue est'  na samom verhnem yrovne

___ w __ app.topLevelWidgets():
    print w.windowTitle()
############################################################################################################

____ PySide.QtCore ______ *
____ PySide.QtGui ______ *

app = QApplication.instance() # vozvrachaet tekychee aktivnoe prilozenie
# app.topLevelWidgets() # mu polychaem spisok vseh widzetov. kotorue est'  na samom verhnem yrovne

___ w __ app.topLevelWidgets():
    print w.metaObject().className() # method metaObject vernjot specialnuj klass s informaciej ob objekte. Y etogo klassa est' edinstvenuj method vozvrachajychij stroky

"""
Like exersice made that print only Foundry classes
"""


############################################################################################################

"""
Kogda sozdajy novuj widget, ja pomechajy fynkcijy getNukeWindow(), kotoraja vernjot mne glavnoe okno v lybom slychae

"""

____ PySide.QtCore ______ *
____ PySide.QtGui ______ *

___ getNukeWindow():
    app = QApplication.instance()

    ___ w __ app.topLevelWidgets():
        __ w.metaObject().className() __ 'Foundry::UI::DockMainWindow'
            r_ w

qnuke = getNukeWindow()
qnuke.sQT..('Nuke')

############################################################################################################

w = ?W..(getNukeWindow(), Qt.Tool)
w.s__
############################################################################################################

____ PySide.QtCore ______ *
____ PySide.QtGui ______ *

___ getNukeWindow():
    app = QApplication.instance()

    ___ w __ app.topLevelWidgets():
        __ w.metaObject().className() __ 'Foundry::UI::DockMainWindow':
            r_ w

qnuke = getNukeWindow()
qnuke.sQT..('Nuke')

w = ?W..(getNukeWindow(), Qt.Tool)
w.setWindowFlags(QtCore.Qt.Window |
                      QtCore.Qt.FramelessWindowHint)
w.s__
w.c__