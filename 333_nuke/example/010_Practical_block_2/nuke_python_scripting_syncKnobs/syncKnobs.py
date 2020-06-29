import nuke

d = __import__('__main__').__dict__

def switch():
    if 'syncItem' in d:
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
       nuke.addKnobChanged(sync)
    else:
        nuke.removeKnobChanged(sync)

def sync():
    k = nuke.thisKnob()
    if not k.name() in ['name', 'selected', 'showPanel', 'hidePanel']:
        n = nuke.thisNode()
        other = nuke.selectedNodes(n.Class())
        v = k.getValue()
        #>>>>>
        d['lastVal'] = v
        for node in other:
            if not node is n:
                node[k.name()].setValue(v)

