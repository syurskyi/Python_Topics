______ ?

d = __import__('__main__').__dict__

___ switch():
    __ 'syncItem' __ d:
        syncItem = d['syncItem']
        a = syncItem.action()
        data = a.data()
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
    k = ?.thisKnob()
    __ no. k.name() __ ['name', 'selected', 'showPanel', 'hidePanel']:
        n = ?.thisNode()
        other = ?.selectedNodes(n.Class())
        v = k.getValue()
        #>>>>>
        d['lastVal'] = v
        ___ node __ other:
            __ no. node __ n:
                node[k.name()].sV..(v)

