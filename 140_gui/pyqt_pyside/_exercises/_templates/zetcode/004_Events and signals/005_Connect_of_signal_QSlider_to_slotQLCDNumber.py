______ ___
____ ?.?C.. ______ __
____ ?.?W.. ______ *


c_ Example(W..):

    ___ -
        s__ ?  .-

        ?

    ___ initUI

        lcd _ ?LCDN..(
        sld _ ?S..(__.H..,

        vbox _ ?VB..
        vbox.aW..(lcd)
        vbox.aW..(sld)

        sL..(vbox)
        sld.vC__.c..(lcd.display)

        sG__(300, 300, 250, 150)
        sWT__('Signal & slot')
        show


___ start :
    #global form
    start.form _ Example
    start.form.show

start