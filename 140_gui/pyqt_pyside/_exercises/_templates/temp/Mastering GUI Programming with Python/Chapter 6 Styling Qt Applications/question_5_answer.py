____ ? ______ ?W.. __ qtw
____ ? ______ ?G.. __ qtg
______ sys

app _ qtw.?A..(sys.argv)

widget _ qtw.QWidget()
palette _ widget.palette()
tile_brush _ qtg.QBrush(
    qtg.QColor('black'),
    qtg.QPixmap('tile.png')
)
palette.setBrush(qtg.QPalette.Window, tile_brush)
widget.setPalette(palette)

widget.s..
app.exec()
