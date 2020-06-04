____ ?.QtGui ______ *
____ ?.QtWidgets ______ *
____ ?.?C.. ______ *

____ MainWindow ______ Ui_MainWindow

______ os
______ random
______ types


BRUSH_MULT = 3
SPRAY_PAINT_MULT = 5
SPRAY_PAINT_N = 100

COLORS = [
    '#000000', '#82817f', '#820300', '#868417', '#007e03', '#037e7b', '#040079',
    '#81067a', '#7f7e45', '#05403c', '#0a7cf6', '#093c7e', '#7e07f9', '#7c4002',

    '#ffffff', '#c1c1c1', '#f70406', '#fffd00', '#08fb01', '#0bf8ee', '#0000fa',
    '#b92fc2', '#fffc91', '#00fd83', '#87f9f9', '#8481c4', '#dc137d', '#fb803c',
]

FONT_SIZES = [7, 8, 9, 10, 11, 12, 13, 14, 18, 24, 36, 48, 64, 72, 96, 144, 288]

MODES = [
    'selectpoly', 'selectrect',
    'eraser', 'fill',
    'dropper', 'stamp',
    'pen', 'brush',
    'spray', 'text',
    'line', 'polyline',
    'rect', 'polygon',
    'ellipse', 'roundrect'
]

CANVAS_DIMENSIONS = 600, 400

STAMP_DIR = './stamps'
STAMPS = [os.pa__.join(STAMP_DIR, f) ___ f __ os.listdir(STAMP_DIR)]

SELECTION_PEN = ?P..(QColor(0xff, 0xff, 0xff), 1, __.DashLine)
PREVIEW_PEN = ?P..(QColor(0xff, 0xff, 0xff), 1, __.SolidLine)


___ build_font(c..):
    """
    Construct a complete font from the configuration options
    :param self:
    :param config:
    :return: QFont
    """
    font = c..['font']
    font.sPS..(c..['fontsize'])
    font.setBold(c..['bold'])
    font.setItalic(c..['italic'])
    font.setUnderline(c..['underline'])
    return font


c_ Canvas(QLabel):

    mode = 'rectangle'

    primary_color = QColor(__.black)
    secondary_color = None

    primary_color_updated = pS.. st.
    secondary_color_updated = pS.. st.

    # Store configuration settings, including pen width, fonts etc.
    c.. = {
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

    active_color = None
    preview_pen = None

    timer_event = None

    current_stamp = None

    ___ initialize
        background_color = QColor(secondary_color) if secondary_color ____ QColor(__.white)
        eraser_color = QColor(secondary_color) if secondary_color ____ QColor(__.white)
        eraser_color.setAlpha(100)
        reset()

    ___ reset
        # Create the pixmap for display.
        sP..(?P..(*CANVAS_DIMENSIONS))

        # Clear the canvas.
        pixmap().fill(background_color)

    ___ set_primary_color(self, hex):
        primary_color = QColor(hex)

    ___ set_secondary_color(self, hex):
        secondary_color = QColor(hex)

    ___ set_config(self, key, value):
        c..[key] = value

    ___ set_mode(self, mode):
        # Clean up active timer animations.
        timer_cleanup()
        # Reset mode-specific vars (all)
        active_shape_fn = None
        active_shape_args = ()

        origin_pos = None

        current_pos = None
        last_pos = None

        history_pos = None
        last_history = []

        current_text = ""
        last_text = ""

        last_config =   # dict

        dash_offset = 0
        locked = F..
        # Apply the mode
        mode = mode

    ___ reset_mode
        set_mode(mode)

    ___ on_timer
        if timer_event:
            timer_event()

    ___ timer_cleanup
        if timer_event:
            # Stop the timer, then trigger cleanup.
            timer_event = timer_event
            timer_event = None
            timer_event(final= st.

    # Mouse events.

    ___ mousePressEvent(self, e):
        fn = getattr(self, "%s_mousePressEvent" % mode, None)
        if fn:
            return fn(e)

    ___ mouseMoveEvent(self, e):
        fn = getattr(self, "%s_mouseMoveEvent" % mode, None)
        if fn:
            return fn(e)

    ___ mouseReleaseEvent(self, e):
        fn = getattr(self, "%s_mouseReleaseEvent" % mode, None)
        if fn:
            return fn(e)

    ___ mouseDoubleClickEvent(self, e):
        fn = getattr(self, "%s_mouseDoubleClickEvent" % mode, None)
        if fn:
            return fn(e)

    # Generic events (shared by brush-like tools)

    ___ generic_mousePressEvent(self, e):
        last_pos = e.pos()

        if e.button() __ __.LeftButton:
            active_color = primary_color
        ____:
            active_color = secondary_color

    ___ generic_mouseReleaseEvent(self, e):
        last_pos = None

    # Mode-specific events.

    # Select polygon events

    ___ selectpoly_mousePressEvent(self, e):
        if not locked or e.button __ __.RightButton:
            active_shape_fn = 'drawPolygon'
            preview_pen = SELECTION_PEN
            generic_poly_mousePressEvent(e)

    ___ selectpoly_timerEvent(self, final=F..):
        generic_poly_timerEvent(final)

    ___ selectpoly_mouseMoveEvent(self, e):
        if not locked:
            generic_poly_mouseMoveEvent(e)

    ___ selectpoly_mouseDoubleClickEvent(self, e):
        current_pos = e.pos()
        locked = T..

    ___ selectpoly_copy
        """
        Copy a polygon region from the current image, returning it.

        Create a mask for the selected area, and use it to blank
        out non-selected regions. Then get the bounding rect of the
        selection and crop to produce the smallest possible image.

        :return: QPixmap of the copied region.
        """
        timer_cleanup()

        pixmap = pixmap().copy()
        bitmap = QBitmap(*CANVAS_DIMENSIONS)
        bitmap.c..  # Starts with random data visible.

        p = QPainter(bitmap)
        # Construct a mask where the user selected area will be kept, the rest removed from the image is transparent.
        userpoly = QPolygon(history_pos + [current_pos])
        p.sP..(?P..(__.color1))
        p.sB..(?B..(__.color1))  # Solid color, Qt.color1 == bit on.
        p.drawPolygon(userpoly)
        p.end()

        # Set our created mask on the image.
        pixmap.setMask(bitmap)

        # Calculate the bounding rect and return a copy of that region.
        return pixmap.copy(userpoly.boundingRect())

    # Select rectangle events

    ___ selectrect_mousePressEvent(self, e):
        active_shape_fn = 'drawRect'
        preview_pen = SELECTION_PEN
        generic_shape_mousePressEvent(e)

    ___ selectrect_timerEvent(self, final=F..):
        generic_shape_timerEvent(final)

    ___ selectrect_mouseMoveEvent(self, e):
        if not locked:
            current_pos = e.pos()

    ___ selectrect_mouseReleaseEvent(self, e):
        current_pos = e.pos()
        locked = T..

    ___ selectrect_copy
        """
        Copy a rectangle region of the current image, returning it.

        :return: QPixmap of the copied region.
        """
        timer_cleanup()
        return pixmap().copy(QRect(origin_pos, current_pos))

    # Eraser events

    ___ eraser_mousePressEvent(self, e):
        generic_mousePressEvent(e)

    ___ eraser_mouseMoveEvent(self, e):
        if last_pos:
            p = QPainter(pixmap())
            p.sP..(?P..(eraser_color, 30, __.SolidLine, __.RoundCap, __.RoundJoin))
            p.drawLine(last_pos, e.pos())

            last_pos = e.pos()
            update()

    ___ eraser_mouseReleaseEvent(self, e):
        generic_mouseReleaseEvent(e)

    # Stamp (pie) events

    ___ stamp_mousePressEvent(self, e):
        p = QPainter(pixmap())
        stamp = current_stamp
        p.drawPixmap(e.x() - stamp.width() // 2, e.y() - stamp.height() // 2, stamp)
        update()

    # Pen events

    ___ pen_mousePressEvent(self, e):
        generic_mousePressEvent(e)

    ___ pen_mouseMoveEvent(self, e):
        if last_pos:
            p = QPainter(pixmap())
            p.sP..(?P..(active_color, c..['size'], __.SolidLine, __.SquareCap, __.RoundJoin))
            p.drawLine(last_pos, e.pos())

            last_pos = e.pos()
            update()

    ___ pen_mouseReleaseEvent(self, e):
        generic_mouseReleaseEvent(e)

    # Brush events

    ___ brush_mousePressEvent(self, e):
        generic_mousePressEvent(e)

    ___ brush_mouseMoveEvent(self, e):
        if last_pos:
            p = QPainter(pixmap())
            p.sP..(?P..(active_color, c..['size'] * BRUSH_MULT, __.SolidLine, __.RoundCap, __.RoundJoin))
            p.drawLine(last_pos, e.pos())

            last_pos = e.pos()
            update()

    ___ brush_mouseReleaseEvent(self, e):
        generic_mouseReleaseEvent(e)

    # Spray events

    ___ spray_mousePressEvent(self, e):
        generic_mousePressEvent(e)

    ___ spray_mouseMoveEvent(self, e):
        if last_pos:
            p = QPainter(pixmap())
            p.sP..(?P..(active_color, 1))

            ___ n __ ra..(c..['size'] * SPRAY_PAINT_N):
                xo = random.gauss(0, c..['size'] * SPRAY_PAINT_MULT)
                yo = random.gauss(0, c..['size'] * SPRAY_PAINT_MULT)
                p.drawPoint(e.x() + xo, e.y() + yo)

        update()

    ___ spray_mouseReleaseEvent(self, e):
        generic_mouseReleaseEvent(e)

    # Text events

    ___ keyPressEvent(self, e):
        if mode __ 'text':
            if e.key() __ __.Key_Backspace:
                current_text = current_text[:-1]
            ____:
                current_text = current_text + e.text()

    ___ text_mousePressEvent(self, e):
        if e.button() __ __.LeftButton and current_pos is None:
            current_pos = e.pos()
            current_text = ""
            timer_event = text_timerEvent

        elif e.button() __ __.LeftButton:

            timer_cleanup()
            # Draw the text to the image
            p = QPainter(pixmap())
            p.setRenderHints(QPainter.Antialiasing)
            font = build_font(c..)
            p.sF..(font)
            pen = ?P..(primary_color, 1, __.SolidLine, __.RoundCap, __.RoundJoin)
            p.sP..(pen)
            p.drawText(current_pos, current_text)
            update()

            reset_mode()

        elif e.button() __ __.RightButton and current_pos:
            reset_mode()

    ___ text_timerEvent(self, final=F..):
        p = QPainter(pixmap())
        p.setCompositionMode(QPainter.RasterOp_SourceXorDestination)
        pen = PREVIEW_PEN
        p.sP..(pen)
        if last_text:
            font = build_font(last_config)
            p.sF..(font)
            p.drawText(current_pos, last_text)

        if not final:
            font = build_font(c..)
            p.sF..(font)
            p.drawText(current_pos, current_text)

        last_text = current_text
        last_config = c...copy()
        update()

    # Fill events

    ___ fill_mousePressEvent(self, e):

        if e.button() __ __.LeftButton:
            active_color = primary_color
        ____:
            active_color = secondary_color

        image = pixmap().toImage()
        w, h = image.width(), image.height()
        x, y = e.x(), e.y()

        # Get our target color from origin.
        target_color = image.pixel(x,y)

        have_seen = set()
        queue = [(x, y)]

        ___ get_cardinal_points(have_seen, center_pos):
            points = []
            cx, cy = center_pos
            ___ x, y __ [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                xx, yy = cx + x, cy + y
                if (xx >= 0 and xx < w and
                    yy >= 0 and yy < h and
                    (xx, yy) not __ have_seen):

                    points.append((xx, yy))
                    have_seen.add((xx, yy))

            return points

        # Now perform the search and fill.
        p = QPainter(pixmap())
        p.sP..(?P..(active_color))

        while queue:
            x, y = queue.pop()
            if image.pixel(x, y) __ target_color:
                p.drawPoint(QPoint(x, y))
                queue.extend(get_cardinal_points(have_seen, (x, y)))

        update()

    # Dropper events

    ___ dropper_mousePressEvent(self, e):
        c = pixmap().toImage().pixel(e.pos())
        hex = QColor(c).name()

        if e.button() __ __.LeftButton:
            set_primary_color(hex)
            primary_color_updated.e..(hex)  # Update UI.

        elif e.button() __ __.RightButton:
            set_secondary_color(hex)
            secondary_color_updated.e..(hex)  # Update UI.

    # Generic shape events: Rectangle, Ellipse, Rounded-rect

    ___ generic_shape_mousePressEvent(self, e):
        origin_pos = e.pos()
        current_pos = e.pos()
        timer_event = generic_shape_timerEvent

    ___ generic_shape_timerEvent(self, final=F..):
        p = QPainter(pixmap())
        p.setCompositionMode(QPainter.RasterOp_SourceXorDestination)
        pen = preview_pen
        pen.setDashOffset(dash_offset)
        p.sP..(pen)
        if last_pos:
            getattr(p, active_shape_fn)(QRect(origin_pos, last_pos), *active_shape_args)

        if not final:
            dash_offset -= 1
            pen.setDashOffset(dash_offset)
            p.sP..(pen)
            getattr(p, active_shape_fn)(QRect(origin_pos, current_pos), *active_shape_args)

        update()
        last_pos = current_pos

    ___ generic_shape_mouseMoveEvent(self, e):
        current_pos = e.pos()

    ___ generic_shape_mouseReleaseEvent(self, e):
        if last_pos:
            # Clear up indicator.
            timer_cleanup()

            p = QPainter(pixmap())
            p.sP..(?P..(primary_color, c..['size'], __.SolidLine, __.SquareCap, __.MiterJoin))

            if c..['fill']:
                p.sB..(?B..(secondary_color))
            getattr(p, active_shape_fn)(QRect(origin_pos, e.pos()), *active_shape_args)
            update()

        reset_mode()

    # Line events

    ___ line_mousePressEvent(self, e):
        origin_pos = e.pos()
        current_pos = e.pos()
        preview_pen = PREVIEW_PEN
        timer_event = line_timerEvent

    ___ line_timerEvent(self, final=F..):
        p = QPainter(pixmap())
        p.setCompositionMode(QPainter.RasterOp_SourceXorDestination)
        pen = preview_pen
        p.sP..(pen)
        if last_pos:
            p.drawLine(origin_pos, last_pos)

        if not final:
            p.drawLine(origin_pos, current_pos)

        update()
        last_pos = current_pos

    ___ line_mouseMoveEvent(self, e):
        current_pos = e.pos()

    ___ line_mouseReleaseEvent(self, e):
        if last_pos:
            # Clear up indicator.
            timer_cleanup()

            p = QPainter(pixmap())
            p.sP..(?P..(primary_color, c..['size'], __.SolidLine, __.RoundCap, __.RoundJoin))

            p.drawLine(origin_pos, e.pos())
            update()

        reset_mode()

    # Generic poly events
    ___ generic_poly_mousePressEvent(self, e):
        if e.button() __ __.LeftButton:
            if history_pos:
                history_pos.append(e.pos())
            ____:
                history_pos = [e.pos()]
                current_pos = e.pos()
                timer_event = generic_poly_timerEvent

        elif e.button() __ __.RightButton and history_pos:
            # Clean up, we're not drawing
            timer_cleanup()
            reset_mode()

    ___ generic_poly_timerEvent(self, final=F..):
        p = QPainter(pixmap())
        p.setCompositionMode(QPainter.RasterOp_SourceXorDestination)
        pen = preview_pen
        pen.setDashOffset(dash_offset)
        p.sP..(pen)
        if last_history:
            getattr(p, active_shape_fn)(*last_history)

        if not final:
            dash_offset -= 1
            pen.setDashOffset(dash_offset)
            p.sP..(pen)
            getattr(p, active_shape_fn)(*history_pos + [current_pos])

        update()
        last_pos = current_pos
        last_history = history_pos + [current_pos]

    ___ generic_poly_mouseMoveEvent(self, e):
        current_pos = e.pos()

    ___ generic_poly_mouseDoubleClickEvent(self, e):
        timer_cleanup()
        p = QPainter(pixmap())
        p.sP..(?P..(primary_color, c..['size'], __.SolidLine, __.RoundCap, __.RoundJoin))

        # Note the brush is ignored for polylines.
        if secondary_color:
            p.sB..(?B..(secondary_color))

        getattr(p, active_shape_fn)(*history_pos + [e.pos()])
        update()
        reset_mode()

    # Polyline events

    ___ polyline_mousePressEvent(self, e):
        active_shape_fn = 'drawPolyline'
        preview_pen = PREVIEW_PEN
        generic_poly_mousePressEvent(e)

    ___ polyline_timerEvent(self, final=F..):
        generic_poly_timerEvent(final)

    ___ polyline_mouseMoveEvent(self, e):
        generic_poly_mouseMoveEvent(e)

    ___ polyline_mouseDoubleClickEvent(self, e):
        generic_poly_mouseDoubleClickEvent(e)

    # Rectangle events

    ___ rect_mousePressEvent(self, e):
        active_shape_fn = 'drawRect'
        active_shape_args = ()
        preview_pen = PREVIEW_PEN
        generic_shape_mousePressEvent(e)

    ___ rect_timerEvent(self, final=F..):
        generic_shape_timerEvent(final)

    ___ rect_mouseMoveEvent(self, e):
        generic_shape_mouseMoveEvent(e)

    ___ rect_mouseReleaseEvent(self, e):
        generic_shape_mouseReleaseEvent(e)

    # Polygon events

    ___ polygon_mousePressEvent(self, e):
        active_shape_fn = 'drawPolygon'
        preview_pen = PREVIEW_PEN
        generic_poly_mousePressEvent(e)

    ___ polygon_timerEvent(self, final=F..):
        generic_poly_timerEvent(final)

    ___ polygon_mouseMoveEvent(self, e):
        generic_poly_mouseMoveEvent(e)

    ___ polygon_mouseDoubleClickEvent(self, e):
        generic_poly_mouseDoubleClickEvent(e)

    # Ellipse events

    ___ ellipse_mousePressEvent(self, e):
        active_shape_fn = 'drawEllipse'
        active_shape_args = ()
        preview_pen = PREVIEW_PEN
        generic_shape_mousePressEvent(e)

    ___ ellipse_timerEvent(self, final=F..):
        generic_shape_timerEvent(final)

    ___ ellipse_mouseMoveEvent(self, e):
        generic_shape_mouseMoveEvent(e)

    ___ ellipse_mouseReleaseEvent(self, e):
        generic_shape_mouseReleaseEvent(e)

    # Roundedrect events

    ___ roundrect_mousePressEvent(self, e):
        active_shape_fn = 'drawRoundedRect'
        active_shape_args = (25, 25)
        preview_pen = PREVIEW_PEN
        generic_shape_mousePressEvent(e)

    ___ roundrect_timerEvent(self, final=F..):
        generic_shape_timerEvent(final)

    ___ roundrect_mouseMoveEvent(self, e):
        generic_shape_mouseMoveEvent(e)

    ___ roundrect_mouseReleaseEvent(self, e):
        generic_shape_mouseReleaseEvent(e)


c_ MainWindow(?MW.., Ui_MainWindow):

    ___  - (self, $ $$
        s__(MainWindow, self). - ($ $$)
        setupUi

        # Replace canvas placeholder from QtDesigner.
        horizontalLayout.removeWidget(canvas)
        canvas = Canvas()
        canvas.initialize()
        # We need to enable mouse tracking to follow the mouse without the button pressed.
        canvas.setMouseTracking( st.
        # Enable focus to capture key inputs.
        canvas.setFocusPolicy(__.StrongFocus)
        horizontalLayout.addWidget(canvas)

        # Setup the mode buttons
        mode_group = QButtonGroup
        mode_group.setExclusive( st.

        ___ mode __ MODES:
            btn = getattr(self, '%sButton' % mode)
            btn.pressed.c__(l___ mode=mode: canvas.set_mode(mode))
            mode_group.addButton(btn)

        # Setup the color selection buttons.
        primaryButton.pressed.c__(l___: choose_color(set_primary_color))
        secondaryButton.pressed.c__(l___: choose_color(set_secondary_color))

        # Initialize button colours.
        ___ n, hex __ en..(COLORS, 1):
            btn = getattr(self, 'colorButton_%d' % n)
            btn.sSS..('QPushButton { background-color: %s; }' % hex)
            btn.hex = hex  # For use in the event below

            ___ patch_mousePressEvent(self_, e):
                if e.button() __ __.LeftButton:
                    set_primary_color(self_.hex)

                elif e.button() __ __.RightButton:
                    set_secondary_color(self_.hex)

            btn.mousePressEvent = types.MethodType(patch_mousePressEvent, btn)

        # Setup up action signals
        actionCopy.t___.c__(copy_to_clipboard)

        # Initialize animation timer.
        timer = ?T..()
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
        current_stamp_n = -1
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
        fontselect = QFontComboBox()
        fontToolbar.addWidget(fontselect)
        fontselect.currentFontChanged.c__(l___ f: canvas.set_config('font', f))
        fontselect.setCurrentFont(?F..('Times'))

        fontsize = ?CB()
        fontsize.aI..([st.(s) ___ s __ FONT_SIZES])
        fontsize.cTC...c__(l___ f: canvas.set_config('fontsize', int(f)))

        # Connect to the signal producing the text of the current selection. Convert the string to float
        # and set as the pointsize. We could also use the index + retrieve from FONT_SIZES.
        fontToolbar.addWidget(fontsize)

        fontToolbar.aA..(actionBold)
        actionBold.t___.c__(l___ s: canvas.set_config('bold', s))
        fontToolbar.aA..(actionItalic)
        actionItalic.t___.c__(l___ s: canvas.set_config('italic', s))
        fontToolbar.aA..(actionUnderline)
        actionUnderline.t___.c__(l___ s: canvas.set_config('underline', s))

        sizeicon = ?L..
        sizeicon.sP..(?P..(os.pa__.join('images', 'border-weight.png')))
        drawingToolbar.addWidget(sizeicon)
        sizeselect = ?S..()
        sizeselect.setRange(1,20)
        sizeselect.setOrientation(__.H..)
        sizeselect.valueChanged.c__(l___ s: canvas.set_config('size', s))
        drawingToolbar.addWidget(sizeselect)

        actionFillShapes.t___.c__(l___ s: canvas.set_config('fill', s))
        drawingToolbar.aA..(actionFillShapes)
        actionFillShapes.sC__( st.

        s..

    ___ choose_color(self, callback):
        dlg = QColorDialog()
        if dlg.e..:
            callback( dlg.selectedColor().name() )

    ___ set_primary_color(self, hex):
        canvas.set_primary_color(hex)
        primaryButton.sSS..('QPushButton { background-color: %s; }' % hex)

    ___ set_secondary_color(self, hex):
        canvas.set_secondary_color(hex)
        secondaryButton.sSS..('QPushButton { background-color: %s; }' % hex)

    ___ next_stamp
        current_stamp_n += 1
        if current_stamp_n >= len(STAMPS):
            current_stamp_n = 0

        pixmap = ?P..(STAMPS[current_stamp_n])
        stampnextButton.sI..(?I..(pixmap))

        canvas.current_stamp = pixmap

    ___ copy_to_clipboard
        clipboard = ?A...clipboard()

        if canvas.mode __ 'selectrect' and canvas.locked:
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
        pa__, _ = QFileDialog.getOpenFileName(self, "Open file", "", "PNG image files (*.png); JPEG image files (*jpg); All files (*.*)")

        if pa__:
            pixmap = ?P..()
            pixmap.load(pa__)

            # We need to crop down to the size of our canvas. Get the size of the loaded image.
            iw = pixmap.width()
            ih = pixmap.height()

            # Get the size of the space we're filling.
            cw, ch = CANVAS_DIMENSIONS

            if iw/cw < ih/ch:  # The height is relatively bigger than the width.
                pixmap = pixmap.scaledToWidth(cw)
                hoff = (pixmap.height() - ch) // 2
                pixmap = pixmap.copy(
                    QRect(QPoint(0, hoff), QPoint(cw, pixmap.height()-hoff))
                )

            elif iw/cw > ih/ch:  # The height is relatively bigger than the width.
                pixmap = pixmap.scaledToHeight(ch)
                woff = (pixmap.width() - cw) // 2
                pixmap = pixmap.copy(
                    QRect(QPoint(woff, 0), QPoint(pixmap.width()-woff, ch))
                )

            canvas.sP..(pixmap)


    ___ save_file
        """
        Save active canvas to image file.
        :return:
        """
        pa__, _ = QFileDialog.getSaveFileName(self, "Save file", "", "PNG Image file (*.png)")

        if pa__:
            pixmap = canvas.pixmap()
            pixmap.save(pa__, "PNG" )

    ___ invert
        img = QImage(canvas.pixmap())
        img.invertPixels()
        pixmap = ?P..()
        pixmap.convertFromImage(img)
        canvas.sP..(pixmap)

    ___ flip_horizontal
        pixmap = canvas.pixmap()
        canvas.sP..(pixmap.transformed(QTransform().scale(-1, 1)))

    ___ flip_vertical
        pixmap = canvas.pixmap()
        canvas.sP..(pixmap.transformed(QTransform().scale(1, -1)))



if __name__ __ '__main__':

    app = ?A..([])
    window = MainWindow()
    app.e..()