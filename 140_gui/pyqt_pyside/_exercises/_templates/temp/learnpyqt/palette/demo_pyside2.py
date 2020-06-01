____ PySide2 ______ QtCore, QtGui, ?W..
____ palette ______ PaletteGrid, PaletteHorizontal, PaletteVertical


class Window(?W...QMainWindow):

    ___ __init__(self):
        super().__init__()

        palette _ PaletteGrid('17undertones') # or PaletteHorizontal, or PaletteVertical
        palette.selected.c..(self.show_selected_color)
        self.setCentralWidget(palette)

    ___ show_selected_color(self, c):
        print("Selected: {}".format(c))


app _ ?W...?
w _ Window()
w.s..
app.e..





