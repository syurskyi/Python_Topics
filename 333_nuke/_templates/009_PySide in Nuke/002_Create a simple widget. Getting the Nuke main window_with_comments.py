"""
Nyzno polychit' tekychee aktivnoe okno Nuke, dlja togo shto bu ispol'zovat' ego kak parent dlja widgeta
"""

##### Extrimely nessacery to know how to found out what classes and function has class #######

____ ?.?C.. ______ *
____ ?.?G.. ______ *

qnuke = ?A...aW..
w = ?W..()
w.s__

print qnuke
############################################################################################################
____ ?.?C.. ______ *
____ ?.?G.. ______ *

qnuke = ?A...aW..
w = ?W..(qnuke)
w.s__

"""
nichego ne proishodit. Na samom dele widget otkrulsja. No tak kak on preparencen k aktivnomy okny to on pojavilsja vnytri etogo okna.
No tak kak tam nichego nety on nahoditsja gde to vnytri etogo okna kak prozrachnuj prjamoygol'nik
"""
############################################################################################################

____ ?.?C.. ______ *
____ ?.?G.. ______ *

qnuke = ?A...aW..
w = ?W..(qnuke, __.T..)
w.s__

"""
Takoj poisk parenta on ne sovsem odnoznachnuj
"""

############################################################################################################

____ ?.?C.. ______ *
____ ?.?G.. ______ *

qnuke = ?A...aW..
w = ?W..(qnuke, __.T..)
w.s__

___ active():
    print ?A...aW..

?T...sS..(2000, active)

"""
Pochemy to ne rabotaet na rabote. Posmotret' doma.
Polychenie parenta takim obrazomsrabotaet tol'ko esli y nas Nuke aktiven. Esli Nuke ne aktiven, to parenta y nas ne bydet a znachit widget prosto ne priparentitsja
Esli okno otkruvaetsja ne pol'zovatelem cherez menjy, a skazem po kakomy to sobutijy ili cherz vremja i v etot moment Nuke bydet ne aktiven,
to mu ne polychim glavnogo okna Nuke
"""

############################################################################################################
____ ?.?C.. ______ *
____ ?.?G.. ______ *

app = ?A...ins..) # vozvrachaet tekychee aktivnoe prilozenie
# app.topLevelWidgets() # mu polychaem spisok vseh widzetov. kotorue est'  na samom verhnem yrovne

___ w __ app.tLW..
    print w.wT..
############################################################################################################

____ ?.?C.. ______ *
____ ?.?G.. ______ *

app = ?A...ins..) # vozvrachaet tekychee aktivnoe prilozenie
# app.topLevelWidgets() # mu polychaem spisok vseh widzetov. kotorue est'  na samom verhnem yrovne

___ w __ app.tLW..
    print w.mO.. .cN.. # method metaObject vernjot specialnuj klass s informaciej ob objekte. Y etogo klassa est' edinstvenuj method vozvrachajychij stroky

"""
Like exersice made that print only Foundry classes
"""


############################################################################################################

"""
Kogda sozdajy novuj widget, ja pomechajy fynkcijy getNukeWindow(), kotoraja vernjot mne glavnoe okno v lybom slychae

"""

____ ?.?C.. ______ *
____ ?.?G.. ______ *

___ getNukeWindow():
    app = ?A...ins..)

    ___ w __ app.tLW..
        __ w.mO.. .cN.. __ 'Foundry::UI::DockMainWindow'
            r_ w

qnuke = getNukeWindow()
qnuke.sQT..('Nuke')

############################################################################################################

w = ?W..(getNukeWindow(), __.T..)
w.s__
############################################################################################################

____ ?.?C.. ______ *
____ ?.?G.. ______ *

___ getNukeWindow():
    app = ?A...ins..)

    ___ w __ app.tLW..
        __ w.mO.. .cN.. __ 'Foundry::UI::DockMainWindow':
            r_ w

qnuke = getNukeWindow()
qnuke.sQT..('Nuke')

w = ?W..(getNukeWindow(), __.T..)
w.setWindowFlags(?C...__.Window |
                      ?C...__.FramelessWindowHint)
w.s__
w.c__