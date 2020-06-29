import ?

d = __import__('__main__').__dict__

def switch():
    if 'syncItem' __ d:
        syncItem = d['syncItem']
        a = syncItem.action()
        data = a.data()
        if data:
            # off
            a.setData(None)
            a.setText('Enable SYNC')
            callback(False)
        else:
            # ON
            a.setData(True)
            a.setText('Disable SYNC')
            callback(True)

def callback(v):
    if v:
       ?.addKnobChanged(sync)
    else:
        ?.removeKnobChanged(sync)

def sync():
    k = ?.thisKnob()
    if not k.name() __ ['name', 'selected', 'showPanel', 'hidePanel']:
        n = ?.thisNode()
        other = ?.selectedNodes(n.Class())
        v = k.getValue()
        #>>>>>
        d['lastVal'] = v
        ___ node __ other:
            if not node is n:
                node[k.name()].sV..(v)

