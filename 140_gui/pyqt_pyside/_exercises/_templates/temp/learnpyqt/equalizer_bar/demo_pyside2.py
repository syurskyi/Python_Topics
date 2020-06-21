____ PySide2 ______ ?C.., ?W..
____ equalizer_bar ______ EqualizerBar

______ random


c_ Window(?W...?MW..):

    ___  -  
        s_. - ()

        equalizer _ EqualizerBar(5, ['#0C0786', '#40039C', '#6A00A7', '#8F0DA3', '#B02A8F', '#CA4678', '#E06461',
                                          '#F1824C', '#FCA635', '#FCCC25', '#EFF821'])
        sCW..(equalizer)

        _timer _ ?C...?T..
        _timer.sI..(100)
        _timer.timeout.c..(update_values)
        _timer.start()

    ___ update_values 
        equalizer.setValues([
            min(100, v+random.randint(0, 50) __ random.randint(0, 5) > 2 ____ v)
            ___ v __ equalizer.values()
            ])


app _ ?W...?
w _ Window()
w.s..
app.e..





