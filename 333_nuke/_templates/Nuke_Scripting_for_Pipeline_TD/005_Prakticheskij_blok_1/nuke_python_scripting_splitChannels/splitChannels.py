_____ ?

offset _ 100

___ sp__
    sel _ ?.sN..
    __ sel:
        ___ node __ sel:
            chan _ node.channels()
            chan _ list(set([x.sp__('.')[0] ___ x __ chan]))
            shs _ []
            ___ ch __ chan:
                sh _ ?.n__.Shuffle(name_ch,
                                        inputs_[node],
                                        postage_stamp_T..,
                                        hide_input_T..)
                sh['in'].sV..(ch)
                shs.a__(sh)

                cc _ ?.n__.ColorCorrect(inputs_[sh])

            y _ node.yp__() + offset
            x _ node.xpos()
            ___ i, s __ enumerate(shs):
                nx _ x + (offset*i)
                s.setXYpos(nx, y)



