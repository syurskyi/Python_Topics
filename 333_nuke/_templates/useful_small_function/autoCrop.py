______ ?
______ nukescripts

globalFirstFrame _ st.(__.(?.r.. .knob('first_frame').value()))
globalLastFrame _ st.(__.(?.r.. .knob('last_frame').value()))


___ selectionCheck():
    selection _ ?.sN..
    ___ i __ selection:
        __ ra__(le.(selection)) __ 0:
            r_ F..
        ____
            r_ selection


___ allDependentNodesAndInputs(node, deepNumber):

    dependent _ node.dependent
    dependentInputs _ # list
    ___ d __ dependent:
        x _ 0
        w__ x <_ deepNumber:
            __ d.input(x) __ node:
                dependentInputs.ap..([d, x])
            x _ x + 1
    r_ dependentInputs


c_ autoCropPanel(nukescripts.PP..):
    p..

___ autoCrop():
    initClass _ autoCropPanel()

    __ selectionCheck() __ no. N..:
        __ initClass.sMD..:
            initClass.autoCropMainCode()
    ____
        ?.m..('Please select one or more inputs that you want to crop')
