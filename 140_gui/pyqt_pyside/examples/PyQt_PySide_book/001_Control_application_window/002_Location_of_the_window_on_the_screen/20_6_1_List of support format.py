from __future__ import print_function
from PySide import QtGui

for i in QtGui.QImageReader.supportedImageFormats():
    print(str(i).upper(), end=" ")