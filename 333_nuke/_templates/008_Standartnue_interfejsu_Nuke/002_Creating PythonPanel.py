______ ?


c_ simplePanel ?.PP..
    ___  - 
        ?.PythonPanel. - (self, 'Simple Panel', 'pw_simplePanel')
        menu = ?.Enumeration_Knob('menu', 'Menu', ['all', 'none', 'selected'])
        addKnob(menu)
        cb = ?.Boolean_Knob('checkbox', 'CheckBox')
        cb.setFlag(?.STARTLINE)
        addKnob(cb)
        btn = ?.PyScript_Knob('btn', 'Execute')
        btn.setFlag(?.STARTLINE)
        addKnob(btn)

    ___ knobChanged(self, knob):
        __ knob is btn:
            print menu.value()


p = simplePanel()
# variant 1
p.s__
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
?.registerPanel('pw.Simple.Panel', addPanel)