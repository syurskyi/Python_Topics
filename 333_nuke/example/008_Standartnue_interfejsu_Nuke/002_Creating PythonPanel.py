import nukescripts


class simplePanel(nukescripts.PythonPanel):
    def __init__(self):
        nukescripts.PythonPanel.__init__(self, 'Simple Panel', 'pw_simplePanel')
        self.menu = nuke.Enumeration_Knob('menu', 'Menu', ['all', 'none', 'selected'])
        self.addKnob(self.menu)
        self.cb = nuke.Boolean_Knob('checkbox', 'CheckBox')
        self.cb.setFlag(nuke.STARTLINE)
        self.addKnob(self.cb)
        self.btn = nuke.PyScript_Knob('btn', 'Execute')
        self.btn.setFlag(nuke.STARTLINE)
        self.addKnob(self.btn)

    def knobChanged(self, knob):
        if knob is self.btn:
            print self.menu.value()


p = simplePanel()
# variant 1
p.show()
# variant 2
p.showModal()
# variant 3
p.showModalDialog()

# add to pane
pane = nuke.getPaneFor('DAG.1')
p.addToPane(pane)


# add to menu
def addPanel():
    panel = simplePanel()
    pane = nuke.getPaneFor('DAG.1')
    return panel.addToPane(pane)


paneMenu = nuke.menu('Pane')
paneMenu.addCommand('Simple Panel', addPanel)
# or
nukescripts.registerPanel('pw.Simple.Panel', addPanel)