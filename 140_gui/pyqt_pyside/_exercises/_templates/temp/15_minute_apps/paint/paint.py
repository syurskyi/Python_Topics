from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from MainWindow import Ui_MainWindow

import os
import random
import types


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
STAMPS = [os.path.join(STAMP_DIR, f) ___ f __ os.listdir(STAMP_DIR)]

SELECTION_PEN = QPen(QColor(0xff, 0xff, 0xff), 1, Qt.DashLine)
PREVIEW_PEN = QPen(QColor(0xff, 0xff, 0xff), 1, Qt.SolidLine)


def build_font(config):
    """
    Construct a complete font from the configuration options
    :param self:
    :param config:
    :return: QFont
    """
    font = config['font']
    font.setPointSize(config['fontsize'])
    font.setBold(config['bold'])
    font.setItalic(config['italic'])
    font.setUnderline(config['underline'])
    return font


class Canvas(QLabel):

    mode = 'rectangle'

    primary_color = QColor(Qt.black)
    secondary_color = None

    primary_color_updated = pyqtSignal(str)
    secondary_color_updated = pyqtSignal(str)

    # Store configuration settings, including pen width, fonts etc.
    config = {
        # Drawing options.
        'size': 1,
        'fill': True,
        # Font options.
        'font': QFont('Times'),
        'fontsize': 12,
        'bold': False,
        'italic': False,
        'underline': False,
    }

    active_color = None
    preview_pen = None

    timer_event = None

    current_stamp = None

    def initialize
        background_color = QColor(secondary_color) if secondary_color else QColor(Qt.white)
        eraser_color = QColor(secondary_color) if secondary_color else QColor(Qt.white)
        eraser_color.setAlpha(100)
        reset()

    def reset
        # Create the pixmap for display.
        setPixmap(QPixmap(*CANVAS_DIMENSIONS))

        # Clear the canvas.
        pixmap().fill(background_color)

    def set_primary_color(self, hex):
        primary_color = QColor(hex)

    def set_secondary_color(self, hex):
        secondary_color = QColor(hex)

    def set_config(self, key, value):
        config[key] = value

    def set_mode(self, mode):
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

        last_config = {}

        dash_offset = 0
        locked = False
        # Apply the mode
        mode = mode

    def reset_mode
        set_mode(mode)

    def on_timer
        if timer_event:
            timer_event()

    def timer_cleanup
        if timer_event:
            # Stop the timer, then trigger cleanup.
            timer_event = timer_event
            timer_event = None
            timer_event(final=True)

    # Mouse events.

    def mousePressEvent(self, e):
        fn = getattr(self, "%s_mousePressEvent" % mode, None)
        if fn:
            return fn(e)

    def mouseMoveEvent(self, e):
        fn = getattr(self, "%s_mouseMoveEvent" % mode, None)
        if fn:
            return fn(e)

    def mouseReleaseEvent(self, e):
        fn = getattr(self, "%s_mouseReleaseEvent" % mode, None)
        if fn:
            return fn(e)

    def mouseDoubleClickEvent(self, e):
        fn = getattr(self, "%s_mouseDoubleClickEvent" % mode, None)
        if fn:
            return fn(e)

    # Generic events (shared by brush-like tools)

    def generic_mousePressEvent(self, e):
        last_pos = e.pos()

        if e.button() == Qt.LeftButton:
            active_color = primary_color
        else:
            active_color = secondary_color

    def generic_mouseReleaseEvent(self, e):
        last_pos = None

    # Mode-specific events.

    # Select polygon events

    def selectpoly_mousePressEvent(self, e):
        if not locked or e.button == Qt.RightButton:
            active_shape_fn = 'drawPolygon'
            preview_pen = SELECTION_PEN
            generic_poly_mousePressEvent(e)

    def selectpoly_timerEvent(self, final=False):
        generic_poly_timerEvent(final)

    def selectpoly_mouseMoveEvent(self, e):
        if not locked:
            generic_poly_mouseMoveEvent(e)

    def selectpoly_mouseDoubleClickEvent(self, e):
        current_pos = e.pos()
        locked = True

    def selectpoly_copy
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
        bitmap.clear()  # Starts with random data visible.

        p = QPainter(bitmap)
        # Construct a mask where the user selected area will be kept, the rest removed from the image is transparent.
        userpoly = QPolygon(history_pos + [current_pos])
        p.setPen(QPen(Qt.color1))
        p.setBrush(QBrush(Qt.color1))  # Solid color, Qt.color1 == bit on.
        p.drawPolygon(userpoly)
        p.end()

        # Set our created mask on the image.
        pixmap.setMask(bitmap)

        # Calculate the bounding rect and return a copy of that region.
        return pixmap.copy(userpoly.boundingRect())

    # Select rectangle events

    def selectrect_mousePressEvent(self, e):
        active_shape_fn = 'drawRect'
        preview_pen = SELECTION_PEN
        generic_shape_mousePressEvent(e)

    def selectrect_timerEvent(self, final=False):
        generic_shape_timerEvent(final)

    def selectrect_mouseMoveEvent(self, e):
        if not locked:
            current_pos = e.pos()

    def selectrect_mouseReleaseEvent(self, e):
        current_pos = e.pos()
        locked = True

    def selectrect_copy
        """
        Copy a rectangle region of the current image, returning it.

        :return: QPixmap of the copied region.
        """
        timer_cleanup()
        return pixmap().copy(QRect(origin_pos, current_pos))

    # Eraser events

    def eraser_mousePressEvent(self, e):
        generic_mousePressEvent(e)

    def eraser_mouseMoveEvent(self, e):
        if last_pos:
            p = QPainter(pixmap())
            p.setPen(QPen(eraser_color, 30, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
            p.drawLine(last_pos, e.pos())

            last_pos = e.pos()
            update()

    def eraser_mouseReleaseEvent(self, e):
        generic_mouseReleaseEvent(e)

    # Stamp (pie) events

    def stamp_mousePressEvent(self, e):
        p = QPainter(pixmap())
        stamp = current_stamp
        p.drawPixmap(e.x() - stamp.width() // 2, e.y() - stamp.height() // 2, stamp)
        update()

    # Pen events

    def pen_mousePressEvent(self, e):
        generic_mousePressEvent(e)

    def pen_mouseMoveEvent(self, e):
        if last_pos:
            p = QPainter(pixmap())
            p.setPen(QPen(active_color, config['size'], Qt.SolidLine, Qt.SquareCap, Qt.RoundJoin))
            p.drawLine(last_pos, e.pos())

            last_pos = e.pos()
            update()

    def pen_mouseReleaseEvent(self, e):
        generic_mouseReleaseEvent(e)

    # Brush events

    def brush_mousePressEvent(self, e):
        generic_mousePressEvent(e)

    def brush_mouseMoveEvent(self, e):
        if last_pos:
            p = QPainter(pixmap())
            p.setPen(QPen(active_color, config['size'] * BRUSH_MULT, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
            p.drawLine(last_pos, e.pos())

            last_pos = e.pos()
            update()

    def brush_mouseReleaseEvent(self, e):
        generic_mouseReleaseEvent(e)

    # Spray events

    def spray_mousePressEvent(self, e):
        generic_mousePressEvent(e)

    def spray_mouseMoveEvent(self, e):
        if last_pos:
            p = QPainter(pixmap())
            p.setPen(QPen(active_color, 1))

            ___ n __ range(config['size'] * SPRAY_PAINT_N):
                xo = random.gauss(0, config['size'] * SPRAY_PAINT_MULT)
                yo = random.gauss(0, config['size'] * SPRAY_PAINT_MULT)
                p.drawPoint(e.x() + xo, e.y() + yo)

        update()

    def spray_mouseReleaseEvent(self, e):
        generic_mouseReleaseEvent(e)

    # Text events

    def keyPressEvent(self, e):
        if mode == 'text':
            if e.key() == Qt.Key_Backspace:
                current_text = current_text[:-1]
            else:
                current_text = current_text + e.text()

    def text_mousePressEvent(self, e):
        if e.button() == Qt.LeftButton and current_pos is None:
            current_pos = e.pos()
            current_text = ""
            timer_event = text_timerEvent

        elif e.button() == Qt.LeftButton:

            timer_cleanup()
            # Draw the text to the image
            p = QPainter(pixmap())
            p.setRenderHints(QPainter.Antialiasing)
            font = build_font(config)
            p.setFont(font)
            pen = QPen(primary_color, 1, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)
            p.setPen(pen)
            p.drawText(current_pos, current_text)
            update()

            reset_mode()

        elif e.button() == Qt.RightButton and current_pos:
            reset_mode()

    def text_timerEvent(self, final=False):
        p = QPainter(pixmap())
        p.setCompositionMode(QPainter.RasterOp_SourceXorDestination)
        pen = PREVIEW_PEN
        p.setPen(pen)
        if last_text:
            font = build_font(last_config)
            p.setFont(font)
            p.drawText(current_pos, last_text)

        if not final:
            font = build_font(config)
            p.setFont(font)
            p.drawText(current_pos, current_text)

        last_text = current_text
        last_config = config.copy()
        update()

    # Fill events

    def fill_mousePressEvent(self, e):

        if e.button() == Qt.LeftButton:
            active_color = primary_color
        else:
            active_color = secondary_color

        image = pixmap().toImage()
        w, h = image.width(), image.height()
        x, y = e.x(), e.y()

        # Get our target color from origin.
        target_color = image.pixel(x,y)

        have_seen = set()
        queue = [(x, y)]

        def get_cardinal_points(have_seen, center_pos):
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
        p.setPen(QPen(active_color))

        while queue:
            x, y = queue.pop()
            if image.pixel(x, y) == target_color:
                p.drawPoint(QPoint(x, y))
                queue.extend(get_cardinal_points(have_seen, (x, y)))

        update()

    # Dropper events

    def dropper_mousePressEvent(self, e):
        c = pixmap().toImage().pixel(e.pos())
        hex = QColor(c).name()

        if e.button() == Qt.LeftButton:
            set_primary_color(hex)
            primary_color_updated.emit(hex)  # Update UI.

        elif e.button() == Qt.RightButton:
            set_secondary_color(hex)
            secondary_color_updated.emit(hex)  # Update UI.

    # Generic shape events: Rectangle, Ellipse, Rounded-rect

    def generic_shape_mousePressEvent(self, e):
        origin_pos = e.pos()
        current_pos = e.pos()
        timer_event = generic_shape_timerEvent

    def generic_shape_timerEvent(self, final=False):
        p = QPainter(pixmap())
        p.setCompositionMode(QPainter.RasterOp_SourceXorDestination)
        pen = preview_pen
        pen.setDashOffset(dash_offset)
        p.setPen(pen)
        if last_pos:
            getattr(p, active_shape_fn)(QRect(origin_pos, last_pos), *active_shape_args)

        if not final:
            dash_offset -= 1
            pen.setDashOffset(dash_offset)
            p.setPen(pen)
            getattr(p, active_shape_fn)(QRect(origin_pos, current_pos), *active_shape_args)

        update()
        last_pos = current_pos

    def generic_shape_mouseMoveEvent(self, e):
        current_pos = e.pos()

    def generic_shape_mouseReleaseEvent(self, e):
        if last_pos:
            # Clear up indicator.
            timer_cleanup()

            p = QPainter(pixmap())
            p.setPen(QPen(primary_color, config['size'], Qt.SolidLine, Qt.SquareCap, Qt.MiterJoin))

            if config['fill']:
                p.setBrush(QBrush(secondary_color))
            getattr(p, active_shape_fn)(QRect(origin_pos, e.pos()), *active_shape_args)
            update()

        reset_mode()

    # Line events

    def line_mousePressEvent(self, e):
        origin_pos = e.pos()
        current_pos = e.pos()
        preview_pen = PREVIEW_PEN
        timer_event = line_timerEvent

    def line_timerEvent(self, final=False):
        p = QPainter(pixmap())
        p.setCompositionMode(QPainter.RasterOp_SourceXorDestination)
        pen = preview_pen
        p.setPen(pen)
        if last_pos:
            p.drawLine(origin_pos, last_pos)

        if not final:
            p.drawLine(origin_pos, current_pos)

        update()
        last_pos = current_pos

    def line_mouseMoveEvent(self, e):
        current_pos = e.pos()

    def line_mouseReleaseEvent(self, e):
        if last_pos:
            # Clear up indicator.
            timer_cleanup()

            p = QPainter(pixmap())
            p.setPen(QPen(primary_color, config['size'], Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))

            p.drawLine(origin_pos, e.pos())
            update()

        reset_mode()

    # Generic poly events
    def generic_poly_mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            if history_pos:
                history_pos.append(e.pos())
            else:
                history_pos = [e.pos()]
                current_pos = e.pos()
                timer_event = generic_poly_timerEvent

        elif e.button() == Qt.RightButton and history_pos:
            # Clean up, we're not drawing
            timer_cleanup()
            reset_mode()

    def generic_poly_timerEvent(self, final=False):
        p = QPainter(pixmap())
        p.setCompositionMode(QPainter.RasterOp_SourceXorDestination)
        pen = preview_pen
        pen.setDashOffset(dash_offset)
        p.setPen(pen)
        if last_history:
            getattr(p, active_shape_fn)(*last_history)

        if not final:
            dash_offset -= 1
            pen.setDashOffset(dash_offset)
            p.setPen(pen)
            getattr(p, active_shape_fn)(*history_pos + [current_pos])

        update()
        last_pos = current_pos
        last_history = history_pos + [current_pos]

    def generic_poly_mouseMoveEvent(self, e):
        current_pos = e.pos()

    def generic_poly_mouseDoubleClickEvent(self, e):
        timer_cleanup()
        p = QPainter(pixmap())
        p.setPen(QPen(primary_color, config['size'], Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))

        # Note the brush is ignored for polylines.
        if secondary_color:
            p.setBrush(QBrush(secondary_color))

        getattr(p, active_shape_fn)(*history_pos + [e.pos()])
        update()
        reset_mode()

    # Polyline events

    def polyline_mousePressEvent(self, e):
        active_shape_fn = 'drawPolyline'
        preview_pen = PREVIEW_PEN
        generic_poly_mousePressEvent(e)

    def polyline_timerEvent(self, final=False):
        generic_poly_timerEvent(final)

    def polyline_mouseMoveEvent(self, e):
        generic_poly_mouseMoveEvent(e)

    def polyline_mouseDoubleClickEvent(self, e):
        generic_poly_mouseDoubleClickEvent(e)

    # Rectangle events

    def rect_mousePressEvent(self, e):
        active_shape_fn = 'drawRect'
        active_shape_args = ()
        preview_pen = PREVIEW_PEN
        generic_shape_mousePressEvent(e)

    def rect_timerEvent(self, final=False):
        generic_shape_timerEvent(final)

    def rect_mouseMoveEvent(self, e):
        generic_shape_mouseMoveEvent(e)

    def rect_mouseReleaseEvent(self, e):
        generic_shape_mouseReleaseEvent(e)

    # Polygon events

    def polygon_mousePressEvent(self, e):
        active_shape_fn = 'drawPolygon'
        preview_pen = PREVIEW_PEN
        generic_poly_mousePressEvent(e)

    def polygon_timerEvent(self, final=False):
        generic_poly_timerEvent(final)

    def polygon_mouseMoveEvent(self, e):
        generic_poly_mouseMoveEvent(e)

    def polygon_mouseDoubleClickEvent(self, e):
        generic_poly_mouseDoubleClickEvent(e)

    # Ellipse events

    def ellipse_mousePressEvent(self, e):
        active_shape_fn = 'drawEllipse'
        active_shape_args = ()
        preview_pen = PREVIEW_PEN
        generic_shape_mousePressEvent(e)

    def ellipse_timerEvent(self, final=False):
        generic_shape_timerEvent(final)

    def ellipse_mouseMoveEvent(self, e):
        generic_shape_mouseMoveEvent(e)

    def ellipse_mouseReleaseEvent(self, e):
        generic_shape_mouseReleaseEvent(e)

    # Roundedrect events

    def roundrect_mousePressEvent(self, e):
        active_shape_fn = 'drawRoundedRect'
        active_shape_args = (25, 25)
        preview_pen = PREVIEW_PEN
        generic_shape_mousePressEvent(e)

    def roundrect_timerEvent(self, final=False):
        generic_shape_timerEvent(final)

    def roundrect_mouseMoveEvent(self, e):
        generic_shape_mouseMoveEvent(e)

    def roundrect_mouseReleaseEvent(self, e):
        generic_shape_mouseReleaseEvent(e)


class MainWindow(QMainWindow, Ui_MainWindow):

    def  - (self, $ $$
        super(MainWindow, self). - ($ $$)
        setupUi

        # Replace canvas placeholder from QtDesigner.
        horizontalLayout.removeWidget(canvas)
        canvas = Canvas()
        canvas.initialize()
        # We need to enable mouse tracking to follow the mouse without the button pressed.
        canvas.setMouseTracking(True)
        # Enable focus to capture key inputs.
        canvas.setFocusPolicy(Qt.StrongFocus)
        horizontalLayout.addWidget(canvas)

        # Setup the mode buttons
        mode_group = QButtonGroup
        mode_group.setExclusive(True)

        ___ mode __ MODES:
            btn = getattr(self, '%sButton' % mode)
            btn.pressed.connect(l___ mode=mode: canvas.set_mode(mode))
            mode_group.addButton(btn)

        # Setup the color selection buttons.
        primaryButton.pressed.connect(l___: choose_color(set_primary_color))
        secondaryButton.pressed.connect(l___: choose_color(set_secondary_color))

        # Initialize button colours.
        ___ n, hex __ en..(COLORS, 1):
            btn = getattr(self, 'colorButton_%d' % n)
            btn.setStyleSheet('QPushButton { background-color: %s; }' % hex)
            btn.hex = hex  # For use in the event below

            def patch_mousePressEvent(self_, e):
                if e.button() == Qt.LeftButton:
                    set_primary_color(self_.hex)

                elif e.button() == Qt.RightButton:
                    set_secondary_color(self_.hex)

            btn.mousePressEvent = types.MethodType(patch_mousePressEvent, btn)

        # Setup up action signals
        actionCopy.triggered.connect(copy_to_clipboard)

        # Initialize animation timer.
        timer = QTimer()
        timer.timeout.connect(canvas.on_timer)
        timer.setInterval(100)
        timer.start()

        # Setup to agree with Canvas.
        set_primary_color('#000000')
        set_secondary_color('#ffffff')

        # Signals for canvas-initiated color changes (dropper).
        canvas.primary_color_updated.connect(set_primary_color)
        canvas.secondary_color_updated.connect(set_secondary_color)

        # Setup the stamp state.
        current_stamp_n = -1
        next_stamp()
        stampnextButton.pressed.connect(next_stamp)

        # Menu options
        actionNewImage.triggered.connect(canvas.initialize)
        actionOpenImage.triggered.connect(open_file)
        actionSaveImage.triggered.connect(save_file)
        actionClearImage.triggered.connect(canvas.reset)
        actionInvertColors.triggered.connect(invert)
        actionFlipHorizontal.triggered.connect(flip_horizontal)
        actionFlipVertical.triggered.connect(flip_vertical)

        # Setup the drawing toolbar.
        fontselect = QFontComboBox()
        fontToolbar.addWidget(fontselect)
        fontselect.currentFontChanged.connect(l___ f: canvas.set_config('font', f))
        fontselect.setCurrentFont(QFont('Times'))

        fontsize = ?CB()
        fontsize.aI..([str(s) ___ s __ FONT_SIZES])
        fontsize.currentTextChanged.connect(l___ f: canvas.set_config('fontsize', int(f)))

        # Connect to the signal producing the text of the current selection. Convert the string to float
        # and set as the pointsize. We could also use the index + retrieve from FONT_SIZES.
        fontToolbar.addWidget(fontsize)

        fontToolbar.addAction(actionBold)
        actionBold.triggered.connect(l___ s: canvas.set_config('bold', s))
        fontToolbar.addAction(actionItalic)
        actionItalic.triggered.connect(l___ s: canvas.set_config('italic', s))
        fontToolbar.addAction(actionUnderline)
        actionUnderline.triggered.connect(l___ s: canvas.set_config('underline', s))

        sizeicon = QLabel()
        sizeicon.setPixmap(QPixmap(os.path.join('images', 'border-weight.png')))
        drawingToolbar.addWidget(sizeicon)
        sizeselect = QSlider()
        sizeselect.setRange(1,20)
        sizeselect.setOrientation(Qt.Horizontal)
        sizeselect.valueChanged.connect(l___ s: canvas.set_config('size', s))
        drawingToolbar.addWidget(sizeselect)

        actionFillShapes.triggered.connect(l___ s: canvas.set_config('fill', s))
        drawingToolbar.addAction(actionFillShapes)
        actionFillShapes.setChecked(True)

        show()

    def choose_color(self, callback):
        dlg = QColorDialog()
        if dlg.exec():
            callback( dlg.selectedColor().name() )

    def set_primary_color(self, hex):
        canvas.set_primary_color(hex)
        primaryButton.setStyleSheet('QPushButton { background-color: %s; }' % hex)

    def set_secondary_color(self, hex):
        canvas.set_secondary_color(hex)
        secondaryButton.setStyleSheet('QPushButton { background-color: %s; }' % hex)

    def next_stamp
        current_stamp_n += 1
        if current_stamp_n >= len(STAMPS):
            current_stamp_n = 0

        pixmap = QPixmap(STAMPS[current_stamp_n])
        stampnextButton.setIcon(QIcon(pixmap))

        canvas.current_stamp = pixmap

    def copy_to_clipboard
        clipboard = QApplication.clipboard()

        if canvas.mode == 'selectrect' and canvas.locked:
            clipboard.setPixmap(canvas.selectrect_copy())

        elif canvas.mode == 'selectpoly' and canvas.locked:
            clipboard.setPixmap(canvas.selectpoly_copy())

        else:
            clipboard.setPixmap(canvas.pixmap())

    def open_file
        """
        Open image file for editing, scaling the smaller dimension and cropping the remainder.
        :return:
        """
        path, _ = QFileDialog.getOpenFileName(self, "Open file", "", "PNG image files (*.png); JPEG image files (*jpg); All files (*.*)")

        if path:
            pixmap = QPixmap()
            pixmap.load(path)

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

            canvas.setPixmap(pixmap)


    def save_file
        """
        Save active canvas to image file.
        :return:
        """
        path, _ = QFileDialog.getSaveFileName(self, "Save file", "", "PNG Image file (*.png)")

        if path:
            pixmap = canvas.pixmap()
            pixmap.save(path, "PNG" )

    def invert
        img = QImage(canvas.pixmap())
        img.invertPixels()
        pixmap = QPixmap()
        pixmap.convertFromImage(img)
        canvas.setPixmap(pixmap)

    def flip_horizontal
        pixmap = canvas.pixmap()
        canvas.setPixmap(pixmap.transformed(QTransform().scale(-1, 1)))

    def flip_vertical
        pixmap = canvas.pixmap()
        canvas.setPixmap(pixmap.transformed(QTransform().scale(1, -1)))



if __name__ == '__main__':

    app = QApplication([])
    window = MainWindow()
    app.exec_()