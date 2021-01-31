_____ ?

offset = 100

___ split
    sel = ?.selectedNodes()
    __ sel:
        ___ node __ sel:
            chan = node.channels()
            chan = list(set([x.split('.')[0] ___ x __ chan]))
            shs = []
            ___ ch __ chan:
                sh = ?.nodes.Shuffle(name=ch,
                                        inputs=[node],
                                        postage_stamp=True,
                                        hide_input=True)
                sh['in'].sV..(ch)
                shs.a__(sh)

                cc = ?.nodes.ColorCorrect(inputs=[sh])

            y = node.yp__() + offset
            x = node.xpos()
            ___ i, s __ enumerate(shs):
                nx = x + (offset*i)
                s.setXYpos(nx, y)



