______ ___
____ ?.QtCore ______ Qt
____ ?.?W.. ______ *


c_ Example(W..):

    ___ -
        s__ ?  .-

        ?

    ___ initUI

        lcd _ QLCDNumber(
        sld _ QSlider(Qt.Horizontal,

        vbox _ ?VB..
        vbox.aW..(lcd)
        vbox.aW..(sld)

        sL..(vbox)
        sld.valueChanged.connect(lcd.display)

        sG__(300, 300, 250, 150)
        sWT__('Signal & slot')
        show


___ start :
    #global form
    start.form _ Example
    start.form.show

start