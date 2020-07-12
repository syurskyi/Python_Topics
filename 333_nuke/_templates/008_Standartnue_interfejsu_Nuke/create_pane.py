______ ?

c_ simplePanel(?.PythonPanel):
    ___  -
        ?.PythonPanel. - (self, 'Simple Panel', 'pw_simplePanel')
        menu _ ?.Enumeration_Knob('menu', 'Menu', ['all', 'none', 'selected'])
        aK..(menu)
        cb _ ?.B_K..('checkbox', 'CheckBox')
        cb.sF..(?.ST..)
        aK..(cb)
        btn _ ?.PyScript_Knob('btn', 'Execute')
        btn.sF..(?.ST..)
        aK..(btn)
        
    ___ knobChanged(self, knob):
        __ knob __ btn:
            print menu.v..
        
p _ simplePanel()
# variant 1
p.s__
# variant 2
p.sM..
# variant 3
p.sMD..

# add to pane
pane _ ?.getPaneFor('DAG.1')
p.addToPane(pane)

# add to menu
___ addPanel():
    panel _ simplePanel()
    pane _ ?.getPaneFor('DAG.1')
    r_ panel.addToPane(pane)

paneMenu _ ?.menu('Pane')
paneMenu.aC..('Simple Panel', addPanel)
#or
?.registerPanel('pw.Simple.Panel', addPanel)