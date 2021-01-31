_____ ?

n1 = ?.nodes.Read()
n2 = ?.nodes.Transform()
n2.setInput(0, n1)
n2.autoplace

n3 = ?.nodes.ColorCorrect()
n3.connectInput(0, n2)
n3.autoplace

n4 = ?.nodes.NoOp()

n5 = ?.nodes.Merge(inputs=[n3, n4])

n3.setInput(0, N..)

n5.inputs()

n5.input(1)

type(n5.input(1))