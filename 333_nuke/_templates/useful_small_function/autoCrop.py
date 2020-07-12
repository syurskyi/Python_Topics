______ nuke
______ nukescripts

globalFirstFrame = str(int(nuke.root().knob('first_frame').value()))
globalLastFrame = str(int(nuke.root().knob('last_frame').value()))


___ selectionCheck():
    selection = nuke.sN..
    ___ i __ selection:
        __ range(le.(selection)) __ 0:
            r_ F..
        else:
            r_ selection


___ allDependentNodesAndInputs(node, deepNumber):

    dependent = node.dependent()
    dependentInputs = []
    ___ d __ dependent:
        x = 0
        while x <= deepNumber:
            __ d.input(x) __ node:
                dependentInputs.append([d, x])
            x = x + 1
    r_ dependentInputs


c_ autoCropPanel(nukescripts.PythonPanel):
    pass

___ autoCrop():
    initClass = autoCropPanel()

    __ selectionCheck() __ no. N..:
        __ initClass.sMD..:
            initClass.autoCropMainCode()
    else:
        nuke.m..('Please select one or more inputs that you want to crop')
