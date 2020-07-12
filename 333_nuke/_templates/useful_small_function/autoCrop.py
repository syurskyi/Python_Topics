______ nuke
______ nukescripts

globalFirstFrame _ str(int(nuke.root().knob('first_frame').value()))
globalLastFrame _ str(int(nuke.root().knob('last_frame').value()))


___ selectionCheck():
    selection _ nuke.sN..
    ___ i __ selection:
        __ range(le.(selection)) __ 0:
            r_ F..
        else:
            r_ selection


___ allDependentNodesAndInputs(node, deepNumber):

    dependent _ node.dependent()
    dependentInputs _ []
    ___ d __ dependent:
        x _ 0
        while x <_ deepNumber:
            __ d.input(x) __ node:
                dependentInputs.append([d, x])
            x _ x + 1
    r_ dependentInputs


c_ autoCropPanel(nukescripts.PythonPanel):
    pass

___ autoCrop():
    initClass _ autoCropPanel()

    __ selectionCheck() __ no. N..:
        __ initClass.sMD..:
            initClass.autoCropMainCode()
    else:
        nuke.m..('Please select one or more inputs that you want to crop')
