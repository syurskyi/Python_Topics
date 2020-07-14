import nuke, nukescripts

class writeManagerClass(nukescripts.PythonPanel):
    def __init__(self):
        nukescripts.PythonPanel.__init__(self, 'Write Manager', 'pw+writemanager')
        self.nodes = {x.name():x for x in nuke.allNodes('Write')}
        for name, node in self.nodes.items():
            line = nuke.String_Knob(name+'-file', name)
            line.setValue(node['file'].getValue())
            self.addKnob(line)
            cb = nuke.Boolean_Knob(name+'-disable','')
            cb.clearFlag(nuke.STARTLINE)
            cb.setValue(not node['disable'].getValue())
            self.addKnob(cb)

        self.start = nuke.PyScript_Knob('render','Render')
        self.start.setFlag(nuke.STARTLINE)
        self.addKnob(self.start)

    def knobChanged(self, knob):
        node = knob.name().split('-')[0]
        if node in self.nodes:
            node = self.nodes[node]
            k = knob.name().split('-')[1]
            if k == 'file':
                node['file'].setValue(knob.value())
            elif k == 'disable':
                node['disable'].setValue(not knob.value())
            return
        if knob is self.start:
            print 'RENDER'


def show():
    w = writeManagerClass()
    w.show()
