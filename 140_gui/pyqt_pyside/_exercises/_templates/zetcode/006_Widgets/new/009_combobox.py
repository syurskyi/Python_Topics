#!/usr/bin/python3
# -*- coding: utf-8 -*-


____ ?.?W.. ______ (W.., ?L..,
                             QComboBox, QApplication)
______ ___


c_ Example(W..):

    ___ -
        s__ .-

        ?

    ___ initUI
        lbl _ ?L..("Ubuntu",

        combo _ QComboBox(
        combo.addItem("Ubuntu")
        combo.addItem("Mandriva")
        combo.addItem("Fedora")
        combo.addItem("Arch")
        combo.addItem("Gentoo")

        combo.m..(50, 50)
        lbl.m..(50, 150)

        combo.activated[str].connect(onActivated)

        sG__(300, 300, 300, 200)
        sWT__('QComboBox')
        show

    ___ onActivated(self, text):
        lbl.setText(text)
        lbl.adjustSize


__ _____ __ _______
    app _ QApplication(___.argv)
    ex _ Example
    ___.exit(app.e..())