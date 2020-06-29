import ?
import nukescripts
from nukescripts import panels

from PySide.QtCore import *
from PySide.QtGui import *


class simplePanel(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setLayout(QVBoxLayout())
        self.locationEdit = QCalendarWidget()
        self.layout().addWidget(self.locationEdit)

panels.registerWidgetAsPanel('simplePanel', 'Simple', "")

w = simplePanel
w.show()

# Eto chesnuj sposob vstavki widgeta vnytri Nuke
# Y etogo sposoba est'  tol'ko odno neydobstvoeto ykazanie widgeta strokoj.
# To est' ne ssulkoj na objekt a strokoj otkyda ego nyzno importit'
# Esli etot klass nahoditsja v nekotorom module na diske, to nyzno napisat'  polnostjy ego pyt', to est' ne pyt' k fajly na diske a pyt'k etomy widgety vnytri modulja
# toest' snachalo imja modulja ptom bnytri nego imja klass
# import mod
# w = mod.simplePanel()
# no pri registracii panelja eto nikak ne pomozet, ne import , ne sozdanie exampljara
# shtobu eta fynkcija nashla klass vnytri modulja, nam nyzno napisat' polnuj ego pyt' imja modylja a potom imja klassa, fynkcija sama importiryet vsjo shto nado i sozdat exampljar

# panels.registerWidgetAsPanel('mod.simplePanel', 'Simple', "")

# Vslychae esli registracija modulja nahoditsja v tom ze module , v kotorom nahoditsja klass , to mozno napisat tak

# panels.registerWidgetAsPanel(__name__.'simplePanel', 'Simple', "")
# V name obuchno pishetsja imja modlja v kotorom proishodit vupolnenie danngo koda