____ ?.?G.. ______ *
____ ?.?W.. ______ *
____ ?.?C.. ______ *

____ MainWindow ______ Ui_MainWindow

______ __
______ random
______ types


BRUSH_MULT _ 3
SPRAY_PAINT_MULT _ 5
SPRAY_PAINT_N _ 100

COLORS _ [
    '#000000', '#82817f', '#820300', '#868417', '#007e03', '#037e7b', '#040079',
    '#81067a', '#7f7e45', '#05403c', '#0a7cf6', '#093c7e', '#7e07f9', '#7c4002',

    '#ffffff', '#c1c1c1', '#f70406', '#fffd00', '#08fb01', '#0bf8ee', '#0000fa',
    '#b92fc2', '#fffc91', '#00fd83', '#87f9f9', '#8481c4', '#dc137d', '#fb803c',
]

FONT_SIZES _ [7, 8, 9, 10, 11, 12, 13, 14, 18, 24, 36, 48, 64, 72, 96, 144, 288]

MODES _ [
    'selectpoly', 'selectrect',
    'eraser', 'fill',
    'dropper', 'stamp',
    'pen', 'brush',
    'spray', 'text',
    'line', 'polyline',
    'rect', 'polygon',
    'ellipse', 'roundrect'
]

CANVAS_DIMENSIONS _ 600, 400

STAMP_DIR _ './stamps'
STAMPS _ [__.pa__.join(STAMP_DIR, f) ___ f __ __.listdir(STAMP_DIR)]

SELECTION_PEN _ ?P..(QColor(0xff, 0xff, 0xff), 1, __.DashLine)
PREVIEW_PEN _ ?P..(QColor(0xff, 0xff, 0xff), 1, __.SolidLine)


___ build_font(c..):
    """
    Construct a complete font from the configuration options
    :param self:
    :param config:
    :return: QFont
    """
    font _ c..['font']
    font.sPS..(c..['fontsize'])
    font.setBold(c..['bold'])
    font.setItalic(c..['italic'])
    font.setUnderline(c..['underline'])
    r_ font


c_ Canvas(?L..):

    mode _ 'rectangle'

    primary_color _ QColor(__.black)
    secondary_color _ None

    primary_color_updated _ pS.. st.
    secondary_color_updated _ pS.. st.

    # Store configuration settings, including pen width, fonts etc.
    c.. _ {
        # Drawing options.
        'size': 1,
        'fill': T..,
        # Font options.
        'font': ?F..('Times'),
        'fontsize': 12,
        'bold': F..,
        'italic': F..,
        'underline': F..,
    }

    active_color _ None
    preview_pen _ None

    timer_event _ None

    current_stamp _ None

    ___ initialize
        background_color _ QColor(secondary_color) __ secondary_color ____ QColor(__.white)
        eraser_color _ QColor(secondary_color) __ secondary_color ____ QColor(__.white)
        eraser_color.setAlpha(100)
        reset()

    ___ reset
        # Create the pixmap for display.
        sP..(?P..(*CANVAS_DIMENSIONS))

        # Clear the canvas.
        pixmap().fill(background_color)

    ___ set_primary_color  hex):
        primary_color _ QColor(hex)

    ___ set_secondary_color  hex):
        secondary_color _ QColor(hex)

    ___ set_config  key, value):
        c..[key] _ value

    ___ set_mode  mode):
        # Clean up active timer animations.
        timer_cleanup()
        # Reset mode-specific vars (all)
        active_shape_fn _ None
        active_shape_args _ ()

        origin_pos _ None

        current_pos _ None
        last_pos _ None

        history_pos _ None
        last_history _   # list

        current_text _ ""
        last_text _ ""

        last_config _   # dict

        dash_offset _ 0
        locked _ F..
        # Apply the mode
        mode _ mode

    ___ reset_mode
        set_mode(mode)

    ___ on_timer
        __ timer_event:
            timer_event()

    ___ timer_cleanup
        __ timer_event:
            # Stop the timer, then trigger cleanup.
            timer_event _ timer_event
            timer_event _ None
            timer_event(final_ st.

    # Mouse events.

    ___ mousePressEvent  e):
        fn _ getattr  "%s_mousePressEvent" % mode, None)
        __ fn:
            r_ fn(e)

    ___ mouseMoveEvent  e):
        fn _ getattr  "%s_mouseMoveEvent" % mode, None)
        __ fn:
            r_ fn(e)

    ___ mouseReleaseEvent  e):
        fn _ getattr  "%s_mouseReleaseEvent" % mode, None)
        __ fn:
            r_ fn(e)

    ___ mouseDoubleClickEvent  e):
        fn _ getattr  "%s_mouseDoubleClickEvent" % mode, None)
        __ fn:
            r_ fn(e)

    # Generic events (shared by brush-like tools)

    ___ generic_mousePressEvent  e):
        last_pos _ e.pos()

        __ e.button() __ __.LeftButton:
            active_color _ primary_color
        ____:
            active_color _ secondary_color

    ___ generic_mouseReleaseEvent  e):
        last_pos _ None

    # Mode-specific events.

    # Select polygon events

    ___ selectpoly_mousePressEvent  e):
        __ not locked or e.button __ __.RightButton:
            active_shape_fn _ 'drawPolygon'
            preview_pen _ SELECTION_PEN
            generic_poly_mousePressEvent(e)

    ___ selectpoly_timerEvent  final_F..):
        generic_poly_timerEvent(final)

    ___ selectpoly_mouseMoveEvent  e):
        __ not locked:
            generic_poly_mouseMoveEvent(e)

    ___ selectpoly_mouseDoubleClickEvent  e):
        current_pos _ e.pos()
        locked _ T..

    ___ selectpoly_copy
        """
        Copy a polygon region from the current image, returning it.

        Create a mask for the selected area, and use it to blank
        out non-selected regions. Then get the bounding rect of the
        selection and crop to produce the smallest possible image.

        :return: QPixmap of the copied region.
        """
        timer_cleanup()

        pixmap _ pixmap().copy()
        bitmap _ QBitmap(*CANVAS_DIMENSIONS)
        bitmap.c..  # Starts with random data visible.

        p _ QPainter(bitmap)
        # Construct a mask where the user selected area will be kept, the rest removed from the image is transparent.
        userpoly _ QPolygon(history_pos + [current_pos])
        p.sP..(?P..(__.color1))
        p.sB..(?B..(__.color1))  # Solid color, Qt.color1 == bit on.
        p.drawPolygon(userpoly)
        p.end()

        # Set our created mask on the image.
        pixmap.setMask(bitmap)

        # Calculate the bounding rect and return a copy of that region.
        r_ pixmap.copy(userpoly.boundingRect())

    # Select rectangle events

    ___ selectrect_mousePressEvent  e):
        active_shape_fn _ 'drawRect'
        preview_pen _ SELECTION_PEN
        generic_shape_mousePressEvent(e)

    ___ selectrect_timerEvent  final_F..):
        generic_shape_timerEvent(final)

    ___ selectrect_mouseMoveEvent  e):
        __ not locked:
            current_pos _ e.pos()

    ___ selectrect_mouseReleaseEvent  e):
        current_pos _ e.pos()
        locked _ T..

    ___ selectrect_copy
        """
        Copy a rectangle region of the current image, returning it.

        :return: QPixmap of the copied region.
        """
        timer_cleanup()
        r_ pixmap().copy(QRect(origin_pos, current_pos))

    # Eraser events

    ___ eraser_mousePressEvent  e):
        generic_mousePressEvent(e)

    ___ eraser_mouseMoveEvent  e):
        __ last_pos:
            p _ QPainter(pixmap())
            p.sP..(?P..(eraser_color, 30, __.SolidLine, __.RoundCap, __.RoundJoin))
            p.drawLine(last_pos, e.pos())

            last_pos _ e.pos()
            update()

    ___ eraser_mouseReleaseEvent  e):
        generic_mouseReleaseEvent(e)

    # Stamp (pie) events

    ___ stamp_mousePressEvent  e):
        p _ QPainter(pixmap())
        stamp _ current_stamp
        p.drawPixmap(e.x() - stamp.width() // 2, e.y() - stamp.height() // 2, stamp)
        update()

    # Pen events

    ___ pen_mousePressEvent  e):
        generic_mousePressEvent(e)

    ___ pen_mouseMoveEvent  e):
        __ last_pos:
            p _ QPainter(pixmap())
            p.sP..(?P..(active_color, c..['size'], __.SolidLine, __.SquareCap, __.RoundJoin))
            p.drawLine(last_pos, e.pos())

            last_pos _ e.pos()
            update()

    ___ pen_mouseReleaseEvent  e):
        generic_mouseReleaseEvent(e)

    # Brush events

    ___ brush_mousePressEvent  e):
        generic_mousePressEvent(e)

    ___ brush_mouseMoveEvent  e):
        __ last_pos:
            p _ QPainter(pixmap())
            p.sP..(?P..(active_color, c..['size'] * BRUSH_MULT, __.SolidLine, __.RoundCap, __.RoundJoin))
            p.drawLine(last_pos, e.pos())

            last_pos _ e.pos()
            update()

    ___ brush_mouseReleaseEvent  e):
        generic_mouseReleaseEvent(e)

    # Spray events

    ___ spray_mousePressEvent  e):
        generic_mousePressEvent(e)

    ___ spray_mouseMoveEvent  e):
        __ last_pos:
            p _ QPainter(pixmap())
            p.sP..(?P..(active_color, 1))

            ___ n __ ra..(c..['size'] * SPRAY_PAINT_N):
                xo _ random.gauss(0, c..['size'] * SPRAY_PAINT_MULT)
                yo _ random.gauss(0, c..['size'] * SPRAY_PAINT_MULT)
                p.drawPoint(e.x() + xo, e.y() + yo)

        update()

    ___ spray_mouseReleaseEvent  e):
        generic_mouseReleaseEvent(e)

    # Text events

    ___ keyPressEvent  e):
        __ mode __ 'text':
            __ e.key() __ __.Key_Backspace:
                current_text _ current_text[:-1]
            ____:
                current_text _ current_text + e.t..

    ___ text_mousePressEvent  e):
        __ e.button() __ __.LeftButton and current_pos is N..
            current_pos _ e.pos()
            current_text _ ""
            timer_event _ text_timerEvent

        elif e.button() __ __.LeftButton:

            timer_cleanup()
            # Draw the text to the image
            p _ QPainter(pixmap())
            p.setRenderHints(QPainter.Antialiasing)
            font _ build_font(c..)
            p.sF..(font)
            pen _ ?P..(primary_color, 1, __.SolidLine, __.RoundCap, __.RoundJoin)
            p.sP..(pen)
            p.drawText(current_pos, current_text)
            update()

            reset_mode()

        elif e.button() __ __.RightButton and current_pos:
            reset_mode()

    ___ text_timerEvent  final_F..):
        p _ QPainter(pixmap())
        p.setCompositionMode(QPainter.RasterOp_SourceXorDestination)
        pen _ PREVIEW_PEN
        p.sP..(pen)
        __ last_text:
            font _ build_font(last_config)
            p.sF..(font)
            p.drawText(current_pos, last_text)

        __ not final:
            font _ build_font(c..)
            p.sF..(font)
            p.drawText(current_pos, current_text)

        last_text _ current_text
        last_config _ c...copy()
        update()

    # Fill events

    ___ fill_mousePressEvent  e):

        __ e.button() __ __.LeftButton:
            active_color _ primary_color
        ____:
            active_color _ secondary_color

        image _ pixmap().toImage()
        w, h _ image.width(), image.height()
        x, y _ e.x(), e.y()

        # Get our target color from origin.
        target_color _ image.pixel(x,y)

        have_seen _ set()
        queue _ [(x, y)]

        ___ get_cardinal_points(have_seen, center_pos):
            points _   # list
            cx, cy _ center_pos
            ___ x, y __ [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                xx, yy _ cx + x, cy + y
                __ (xx >_ 0 and xx < w and
                    yy >_ 0 and yy < h and
                    (xx, yy) not __ have_seen):

                    points.ap..((xx, yy))
                    have_seen.add((xx, yy))

            r_ points

        # Now perform the search and fill.
        p _ QPainter(pixmap())
        p.sP..(?P..(active_color))

        while queue:
            x, y _ queue.pop()
            __ image.pixel(x, y) __ target_color:
                p.drawPoint(QPoint(x, y))
                queue.extend(get_cardinal_points(have_seen, (x, y)))

        update()

    # Dropper events

    ___ dropper_mousePressEvent  e):
        c _ pixmap().toImage().pixel(e.pos())
        hex _ QColor(c).name()

        __ e.button() __ __.LeftButton:
            set_primary_color(hex)
            primary_color_updated.e..(hex)  # Update UI.

        elif e.button() __ __.RightButton:
            set_secondary_color(hex)
            secondary_color_updated.e..(hex)  # Update UI.

    # Generic shape events: Rectangle, Ellipse, Rounded-rect

    ___ generic_shape_mousePressEvent  e):
        origin_pos _ e.pos()
        current_pos _ e.pos()
        timer_event _ generic_shape_timerEvent

    ___ generic_shape_timerEvent  final_F..):
        p _ QPainter(pixmap())
        p.setCompositionMode(QPainter.RasterOp_SourceXorDestination)
        pen _ preview_pen
        pen.setDashOffset(dash_offset)
        p.sP..(pen)
        __ last_pos:
            getattr(p, active_shape_fn)(QRect(origin_pos, last_pos), *active_shape_args)

        __ not final:
            dash_offset -_ 1
            pen.setDashOffset(dash_offset)
            p.sP..(pen)
            getattr(p, active_shape_fn)(QRect(origin_pos, current_pos), *active_shape_args)

        update()
        last_pos _ current_pos

    ___ generic_shape_mouseMoveEvent  e):
        current_pos _ e.pos()

    ___ generic_shape_mouseReleaseEvent  e):
        __ last_pos:
            # Clear up indicator.
            timer_cleanup()

            p _ QPainter(pixmap())
            p.sP..(?P..(primary_color, c..['size'], __.SolidLine, __.SquareCap, __.MiterJoin))

            __ c..['fill']:
                p.sB..(?B..(secondary_color))
            getattr(p, active_shape_fn)(QRect(origin_pos, e.pos()), *active_shape_args)
            update()

        reset_mode()

    # Line events

    ___ line_mousePressEvent  e):
        origin_pos _ e.pos()
        current_pos _ e.pos()
        preview_pen _ PREVIEW_PEN
        timer_event _ line_timerEvent

    ___ line_timerEvent  final_F..):
        p _ QPainter(pixmap())
        p.setCompositionMode(QPainter.RasterOp_SourceXorDestination)
        pen _ preview_pen
        p.sP..(pen)
        __ last_pos:
            p.drawLine(origin_pos, last_pos)

        __ not final:
            p.drawLine(origin_pos, current_pos)

        update()
        last_pos _ current_pos

    ___ line_mouseMoveEvent  e):
        current_pos _ e.pos()

    ___ line_mouseReleaseEvent  e):
        __ last_pos:
            # Clear up indicator.
            timer_cleanup()

            p _ QPainter(pixmap())
            p.sP..(?P..(primary_color, c..['size'], __.SolidLine, __.RoundCap, __.RoundJoin))

            p.drawLine(origin_pos, e.pos())
            update()

        reset_mode()

    # Generic poly events
    ___ generic_poly_mousePressEvent  e):
        __ e.button() __ __.LeftButton:
            __ history_pos:
                history_pos.ap..(e.pos())
            ____:
                history_pos _ [e.pos()]
                current_pos _ e.pos()
                timer_event _ generic_poly_timerEvent

        elif e.button() __ __.RightButton and history_pos:
            # Clean up, we're not drawing
            timer_cleanup()
            reset_mode()

    ___ generic_poly_timerEvent  final_F..):
        p _ QPainter(pixmap())
        p.setCompositionMode(QPainter.RasterOp_SourceXorDestination)
        pen _ preview_pen
        pen.setDashOffset(dash_offset)
        p.sP..(pen)
        __ last_history:
            getattr(p, active_shape_fn)(*last_history)

        __ not final:
            dash_offset -_ 1
            pen.setDashOffset(dash_offset)
            p.sP..(pen)
            getattr(p, active_shape_fn)(*history_pos + [current_pos])

        update()
        last_pos _ current_pos
        last_history _ history_pos + [current_pos]

    ___ generic_poly_mouseMoveEvent  e):
        current_pos _ e.pos()

    ___ generic_poly_mouseDoubleClickEvent  e):
        timer_cleanup()
        p _ QPainter(pixmap())
        p.sP..(?P..(primary_color, c..['size'], __.SolidLine, __.RoundCap, __.RoundJoin))

        # Note the brush is ignored for polylines.
        __ secondary_color:
            p.sB..(?B..(secondary_color))

        getattr(p, active_shape_fn)(*history_pos + [e.pos()])
        update()
        reset_mode()

    # Polyline events

    ___ polyline_mousePressEvent  e):
        active_shape_fn _ 'drawPolyline'
        preview_pen _ PREVIEW_PEN
        generic_poly_mousePressEvent(e)

    ___ polyline_timerEvent  final_F..):
        generic_poly_timerEvent(final)

    ___ polyline_mouseMoveEvent  e):
        generic_poly_mouseMoveEvent(e)

    ___ polyline_mouseDoubleClickEvent  e):
        generic_poly_mouseDoubleClickEvent(e)

    # Rectangle events

    ___ rect_mousePressEvent  e):
        active_shape_fn _ 'drawRect'
        active_shape_args _ ()
        preview_pen _ PREVIEW_PEN
        generic_shape_mousePressEvent(e)

    ___ rect_timerEvent  final_F..):
        generic_shape_timerEvent(final)

    ___ rect_mouseMoveEvent  e):
        generic_shape_mouseMoveEvent(e)

    ___ rect_mouseReleaseEvent  e):
        generic_shape_mouseReleaseEvent(e)

    # Polygon events

    ___ polygon_mousePressEvent  e):
        active_shape_fn _ 'drawPolygon'
        preview_pen _ PREVIEW_PEN
        generic_poly_mousePressEvent(e)

    ___ polygon_timerEvent  final_F..):
        generic_poly_timerEvent(final)

    ___ polygon_mouseMoveEvent  e):
        generic_poly_mouseMoveEvent(e)

    ___ polygon_mouseDoubleClickEvent  e):
        generic_poly_mouseDoubleClickEvent(e)

    # Ellipse events

    ___ ellipse_mousePressEvent  e):
        active_shape_fn _ 'drawEllipse'
        active_shape_args _ ()
        preview_pen _ PREVIEW_PEN
        generic_shape_mousePressEvent(e)

    ___ ellipse_timerEvent  final_F..):
        generic_shape_timerEvent(final)

    ___ ellipse_mouseMoveEvent  e):
        generic_shape_mouseMoveEvent(e)

    ___ ellipse_mouseReleaseEvent  e):
        generic_shape_mouseReleaseEvent(e)

    # Roundedrect events

    ___ roundrect_mousePressEvent  e):
        active_shape_fn _ 'drawRoundedRect'
        active_shape_args _ (25, 25)
        preview_pen _ PREVIEW_PEN
        generic_shape_mousePressEvent(e)

    ___ roundrect_timerEvent  final_F..):
        generic_shape_timerEvent(final)

    ___ roundrect_mouseMoveEvent  e):
        generic_shape_mouseMoveEvent(e)

    ___ roundrect_mouseReleaseEvent  e):
        generic_shape_mouseReleaseEvent(e)


c_ MainWindow(?MW.., Ui_MainWindow):

    ___  -   $ $$
        s__(MainWindow, self). - ($ $$)
        setupUi

        # Replace canvas placeholder from QtDesigner.
        horizontalLayout.removeWidget(canvas)
        canvas _ Canvas()
        canvas.initialize()
        # We need to enable mouse tracking to follow the mouse without the button pressed.
        canvas.setMouseTracking( st.
        # Enable focus to capture key inputs.
        canvas.setFocusPolicy(__.StrongFocus)
        horizontalLayout.aW..(canvas)

        # Setup the mode buttons
        mode_group _ QButtonGroup
        mode_group.setExclusive( st.

        ___ mode __ MODES:
            btn _ getattr  '%sButton' % mode)
            btn.pressed.c__(l___ mode_mode: canvas.set_mode(mode))
            mode_group.addButton(btn)

        # Setup the color selection buttons.
        primaryButton.pressed.c__(l___: choose_color(set_primary_color))
        secondaryButton.pressed.c__(l___: choose_color(set_secondary_color))

        # Initialize button colours.
        ___ n, hex __ en..(COLORS, 1):
            btn _ getattr  'colorButton_%d' % n)
            btn.sSS..('QPushButton { background-color: %s; }' % hex)
            btn.hex _ hex  # For use in the event below

            ___ patch_mousePressEvent(self_, e):
                __ e.button() __ __.LeftButton:
                    set_primary_color(self_.hex)

                elif e.button() __ __.RightButton:
                    set_secondary_color(self_.hex)

            btn.mousePressEvent _ types.MethodType(patch_mousePressEvent, btn)

        # Setup up action signals
        actionCopy.t___.c__(copy_to_clipboard)

        # Initialize animation timer.
        timer _ ?T..()
        timer.timeout.c__(canvas.on_timer)
        timer.sI..(100)
        timer.start()

        # Setup to agree with Canvas.
        set_primary_color('#000000')
        set_secondary_color('#ffffff')

        # Signals for canvas-initiated color changes (dropper).
        canvas.primary_color_updated.c__(set_primary_color)
        canvas.secondary_color_updated.c__(set_secondary_color)

        # Setup the stamp state.
        current_stamp_n _ -1
        next_stamp()
        stampnextButton.pressed.c__(next_stamp)

        # Menu options
        actionNewImage.t___.c__(canvas.initialize)
        actionOpenImage.t___.c__(open_file)
        actionSaveImage.t___.c__(save_file)
        actionClearImage.t___.c__(canvas.reset)
        actionInvertColors.t___.c__(invert)
        actionFlipHorizontal.t___.c__(flip_horizontal)
        actionFlipVertical.t___.c__(flip_vertical)

        # Setup the drawing toolbar.
        fontselect _ QFontComboBox()
        fontToolbar.aW..(fontselect)
        fontselect.currentFontChanged.c__(l___ f: canvas.set_config('font', f))
        fontselect.setCurrentFont(?F..('Times'))

        fontsize _ ?CB()
        fontsize.aI..([st.(s) ___ s __ FONT_SIZES])
        fontsize.cTC...c__(l___ f: canvas.set_config('fontsize', in.(f)))

        # Connect to the signal producing the text of the current selection. Convert the string to float
        # and set as the pointsize. We could also use the index + retrieve from FONT_SIZES.
        fontToolbar.aW..(fontsize)

        fontToolbar.aA..(actionBold)
        actionBold.t___.c__(l___ s: canvas.set_config('bold', s))
        fontToolbar.aA..(actionItalic)
        actionItalic.t___.c__(l___ s: canvas.set_config('italic', s))
        fontToolbar.aA..(actionUnderline)
        actionUnderline.t___.c__(l___ s: canvas.set_config('underline', s))

        sizeicon _ ?L..
        sizeicon.sP..(?P..(__.pa__.join('images', 'border-weight.png')))
        drawingToolbar.aW..(sizeicon)
        sizeselect _ ?S..()
        sizeselect.setRange(1,20)
        sizeselect.setOrientation(__.H..)
        sizeselect.valueChanged.c__(l___ s: canvas.set_config('size', s))
        drawingToolbar.aW..(sizeselect)

        actionFillShapes.t___.c__(l___ s: canvas.set_config('fill', s))
        drawingToolbar.aA..(actionFillShapes)
        actionFillShapes.sC__( st.

        s..

    ___ choose_color  callback):
        dlg _ QColorDialog()
        __ dlg.e..:
            callback( dlg.selectedColor().name() )

    ___ set_primary_color  hex):
        canvas.set_primary_color(hex)
        primaryButton.sSS..('QPushButton { background-color: %s; }' % hex)

    ___ set_secondary_color  hex):
        canvas.set_secondary_color(hex)
        secondaryButton.sSS..('QPushButton { background-color: %s; }' % hex)

    ___ next_stamp
        current_stamp_n +_ 1
        __ current_stamp_n >_ le.(STAMPS):
            current_stamp_n _ 0

        pixmap _ ?P..(STAMPS[current_stamp_n])
        stampnextButton.sI..(?I..(pixmap))

        canvas.current_stamp _ pixmap

    ___ copy_to_clipboard
        clipboard _ ?A...clipboard()

        __ canvas.mode __ 'selectrect' and canvas.locked:
            clipboard.sP..(canvas.selectrect_copy())

        elif canvas.mode __ 'selectpoly' and canvas.locked:
            clipboard.sP..(canvas.selectpoly_copy())

        ____:
            clipboard.sP..(canvas.pixmap())

    ___ open_file
        """
        Open image file for editing, scaling the smaller dimension and cropping the remainder.
        :return:
        """
        pa__, _ _ QFileDialog.getOpenFileName  "Open file", "", "PNG image files (*.png); JPEG image files (*jpg); All files (*.*)")

        __ pa__:
            pixmap _ ?P..()
            pixmap.load(pa__)

            # We need to crop down to the size of our canvas. Get the size of the loaded image.
            iw _ pixmap.width()
            ih _ pixmap.height()

            # Get the size of the space we're filling.
            cw, ch _ CANVAS_DIMENSIONS

            __ iw/cw < ih/ch:  # The height is relatively bigger than the width.
                pixmap _ pixmap.sTW..(cw)
                hoff _ (pixmap.height() - ch) // 2
                pixmap _ pixmap.copy(
                    QRect(QPoint(0, hoff), QPoint(cw, pixmap.height()-hoff))
                )

            elif iw/cw > ih/ch:  # The height is relatively bigger than the width.
                pixmap _ pixmap.scaledToHeight(ch)
                woff _ (pixmap.width() - cw) // 2
                pixmap _ pixmap.copy(
                    QRect(QPoint(woff, 0), QPoint(pixmap.width()-woff, ch))
                )

            canvas.sP..(pixmap)


    ___ save_file
        """
        Save active canvas to image file.
        :return:
        """
        pa__, _ _ QFileDialog.getSaveFileName  "Save file", "", "PNG Image file (*.png)")

        __ pa__:
            pixmap _ canvas.pixmap()
            pixmap.save(pa__, "PNG" )

    ___ invert
        img _ QImage(canvas.pixmap())
        img.invertPixels()
        pixmap _ ?P..()
        pixmap.convertFromImage(img)
        canvas.sP..(pixmap)

    ___ flip_horizontal
        pixmap _ canvas.pixmap()
        canvas.sP..(pixmap.transformed(QTransform().scale(-1, 1)))

    ___ flip_vertical
        pixmap _ canvas.pixmap()
        canvas.sP..(pixmap.transformed(QTransform().scale(1, -1)))



__ __name__ __ '__main__':

    app _ ?A..([])
    window _ MainWindow()
    app.e..()