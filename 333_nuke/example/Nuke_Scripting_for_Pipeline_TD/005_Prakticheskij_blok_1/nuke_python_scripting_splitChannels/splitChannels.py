import nuke

offset = 100

def split():
    sel = nuke.selectedNodes()
    if sel:
        for node in sel:
            chan = node.channels()
            chan = list(set([x.split('.')[0] for x in chan]))
            shs = []
            for ch in chan:
                sh = nuke.nodes.Shuffle(name=ch,
                                        inputs=[node],
                                        postage_stamp=True,
                                        hide_input=True)
                sh['in'].setValue(ch)
                shs.append(sh)

                cc = nuke.nodes.ColorCorrect(inputs=[sh])

            y = node.ypos() + offset
            x = node.xpos()
            for i, s in enumerate(shs):
                nx = x + (offset*i)
                s.setXYpos(nx, y)



