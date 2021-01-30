_____ ?

___ my_cb
    print ?.thisNode().name()

?.addOnCreated(my_cb, nodeClass='Transform')
?.removeOnCreated(my_cb, nodeClass='Transform')

___ my_cb2
    print ?.thisKnob().getValue()

?.addKnobChanged(my_cb2)
?.removeKnobChanged(my_cb2)

___ uiUpdate
    print ?.thisNode().name()
    print ?.thisClass()
    print ?.thisView()
    print ?.thisParent().name()

?.addUpdateUI(uiUpdate)
?.removeUpdateUI(uiUpdate)

########################################################################################################################

___ myCallback2
    print ?.thisNode().name()


?.addOnCreate(myCallback2, nodeClass='Transform')
?.removeOnCreate(myCallback2, nodeClass='Transform')


___ printKnob
    print ?.thisKnob().name()


?.addKnobChanged(printKnob)
?.removeKnobChanged(printKnob)


___ uiUpdate
    print ?.thisNode().name()
    print ?.thisClass()
    print ?.thisView()
    print ?.thisParent().name()


?.addUpdateUI(uiUpdate)
?.removeUpdateUI(uiUpdate)


___ multiKnob
    n = ?.thisNode()
    k = ?.thisKnob()
    other = ?.selectedNodes(n.Class())
    val = k.value()
    ___ node __ other:
        __ no. node is n:
            node[k.name()].setValue(val)


?.addKnobChanged(multiKnob)
?.removeKnobChanged(multiKnob)