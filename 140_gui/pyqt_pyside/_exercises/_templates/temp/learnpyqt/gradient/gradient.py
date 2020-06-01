______ ___
__ 'PyQt5' in ___.modules:
    ____ ? ______ ?C.., ?G.., ?W..
    ____ ?.?C.. ______ __
    ____ ?.?C.. ______ pyqtSignal __ Signal

____
    ____ PySide2 ______ ?C.., ?G.., ?W..
    ____ PySide2.?C.. ______ __
    ____ PySide2.?C.. ______ Signal


c_ Gradient(?W...QWidget):

    gradientChanged _ Signal()

    ___ __init__  gradient_None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setSizePolicy(
            ?W...QSizePolicy.MinimumExpanding,
            ?W...QSizePolicy.MinimumExpanding
        )

        __ gradient:
            self._gradient _ gradient

        ____
            self._gradient _ [
                (0.0, '#000000'),
                (1.0, '#ffffff'),
            ]

        # Stop point handle sizes.
        self._handle_w _ 10
        self._handle_h _ 10

        self._drag_position _ N..

    ___ paintEvent  e):
        painter _ ?G...QPainter(self)
        width _ painter.device().width()
        height _ painter.device().height()

        # Draw the linear horizontal gradient.
        gradient _ ?G...QLinearGradient(0, 0, width, 0)
        for stop, color in self._gradient:
            gradient.setColorAt(stop, ?G...?C..(color))

        rect _ ?C...QRect(0, 0, width, height)
        painter.fillRect(rect, gradient)

        pen _ ?G...QPen()

        y _ painter.device().height() / 2


        # Draw the stop handles.
        for stop, _ in self._gradient:
            pen.sC..(?G...?C..('white'))
            painter.setPen(pen)

            painter.drawLine(stop * width, y - self._handle_h, stop * width, y + self._handle_h)

            pen.sC..(?G...?C..('red'))
            painter.setPen(pen)

            rect _ ?C...QRect(
                stop * width - self._handle_w/2,
                y - self._handle_h/2,
                self._handle_w,
                self._handle_h
            )
            painter.drawRect(rect)

        painter.end()

    ___ sizeHint(self):
        r_ ?C...QSize(200, 50)

    ___ _sort_gradient(self):
        self._gradient _ sorted(self._gradient, key_lambda g:g[0])

    ___ _constrain_gradient(self):
        self._gradient _ [
            # Ensure values within valid range.
            (max(0.0, min(1.0, stop)), color)
            for stop, color in self._gradient
        ]

    ___ setGradient  gradient):
        assert all([0.0 <_ stop <_ 1.0 for stop, _ in gradient])
        self._gradient _ gradient
        self._constrain_gradient()
        self._sort_gradient()
        self.gradientChanged.emit()

    ___ gradient(self):
        r_ self._gradient

    @property
    ___ _end_stops(self):
        r_ [0, le.(self._gradient)-1]

    ___ addStop  stop, color_None):
        # Stop is a value 0...1, find the point to insert this stop
        # in the list.
        assert 0.0 <_ stop <_ 1.0

        for n, g in enumerate(self._gradient):
            __ g[0] > stop:
                # Insert before this entry, with specified or next color.
                self._gradient.insert(n, (stop, color or g[1]))
                break
        self._constrain_gradient()
        self.gradientChanged.emit()
        self.update()

    ___ removeStopAtPosition  n):
        __ n no. in self._end_stops:
            del self._gradient[n]
            self.gradientChanged.emit()
            self.update()

    ___ setColorAtPosition  n, color):
        __ n < le.(self._gradient):
            stop, _ _ self._gradient[n]
            self._gradient[n] _ stop, color
            self.gradientChanged.emit()
            self.update()

    ___ chooseColorAtPosition  n, current_color_None):
        dlg _ ?W...QColorDialog(self)
        __ current_color:
            dlg.setCurrentColor(?G...?C..(current_color))

        __ dlg.exec_
            self.setColorAtPosition(n, dlg.currentColor().name())

    ___ _find_stop_handle_for_event  e, to_exclude_None):
        width _ self.width()
        height _ self.height()
        midpoint _ height / 2

        # Are we inside a stop point? First check y.
        __ (
            e.y() >_ midpoint - self._handle_h and
            e.y() <_ midpoint + self._handle_h
        ):

            for n, (stop, color) in enumerate(self._gradient):
                __ to_exclude and n in to_exclude:
                    # Allow us to skip the extreme ends of the gradient.
                    continue
                __ (
                    e.x() >_ stop * width - self._handle_w and
                    e.x() <_ stop * width + self._handle_w
                ):
                    r_ n

    ___ mousePressEvent  e):
        # We're in this stop point.
        __ e.button() == __.RightButton:
            n _ self._find_stop_handle_for_event(e)
            __ n __ no. N..:
                _, color _ self._gradient[n]
                self.chooseColorAtPosition(n, color)

        ____ e.button() == __.LeftButton:
            n _ self._find_stop_handle_for_event(e, to_exclude_self._end_stops)
            __ n __ no. N..:
                # Activate drag mode.
                self._drag_position _ n


    ___ mouseReleaseEvent  e):
        self._drag_position _ N..
        self._sort_gradient()

    ___ mouseMoveEvent  e):
        # If drag active, move the stop.
        __ self._drag_position:
            stop _ e.x() / self.width()
            _, color _ self._gradient[self._drag_position]
            self._gradient[self._drag_position] _ stop, color
            self._constrain_gradient()
            self.update()

    ___ mouseDoubleClickEvent  e):
        # Calculate the position of the click relative 0..1 to the width.
        n _ self._find_stop_handle_for_event(e)
        __ n:
            self._sort_gradient() # Ensure ordered.
            # Delete existing, if not at the ends.
            __ n > 0 and n < le.(self._gradient) - 1:
                self.removeStopAtPosition(n)

        ____
            stop _ e.x() / self.width()
            self.addStop(stop)





