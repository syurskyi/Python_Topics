____ ? ______ ?W.. as qtw
____ ? ______ QtGui as qtg
______ sys

app _ qtw.QApplication(sys.argv)

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
