from __future__ import print_function
from PySide2 import QtGui, QtWidgets

for i in QtGui.QImageReader.supportedImageFormats():
    print(str(i).upper(), end=" ")