from PyQt5 import QtGui
for i in QtGui.QImageReader.supportedImageFormats():
    print(str(i, "ascii").upper(), end=" ")


ico = window.style().standardIcon(QtWidgets.QStyle.SP_MessageBoxCritical)
window.setWindowIcon(ico)