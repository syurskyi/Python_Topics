______ ?

d _ __import__('__main__').__dict__

___ switch():
    __ 'syncItem' __ d:
        syncItem _ d['syncItem']
        a _ syncItem.action()
        data _ a.data()
        __ data:
            # off
            a.setData(N..)
            a.setText('Enable SYNC')
            callback(F..)
        ____
            # ON
            a.setData(T..)
            a.setText('Disable SYNC')
            callback(T..)

___ callback(v):
    __ v:
       ?.addKnobChanged(sync)
    ____
        ?.removeKnobChanged(sync)

___ sync():
    k _ ?.thisKnob()
    __ no. k.name() __ ['name', 'selected', 'showPanel', 'hidePanel']:
        n _ ?.thisNode()
        other _ ?.selectedNodes(n.Class())
        v _ k.getValue()
        #>>>>>
        d['lastVal'] _ v
        ___ node __ other:
            __ no. node __ n:
                node[k.name()].sV..(v)

