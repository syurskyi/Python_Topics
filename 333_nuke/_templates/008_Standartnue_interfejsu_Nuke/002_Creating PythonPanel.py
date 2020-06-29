______ nukescripts


class simplePanel(nukescripts.PythonPanel):
    ___ __init__(self):
        nukescripts.PythonPanel.__init__(self, 'Simple Panel', 'pw_simplePanel')
        self.menu = ?.Enumeration_Knob('menu', 'Menu', ['all', 'none', 'selected'])
        self.addKnob(self.menu)
        self.cb = ?.Boolean_Knob('checkbox', 'CheckBox')
        self.cb.setFlag(?.STARTLINE)
        self.addKnob(self.cb)
        self.btn = ?.PyScript_Knob('btn', 'Execute')
        self.btn.setFlag(?.STARTLINE)
        self.addKnob(self.btn)

    ___ knobChanged(self, knob):
        __ knob is self.btn:
            print self.menu.value()


p = simplePanel()
# variant 1
p.show()
# variant 2
p.showModal()
# variant 3
p.showModalDialog()

# add to pane
pane = ?.getPaneFor('DAG.1')
p.addToPane(pane)


# add to menu
___ addPanel():
    panel = simplePanel()
    pane = ?.getPaneFor('DAG.1')
    return panel.addToPane(pane)


paneMenu = ?.menu('Pane')
paneMenu.addCommand('Simple Panel', addPanel)
# or
nukescripts.registerPanel('pw.Simple.Panel', addPanel)