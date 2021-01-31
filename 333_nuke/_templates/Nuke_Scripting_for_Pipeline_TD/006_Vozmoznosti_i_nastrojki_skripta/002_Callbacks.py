_____ ?

___ my_cb
    print ?.tN.. .n..

?.addOnCreated(my_cb, nodeClass='Transform')
?.removeOnCreated(my_cb, nodeClass='Transform')

___ my_cb2
    print ?.thisKnob().gV..()

?.addKnobChanged(my_cb2)
?.removeKnobChanged(my_cb2)

___ uiUpdate
    print ?.tN.. .n..
    print ?.thisClass()
    print ?.thisView()
    print ?.thisParent().n..

?.addUpdateUI(uiUpdate)
?.removeUpdateUI(uiUpdate)

########################################################################################################################

___ myCallback2
    print ?.tN.. .n..


?.addOnCreate(myCallback2, nodeClass='Transform')
?.removeOnCreate(myCallback2, nodeClass='Transform')


___ printKnob
    print ?.thisKnob().n..


?.addKnobChanged(printKnob)
?.removeKnobChanged(printKnob)


___ uiUpdate
    print ?.tN.. .n..
    print ?.thisClass()
    print ?.thisView()
    print ?.thisParent().n..


?.addUpdateUI(uiUpdate)
?.removeUpdateUI(uiUpdate)


___ multiKnob
    n = ?.tN..
    k = ?.thisKnob()
    other = ?.selectedNodes(n.Class())
    val = k.value()
    ___ node __ other:
        __ no. node __ n:
            node[k.n..].sV..(val)


?.addKnobChanged(multiKnob)
?.removeKnobChanged(multiKnob)