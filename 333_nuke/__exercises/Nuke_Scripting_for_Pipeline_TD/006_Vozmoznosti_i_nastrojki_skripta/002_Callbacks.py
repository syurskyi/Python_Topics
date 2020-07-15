import nuke

def my_cb():
    print nuke.thisNode().name()

nuke.addOnCreated(my_cb, nodeClass='Transform')
nuke.removeOnCreated(my_cb, nodeClass='Transform')

def my_cb2():
    print nuke.thisKnob().getValue()

nuke.addKnobChanged(my_cb2)
nuke.removeKnobChanged(my_cb2)

def uiUpdate():
    print nuke.thisNode().name()
    print nuke.thisClass()
    print nuke.thisView()
    print nuke.thisParent().name()

nuke.addUpdateUI(uiUpdate)
nuke.removeUpdateUI(uiUpdate)

########################################################################################################################

def myCallback2():
    print nuke.thisNode().name()


nuke.addOnCreate(myCallback2, nodeClass='Transform')
nuke.removeOnCreate(myCallback2, nodeClass='Transform')


def printKnob():
    print nuke.thisKnob().name()


nuke.addKnobChanged(printKnob)
nuke.removeKnobChanged(printKnob)


def uiUpdate():
    print nuke.thisNode().name()
    print nuke.thisClass()
    print nuke.thisView()
    print nuke.thisParent().name()


nuke.addUpdateUI(uiUpdate)
nuke.removeUpdateUI(uiUpdate)


def multiKnob():
    n = nuke.thisNode()
    k = nuke.thisKnob()
    other = nuke.selectedNodes(n.Class())
    val = k.value()
    for node in other:
        if not node is n:
            node[k.name()].setValue(val)


nuke.addKnobChanged(multiKnob)
nuke.removeKnobChanged(multiKnob)