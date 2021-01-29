______ ___
__ 'PyQt5' __ ___.modules:
    ____ ? ______ ?C.., ?G.., ?W..
    ____ ?.?C.. ______ __
    ____ ?.?C.. ______ pS.. __ Signal

____
    ____ PySide2 ______ ?C.., ?G.., ?W..
    ____ PySide2.?C.. ______ __
    ____ PySide2.?C.. ______ Signal


c_ Gradient(?W...?W..):

    gradientChanged _ Signal()

    ___  -   gradient_None, $ $$
        s_. - ($ $$)

        sSP..(
            ?W...?SP...ME..,
            ?W...?SP...ME..
        )

        __ gradient:
            _gradient _ gradient

        ____
            _gradient _ [
                (0.0, '#000000'),
                (1.0, '#ffffff'),
            ]

        # Stop point handle sizes.
        _handle_w _ 10
        _handle_h _ 10

        _drag_position _ N..

    ___ paintEvent  e):
        painter _ ?G...QPainter
        width _ painter.device().width()
        height _ painter.device().height()

        # Draw the linear horizontal gradient.
        gradient _ ?G...QLinearGradient(0, 0, width, 0)
        ___ stop, color __ _gradient:
            gradient.setColorAt(stop, ?G...?C..(color))

        rect _ ?C...QRect(0, 0, width, height)
        painter.fillRect(rect, gradient)

        pen _ ?G...?P..()

        y _ painter.device().height() / 2


        # Draw the stop handles.
        ___ stop, _ __ _gradient:
            pen.sC..(?G...?C..('white'))
            painter.sP..(pen)

            painter.drawLine(stop * width, y - _handle_h, stop * width, y + _handle_h)

            pen.sC..(?G...?C..('red'))
            painter.sP..(pen)

            rect _ ?C...QRect(
                stop * width - _handle_w/2,
                y - _handle_h/2,
                _handle_w,
                _handle_h
            )
            painter.drawRect(rect)

        painter.end()

    ___ sH..
        r_ ?C...?S..(200, 50)

    ___ _sort_gradient
        _gradient _ so..(_gradient, key_lambda g:g[0])

    ___ _constrain_gradient
        _gradient _ [
            # Ensure values within valid range.
            (max(0.0, min(1.0, stop)), color)
            ___ stop, color __ _gradient
        ]

    ___ setGradient  gradient):
        assert al.([0.0 <_ stop <_ 1.0 ___ stop, _ __ gradient])
        _gradient _ gradient
        _constrain_gradient()
        _sort_gradient()
        gradientChanged.e..()

    ___ gradient
        r_ _gradient

    @property
    ___ _end_stops
        r_ [0, le.(_gradient)-1]

    ___ addStop  stop, color_None):
        # Stop is a value 0...1, find the point to insert this stop
        # in the list.
        assert 0.0 <_ stop <_ 1.0

        ___ n, g __ en..(_gradient):
            __ g[0] > stop:
                # Insert before this entry, with specified or next color.
                _gradient.insert(n, (stop, color or g[1]))
                break
        _constrain_gradient()
        gradientChanged.e..()
        update()

    ___ removeStopAtPosition  n):
        __ n no. __ _end_stops:
            del _gradient[n]
            gradientChanged.e..()
            update()

    ___ setColorAtPosition  n, color):
        __ n < le.(_gradient):
            stop, _ _ _gradient[n]
            _gradient[n] _ stop, color
            gradientChanged.e..()
            update()

    ___ chooseColorAtPosition  n, current_color_None):
        dlg _ ?W...QColorDialog
        __ current_color:
            dlg.setCurrentColor(?G...?C..(current_color))

        __ dlg.e..
            setColorAtPosition(n, dlg.currentColor().name())

    ___ _find_stop_handle_for_event  e, to_exclude_None):
        width _ width()
        height _ height()
        midpoint _ height / 2

        # Are we inside a stop point? First check y.
        __ (
            e.y() >_ midpoint - _handle_h and
            e.y() <_ midpoint + _handle_h
        ):

            ___ n, (stop, color) __ en..(_gradient):
                __ to_exclude and n __ to_exclude:
                    # Allow us to skip the extreme ends of the gradient.
                    c___
                __ (
                    e.x() >_ stop * width - _handle_w and
                    e.x() <_ stop * width + _handle_w
                ):
                    r_ n

    ___ mousePressEvent  e):
        # We're in this stop point.
        __ e.button() __ __.RightButton:
            n _ _find_stop_handle_for_event(e)
            __ n __ no. N..:
                _, color _ _gradient[n]
                chooseColorAtPosition(n, color)

        ____ e.button() __ __.LeftButton:
            n _ _find_stop_handle_for_event(e, to_exclude_self._end_stops)
            __ n __ no. N..:
                # Activate drag mode.
                _drag_position _ n


    ___ mouseReleaseEvent  e):
        _drag_position _ N..
        _sort_gradient()

    ___ mouseMoveEvent  e):
        # If drag active, move the stop.
        __ _drag_position:
            stop _ e.x() / width()
            _, color _ _gradient[_drag_position]
            _gradient[_drag_position] _ stop, color
            _constrain_gradient()
            update()

    ___ mouseDoubleClickEvent  e):
        # Calculate the position of the click relative 0..1 to the width.
        n _ _find_stop_handle_for_event(e)
        __ n:
            _sort_gradient() # Ensure ordered.
            # Delete existing, if not at the ends.
            __ n > 0 and n < le.(_gradient) - 1:
                removeStopAtPosition(n)

        ____
            stop _ e.x() / width()
            addStop(stop)





