____ ? ______ ?W.. as qtw
____ ? ______ QtGui as qtg
____ ? ______ QtCore as qtc

____ os ______ path
______ sys


class TTTBoard(qtw.QGraphicsScene):

    square_rects _ (
        qtc.QRectF(5, 5, 190, 190),
        qtc.QRectF(205, 5, 190, 190),
        qtc.QRectF(405, 5, 190, 190),
        qtc.QRectF(5, 205, 190, 190),
        qtc.QRectF(205, 205, 190, 190),
        qtc.QRectF(405, 205, 190, 190),
        qtc.QRectF(5, 405, 190, 190),
        qtc.QRectF(205, 405, 190, 190),
        qtc.QRectF(405, 405, 190, 190)
    )

    square_clicked _ qtc.pyqtSignal(int)

    ___ __init__(self):
        super().__init__()
        self.setSceneRect(0, 0, 600, 600)
        self.setBackgroundBrush(qtg.QBrush(qtc.Qt.cyan))
        for square in self.square_rects:
            self.addRect(square, brush_qtg.QBrush(qtc.Qt.white))

        if getattr(sys, 'frozen', False):
            directory _ sys._MEIPASS
        else:  # Not frozen
            directory _ path.dirname(__file__)
        self.mark_pngs _ {
            'X': qtg.QPixmap(path.join(directory, 'images', 'X.png')),
            'O': qtg.QPixmap(path.join(directory, 'images', 'O.png'))
        }
        self.marks _ []

    ___ set_board(self, marks):
        for i, square in enumerate(marks):
            if square in self.mark_pngs:
                mark _ self.addPixmap(self.mark_pngs[square])
                mark.setPos(self.square_rects[i].topLeft())
                self.marks.append(mark)

    ___ clear_board(self):
        for mark in self.marks:
            self.removeItem(mark)

    ___ mousePressEvent(self, mouse_event):
        """Handle mouse clicks on the board"""
        position _ mouse_event.buttonDownScenePos(qtc.Qt.LeftButton)
        for square, qrect in enumerate(self.square_rects):
            if qrect.contains(position):
                self.square_clicked.emit(square)
                break
