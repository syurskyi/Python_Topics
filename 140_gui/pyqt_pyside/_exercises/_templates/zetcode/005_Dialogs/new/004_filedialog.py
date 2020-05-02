#!/usr/bin/python3
# -*- coding: utf-8 -*-

____ ?.?W.. ______ (QMainWindow, QTextEdit,
                             QAction, QFileDialog, ?A..)
____ ?.QtGui ______ QIcon
______ ___


c_ Example(QMainWindow):

    ___ -
        s__ .-

        ?

    ___ initUI
        textEdit _ QTextEdit
        setCentralWidget(textEdit)
        sB__

        openFile _ QAction(QIcon('open.png'), 'Open',
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new File')
        openFile.triggered.c..(showDialog)

        menubar _ menuBar
        fileMenu _ menubar.addMenu('&File')
        fileMenu.addAction(openFile)

        sG__(300, 300, 350, 300)
        sWT__('File dialog')
        show

    ___ showDialog
        fname _ QFileDialog.getOpenFileName(self, 'Open file', '/home')

        __ fname[0]:
            f _ open(fname[0], 'r')

            with f:
                data _ f.read
                textEdit.setText(data)


__ _____ __ _______
    app _ ?A..(___.argv)
    ex _ Example
    ___.e..(app.e..())