______ ___
__ 'PyQt5' __ ___.modules:
    ____ ? ______ ?C.., ?G.., ?W..
    ____ ?.?C.. ______ __
    ____ ?.?C.. ______ pS.. __ Signal

____
    ____ PySide2 ______ ?C.., ?G.., ?W..
    ____ PySide2.?C.. ______ __
    ____ PySide2.?C.. ______ Signal


c_ EqualizerBar(?W...?W..):

    ___  -   bars, steps, $ $$
        s_. - ($ $$)

        sSP..(
            ?W...?SP...ME..,
            ?W...?SP...ME..
        )

        __ isinstance(steps, li..):
            # list of colours.
            n_steps _ le.(steps)
            steps _ steps

        ____ isinstance(steps, in.):
            # int number of bars, defaults to red.
            n_steps _ steps
            steps _ ['red'] * steps

        ____
            r_ TypeError('steps must be a list or int')

        # Bar appearance.
        n_bars _ bars
        _x_solid_percent _ 0.8
        _y_solid_percent _ 0.8
        _background_color _ ?G...?C..('black')
        _padding _ 25  # n-pixel gap around edge.

        # Bar behaviour
        _timer _ N..
        setDecayFrequencyMs(100)
        _decay _ 10

        # Ranges
        _vmin _ 0
        _vmax _ 100

        # Current values are stored in a list.
        _values _ [0.0] * bars


    ___ paintEvent  e):
        painter _ ?G...QPainter

        brush _ ?G...?B..()
        brush.sC..(_background_color)
        brush.sS..(__.SolidPattern)
        rect _ ?C...QRect(0, 0, painter.device().width(), painter.device().height())
        painter.fillRect(rect, brush)

        # Define our canvas.
        d_height _ painter.device().height() - (_padding * 2)
        d_width _ painter.device().width() - (_padding * 2)

        # Draw the bars.
        step_y _ d_height / n_steps
        bar_height _ step_y * _y_solid_percent
        bar_height_space _ step_y * (1 - _x_solid_percent) / 2

        step_x _ d_width / n_bars
        bar_width _ step_x * _x_solid_percent
        bar_width_space _ step_x * (1 - _y_solid_percent) / 2

        ___ b __ ra..(n_bars):

            # Calculate the y-stop position for this bar, from the value in range.
            pc _ (_values[b] - _vmin) / (_vmax - _vmin)
            n_steps_to_draw _ in.(pc * n_steps)

            ___ n __ ra..(n_steps_to_draw):
                brush.sC..(?G...?C..(steps[n]))
                rect _ ?C...QRect(
                    _padding + (step_x * b) + bar_width_space,
                    _padding + d_height - ((1 + n) * step_y) + bar_height_space,
                    bar_width,
                    bar_height
                )
                painter.fillRect(rect, brush)

        painter.end()

    ___ sH..
        r_ ?C...?S..(20, 120)

    ___ _trigger_refresh
        update()

    ___ setDecay  f):
        _decay _ fl..(f)

    ___ setDecayFrequencyMs  ms):
        __ _timer:
            _timer.s..

        __ ms:
            _timer _ ?C...?T..
            _timer.sI..(ms)
            _timer.timeout.c..(_decay_beat)
            _timer.start()

    ___ _decay_beat
        _values _ [
            max(0, v - _decay)
            ___ v __ _values
        ]
        update()  # Redraw new position.

    ___ setValues  v):
        _values _ v
        update()

    ___ values
        r_ _values

    ___ setRange  vmin, vmax):
        assert fl..(vmin) < fl..(vmax)
        _vmin, _vmax _ fl..(vmin), fl..(vmax)

    ___ sC..  color):
        steps _ [color] * _bar.n_steps
        update()

    ___ setColors  colors):
        n_steps _ le.(colors)
        steps _ colors
        update()


    ___ setBarPadding  i):
        _padding _ in.(i)
        update()


    ___ setBarSolidPercent  f):
        _bar_solid_percent _ fl..(f)
        update()


    ___ setBackgroundColor  color):
        _background_color _ ?G...?C..(color)
        update()

