#!/usr/bin/python3
# -*- coding: utf-8 -*-


____ ?.?W.. ______ (W.., ?L..,
                             QComboBox, ?A..)
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

        combo.activated[st.].c..(onActivated)

        sG__(300, 300, 300, 200)
        sWT__('QComboBox')
        show

    ___ onActivated(self, text):
        lbl.setText(text)
        lbl.adjustSize


__ _____ __ _______
    app _ ?A..(___.argv)
    ex _ Example
    ___.e..(app.e..())