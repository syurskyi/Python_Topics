____ ?.?G.. ______ *
____ ?.?C.. ______ *


# put to main namespase
c_ myWidget(?PB..):
    ___  - (self, text='NewButton'):
        s_(myWidget, self). - (text)

    ___ makeUI
        r_ self

    ___ updateValue
        pass


# ====================

n = ?.sN__
k = ?.PyCustom_Knob('btn', '', 'myWidget("Button")')
k = ?.PyCustom_Knob('btn', '', 'myWidget()')
n.addKnob(k)
k.setFlag(?.STARTLINE)