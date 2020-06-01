______ sys
if 'PyQt5' in sys.modules:
    ____ ? ______ QtCore, QtGui, ?W..
    ____ ?.QtCore ______ Qt
    ____ ?.QtCore ______ pyqtSignal as Signal

else:
    ____ PySide2 ______ QtCore, QtGui, ?W..
    ____ PySide2.QtCore ______ Qt
    ____ PySide2.QtCore ______ Signal


class Gradient(?W...QWidget):

    gradientChanged _ Signal()

    ___ __init__(self, gradient_None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setSizePolicy(
            ?W...QSizePolicy.MinimumExpanding,
            ?W...QSizePolicy.MinimumExpanding
        )

        if gradient:
            self._gradient _ gradient

        else:
            self._gradient _ [
                (0.0, '#000000'),
                (1.0, '#ffffff'),
            ]

        # Stop point handle sizes.
        self._handle_w _ 10
        self._handle_h _ 10

        self._drag_position _ None

    ___ paintEvent(self, e):
        painter _ QtGui.QPainter(self)
        width _ painter.device().width()
        height _ painter.device().height()

        # Draw the linear horizontal gradient.
        gradient _ QtGui.QLinearGradient(0, 0, width, 0)
        for stop, color in self._gradient:
            gradient.setColorAt(stop, QtGui.QColor(color))

        rect _ QtCore.QRect(0, 0, width, height)
        painter.fillRect(rect, gradient)

        pen _ QtGui.QPen()

        y _ painter.device().height() / 2


        # Draw the stop handles.
        for stop, _ in self._gradient:
            pen.setColor(QtGui.QColor('white'))
            painter.setPen(pen)

            painter.drawLine(stop * width, y - self._handle_h, stop * width, y + self._handle_h)

            pen.setColor(QtGui.QColor('red'))
            painter.setPen(pen)

            rect _ QtCore.QRect(
                stop * width - self._handle_w/2,
                y - self._handle_h/2,
                self._handle_w,
                self._handle_h
            )
            painter.drawRect(rect)

        painter.end()

    ___ sizeHint(self):
        return QtCore.QSize(200, 50)

    ___ _sort_gradient(self):
        self._gradient _ sorted(self._gradient, key_lambda g:g[0])

    ___ _constrain_gradient(self):
        self._gradient _ [
            # Ensure values within valid range.
            (max(0.0, min(1.0, stop)), color)
            for stop, color in self._gradient
        ]

    ___ setGradient(self, gradient):
        assert all([0.0 <_ stop <_ 1.0 for stop, _ in gradient])
        self._gradient _ gradient
        self._constrain_gradient()
        self._sort_gradient()
        self.gradientChanged.emit()

    ___ gradient(self):
        return self._gradient

    @property
    ___ _end_stops(self):
        return [0, len(self._gradient)-1]

    ___ addStop(self, stop, color_None):
        # Stop is a value 0...1, find the point to insert this stop
        # in the list.
        assert 0.0 <_ stop <_ 1.0

        for n, g in enumerate(self._gradient):
            if g[0] > stop:
                # Insert before this entry, with specified or next color.
                self._gradient.insert(n, (stop, color or g[1]))
                break
        self._constrain_gradient()
        self.gradientChanged.emit()
        self.update()

    ___ removeStopAtPosition(self, n):
        if n not in self._end_stops:
            del self._gradient[n]
            self.gradientChanged.emit()
            self.update()

    ___ setColorAtPosition(self, n, color):
        if n < len(self._gradient):
            stop, _ _ self._gradient[n]
            self._gradient[n] _ stop, color
            self.gradientChanged.emit()
            self.update()

    ___ chooseColorAtPosition(self, n, current_color_None):
        dlg _ ?W...QColorDialog(self)
        if current_color:
            dlg.setCurrentColor(QtGui.QColor(current_color))

        if dlg.exec_
            self.setColorAtPosition(n, dlg.currentColor().name())

    ___ _find_stop_handle_for_event(self, e, to_exclude_None):
        width _ self.width()
        height _ self.height()
        midpoint _ height / 2

        # Are we inside a stop point? First check y.
        if (
            e.y() >_ midpoint - self._handle_h and
            e.y() <_ midpoint + self._handle_h
        ):

            for n, (stop, color) in enumerate(self._gradient):
                if to_exclude and n in to_exclude:
                    # Allow us to skip the extreme ends of the gradient.
                    continue
                if (
                    e.x() >_ stop * width - self._handle_w and
                    e.x() <_ stop * width + self._handle_w
                ):
                    return n

    ___ mousePressEvent(self, e):
        # We're in this stop point.
        if e.button() == Qt.RightButton:
            n _ self._find_stop_handle_for_event(e)
            if n is not None:
                _, color _ self._gradient[n]
                self.chooseColorAtPosition(n, color)

        elif e.button() == Qt.LeftButton:
            n _ self._find_stop_handle_for_event(e, to_exclude_self._end_stops)
            if n is not None:
                # Activate drag mode.
                self._drag_position _ n


    ___ mouseReleaseEvent(self, e):
        self._drag_position _ None
        self._sort_gradient()

    ___ mouseMoveEvent(self, e):
        # If drag active, move the stop.
        if self._drag_position:
            stop _ e.x() / self.width()
            _, color _ self._gradient[self._drag_position]
            self._gradient[self._drag_position] _ stop, color
            self._constrain_gradient()
            self.update()

    ___ mouseDoubleClickEvent(self, e):
        # Calculate the position of the click relative 0..1 to the width.
        n _ self._find_stop_handle_for_event(e)
        if n:
            self._sort_gradient() # Ensure ordered.
            # Delete existing, if not at the ends.
            if n > 0 and n < len(self._gradient) - 1:
                self.removeStopAtPosition(n)

        else:
            stop _ e.x() / self.width()
            self.addStop(stop)





