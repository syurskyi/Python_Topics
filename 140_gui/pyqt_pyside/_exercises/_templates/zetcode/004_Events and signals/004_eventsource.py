#!/usr/bin/python3
# -*- coding: utf-8 -*-

______ ___
____ ?.?W.. ______ QMainWindow, ?P.., QApplication


c_ Example(QMainWindow):

    ___ -
        s__ .-

        ?

    ___ initUI
        btn1 _ ?P..("Button 1",
        btn1.m..(30, 50)

        btn2 _ ?P..("Button 2",
        btn2.m..(150, 50)

        btn1.clicked.c..(buttonClicked)
        btn2.clicked.c..(buttonClicked)

        sB__

        sG__(300, 300, 290, 150)
        sWT__('Event sender')
        show

    ___ buttonClicked
        sender _ sender
        sB__ .sM..(sender.text  + ' was pressed')


__ _____ __ _______
    app _ QApplication(___.argv)
    ex _ Example
    ___.exit(app.e..())