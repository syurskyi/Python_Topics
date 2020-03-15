# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys

def on_current_changed(s):
    print("on_current_changed", s)

def on_directory_entered(s):
    print("on_directory_entered", s)

def on_file_selected(s):
    print("on_file_selected", s)

def on_files_selected(s):
    print("on_files_selected", s)

def on_filter_selected(s):
    print("on_filter_selected", s)

def on_clicked():
    dialog = QtGui.QFileDialog(parent=window,
                               filter="All (*);;Images (*.png *.jpg)",
                               caption="Это заголовок окна")
    dialog.setAcceptMode(QtGui.QFileDialog.AcceptOpen)
    dialog.setDirectory(QtCore.QDir.currentPath())
    dialog.setFileMode(QtGui.QFileDialog.ExistingFiles)
    dialog.setSidebarUrls([QtCore.QUrl.fromLocalFile("C:\\book"),
                           QtCore.QUrl.fromLocalFile("C:\\book\\eclipse")])
    dialog.currentChanged["const QString&"].connect(on_current_changed)
    dialog.directoryEntered["const QString&"].connect(on_directory_entered)
    dialog.fileSelected["const QString&"].connect(on_file_selected)
    dialog.filesSelected["const QStringList&"].connect(on_files_selected)
    dialog.filterSelected["const QString&"].connect(on_filter_selected)

    result = dialog.exec_()
    if result == QtGui.QDialog.Accepted:
        print(dialog.selectedFiles())
    else:
        print("Нажата кнопка Cancel")

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QFileDialog")
window.resize(300, 70)

button = QtGui.QPushButton("Отобразить диалоговое окно...")
button.clicked.connect(on_clicked)

box = QtGui.QVBoxLayout()
box.addWidget(button)
window.setLayout(box)
window.show()

sys.exit(app.exec_())