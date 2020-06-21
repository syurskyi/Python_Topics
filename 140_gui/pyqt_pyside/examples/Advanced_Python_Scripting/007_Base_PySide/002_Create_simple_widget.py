# import PySide.QtGui as QtGui

# Esli pojavljaetsja oshibka "Must construct a QApplication before a QPaintDevice
# Nado sozdat'  app = QApplication([]) pered vidzetom
# Oshibka oznachaet shto pered tem kak mu otkroem okno y nas dolzno but' inicilizirovano prilozenie QApplication
# QApplication eto klass kotoruj sozdajot prilozenie, tot process kotoruj vstraivaetsja v operacionyjy sistemy
# vstraivaetsja v ejo event loop, sledit za ispolzovaniem pamjati, procesora i drygih resyrsov, to est'
# osnovnoe prilozenie
# QPaintDevice eto dvizok kotoruj nam risyet prilozenie

# from PySide import QtGui
from PySide2.QtWidgets import *

# Esli pojavljaetsja oshibka "Must construct a QApplication before a QPaintDevice
# Nado sozdat'  app = QApplication([]) pered vidzetom


# Esli pojavljaetsja oshibka "Must construct a QApplication before a QPaintDevice
# Nado sozdat'  app = QApplication([]) pered vidzetom
# widget bez roditel'skogo vidgeta otobrazaetsja kak okno
# Vse dochernie vidzetu vnytri roditel'skogo vidzeta mogyt nahoditsja tol'ko s pomochjy layout.
# Layout eto toze prjamoygolnaja oblast', no ona ne javljaetsja vidgetom, eto algoritm raspredelenija vidgetov
# vnytri etoj prjamoygol'noj oblasti

app = QApplication([])
w = QWidget()
l = QVBoxLayout()  # sozdajotsja ekzempljar klassa QVBoxLayout
# l = QHBoxLayout()
w.setLayout(l)     # s pomochjy metoda setLayout() ispolzyj l - layout dlja postgroenija vidgetov vnytri sebja
label = QLabel('Text') # teper mu mozem shto to polozit' v etot layout
                       # Pri portirovanii C++ bibioteki na python, v PySide QString ydaljon, vmesto nejo mozno
                       # ispol'zovat' obuchnue python stroki
l.addWidget(label)     # shto bu label bul vidimum, ego nado pomesti' v layout
b = QPushButton('OK')
l.addWidget(b)

w.show()
app.exec_()

# print(dir(QApplication))


# ################# QApplication #######################################################################

# https://srinikom.github.io/pyside-docs/PySide/QtGui/QApplication.html
# https://doc.qt.io/qtforpython/PySide2/QtWidgets/QApplication.html


# ################## QPaintDevice #######################################################################

# https://doc.qt.io/qtforpython/PySide2/QtGui/QPaintDevice.html
# https://srinikom.github.io/pyside-docs/PySide/QtGui/QPaintDevice.html

# ################## QWidget #######################################################################

# https://srinikom.github.io/pyside-docs/PySide/QtGui/QWidget.html
# https://doc.qt.io/qtforpython/PySide2/QtWidgets/QWidget.html#more

# ################## QLabel #######################################################################

# https://doc.qt.io/qtforpython/PySide2/QtWidgets/QLabel.html#qlabel

# ################## QPushButton #######################################################################

# https://doc.qt.io/qt-5/qpushbutton.html
# https://doc.qt.io/qtforpython/PySide2/QtWidgets/QPushButton.html#qpushbutton
# https://doc.qt.io/qtforpython/PySide2/QtWidgets/QPushButton.html#more

