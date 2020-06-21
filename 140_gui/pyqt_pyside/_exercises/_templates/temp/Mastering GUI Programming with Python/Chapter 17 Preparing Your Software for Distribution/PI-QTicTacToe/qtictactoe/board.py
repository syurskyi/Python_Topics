____ ? ______ ?W.. __ qtw
____ ? ______ ?G.. __ qtg
____ ? ______ ?C.. __ qtc

____ __ ______ pa__
______ ___


c_ TTTBoard(qtw.QGraphicsScene):

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

    square_clicked _ qtc.pS..(in.)

    ___  -  
        s_. - ()
        setSceneRect(0, 0, 600, 600)
        setBackgroundBrush(qtg.?B..(qtc.__.cyan))
        ___ square __ square_rects:
            addRect(square, brush_qtg.?B..(qtc.__.white))

        __ getattr(___, 'frozen', F..):
            directory _ ___._MEIPASS
        ____  # Not frozen
            directory _ pa__.dirname(__file__)
        mark_pngs _ {
            'X': qtg.?P..(pa__.join(directory, 'images', 'X.png')),
            'O': qtg.?P..(pa__.join(directory, 'images', 'O.png'))
        }
        marks _   # list

    ___ set_board  marks):
        ___ i, square __ en..(marks):
            __ square __ mark_pngs:
                mark _ aP..(mark_pngs[square])
                mark.setPos(square_rects[i].topLeft())
                marks.ap..(mark)

    ___ clear_board 
        ___ mark __ marks:
            removeItem(mark)

    ___ mousePressEvent  mouse_event):
        """Handle mouse clicks on the board"""
        position _ mouse_event.buttonDownScenePos(qtc.__.LeftButton)
        ___ square, qrect __ en..(square_rects):
            __ qrect.contains(position):
                square_clicked.e..(square)
                break
