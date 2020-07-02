______ ?

d = __import__('__main__').__dict__

___ switch():
    __ 'syncItem' __ d:
        syncItem = d['syncItem']
        a = syncItem.action()
        data = a.data()
        __ data:
            # off
            a.setData(None)
            a.setText('Enable SYNC')
            callback(False)
        ____
            # ON
            a.setData(True)
            a.setText('Disable SYNC')
            callback(True)

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
            __ no. node is n:
                node[k.name()].sV..(v)

