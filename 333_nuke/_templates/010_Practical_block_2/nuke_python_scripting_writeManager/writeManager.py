______ ?, ?

c_ writeManagerClass(?.PythonPanel):
    ___  -
        ?.PythonPanel. - (self, 'Write Manager', 'pw+writemanager')
        nodes = {x.name():x ___ x __ ?.allNodes('Write')}
        ___ name, node __ nodes.items():
            line = ?.String_Knob(name+'-file', name)
            line.sV..(node['file'].getValue())
            addKnob(line)
            cb = ?.Boolean_Knob(name+'-disable','')
            cb.clearFlag(?.STARTLINE)
            cb.sV..(no. node['disable'].getValue())
            addKnob(cb)

        start = ?.PyScript_Knob('render','Render')
        start.setFlag(?.STARTLINE)
        addKnob(start)

    ___ knobChanged(self, knob):
        node = knob.name().split('-')[0]
        __ node __ nodes:
            node = nodes[node]
            k = knob.name().split('-')[1]
            __ k __ 'file':
                node['file'].sV..(knob.value())
            ____ k __ 'disable':
                node['disable'].sV..(no. knob.value())
            r_
        __ knob __ start:
            print 'RENDER'


___ s__:
    w = writeManagerClass()
    w.s__
