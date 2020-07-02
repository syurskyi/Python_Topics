______ nuke
______ nukescripts

globalFirstFrame = str(int(nuke.root().knob('first_frame').value()))
globalLastFrame = str(int(nuke.root().knob('last_frame').value()))


___ selectionCheck():
    selection = nuke.selectedNodes()
    ___ i __ selection:
        __ range(len(selection)) == 0:
            return False
        else:
            return selection


___ allDependentNodesAndInputs(node, deepNumber):

    dependent = node.dependent()
    dependentInputs = []
    ___ d __ dependent:
        x = 0
        while x <= deepNumber:
            __ d.input(x) == node:
                dependentInputs.append([d, x])
            x = x + 1
    return dependentInputs


c_ autoCropPanel(nukescripts.PythonPanel):
    pass

___ autoCrop():
    initClass = autoCropPanel()

    __ selectionCheck() is no. None:
        __ initClass.showModalDialog():
            initClass.autoCropMainCode()
    else:
        nuke.message('Please select one or more inputs that you want to crop')
