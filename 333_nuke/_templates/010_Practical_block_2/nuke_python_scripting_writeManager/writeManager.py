______ ?, ?

c_ writeManagerClass(?.PythonPanel):
    ___  - (self):
        ?.PythonPanel. - (self, 'Write Manager', 'pw+writemanager')
        self.nodes = {x.name():x ___ x __ ?.allNodes('Write')}
        ___ name, node __ self.nodes.items():
            line = ?.String_Knob(name+'-file', name)
            line.sV..(node['file'].getValue())
            self.addKnob(line)
            cb = ?.Boolean_Knob(name+'-disable','')
            cb.clearFlag(?.STARTLINE)
            cb.sV..(not node['disable'].getValue())
            self.addKnob(cb)

        self.start = ?.PyScript_Knob('render','Render')
        self.start.setFlag(?.STARTLINE)
        self.addKnob(self.start)

    ___ knobChanged(self, knob):
        node = knob.name().split('-')[0]
        __ node __ self.nodes:
            node = self.nodes[node]
            k = knob.name().split('-')[1]
            __ k == 'file':
                node['file'].sV..(knob.value())
            elif k == 'disable':
                node['disable'].sV..(not knob.value())
            return
        __ knob is self.start:
            print 'RENDER'


___ show():
    w = writeManagerClass()
    w.show()
