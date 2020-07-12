______ ?, ?

c_ writeManagerClass(?.PythonPanel):
    ___  -
        ?.PythonPanel. - (self, 'Write Manager', 'pw+writemanager')
        nodes _ {x.name():x ___ x __ ?.allNodes('Write')}
        ___ name, node __ nodes.items():
            line _ ?.String_Knob(name+'-file', name)
            line.sV..(node['file'].getValue())
            aK..(line)
            cb _ ?.B_K..(name+'-disable','')
            cb.clearFlag(?.ST..)
            cb.sV..(no. node['disable'].getValue())
            aK..(cb)

        start _ ?.PyScript_Knob('render','Render')
        start.sF..(?.ST..)
        aK..(start)

    ___ knobChanged(self, knob):
        node _ knob.name().split('-')[0]
        __ node __ nodes:
            node _ nodes[node]
            k _ knob.name().split('-')[1]
            __ k __ 'file':
                node['file'].sV..(knob.value())
            ____ k __ 'disable':
                node['disable'].sV..(no. knob.value())
            r_
        __ knob __ start:
            print 'RENDER'


___ s__:
    w _ writeManagerClass()
    w.s__
