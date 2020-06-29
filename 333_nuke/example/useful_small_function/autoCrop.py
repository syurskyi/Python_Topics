import nuke
import nukescripts

globalFirstFrame = str(int(nuke.root().knob('first_frame').value()))
globalLastFrame = str(int(nuke.root().knob('last_frame').value()))


def selectionCheck():
    selection = nuke.selectedNodes()
    for i in selection:
        if range(len(selection)) == 0:
            return False
        else:
            return selection


def allDependentNodesAndInputs(node, deepNumber):

    dependent = node.dependent()
    dependentInputs = []
    for d in dependent:
        x = 0
        while x <= deepNumber:
            if d.input(x) == node:
                dependentInputs.append([d, x])
            x = x + 1
    return dependentInputs


class autoCropPanel(nukescripts.PythonPanel):
    pass

def autoCrop():
    initClass = autoCropPanel()

    if selectionCheck() is not None:
        if initClass.showModalDialog():
            initClass.autoCropMainCode()
    else:
        nuke.message('Please select one or more inputs that you want to crop')
