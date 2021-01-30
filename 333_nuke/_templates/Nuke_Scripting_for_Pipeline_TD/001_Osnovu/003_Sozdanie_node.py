_____ ?
_____ nukescripts
# Osobennosti etogo metoda javljaetsja shto noda sozdanaja pri pomochi
# etoj fynkcii avtomaticheski konektitsa k vudelenoj node

?.createNode('Transform', 'rotate 45 scale 2', inpanel=False)

# Etot metod ne prisoedinjaet nody i ne otkruvaet panel
# knob name nado ispolzovat cherez nukescript

?.nodes.ColorCorrect()

t1 = ?.createNode('Transform', 'rotate 45 scale 2', inpanel=False)

?.nodes.Transform(rotate=45, name=nukescripts.findNextNodeName('MyTransform'), inputs=[t1])
