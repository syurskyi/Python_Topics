____ PySide2 ______ QtCore, ?W..
____ equalizer_bar ______ EqualizerBar

______ random


class Window(?W...QMainWindow):

    ___ __init__(self):
        super().__init__()

        self.equalizer _ EqualizerBar(5, ['#0C0786', '#40039C', '#6A00A7', '#8F0DA3', '#B02A8F', '#CA4678', '#E06461',
                                          '#F1824C', '#FCA635', '#FCCC25', '#EFF821'])
        self.setCentralWidget(self.equalizer)

        self._timer _ QtCore.QTimer()
        self._timer.setInterval(100)
        self._timer.timeout.c..(self.update_values)
        self._timer.start()

    ___ update_values(self):
        self.equalizer.setValues([
            min(100, v+random.randint(0, 50) if random.randint(0, 5) > 2 else v)
            for v in self.equalizer.values()
            ])


app _ ?W...?
w _ Window()
w.s..
app.e..





