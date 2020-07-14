import nuke

n1 = nuke.nodes.Read()
n2 = nuke.nodes.Transform()
n2.setInput(0, n1)
n2.autoplace

n3 = nuke.nodes.ColorCorrect()
n3.connectInput(0, n2)
n3.autoplace

n4 = nuke.nodes.NoOp()

n5 = nuke.nodes.Merge(inputs=[n3, n4])

n3.setInput(0, None)

n5.inputs()

n5.input(1)

type(n5.input(1))