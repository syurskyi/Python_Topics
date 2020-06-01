______ ___
__ 'PyQt5' in ___.modules:
    ____ ? ______ ?C.., ?G.., ?W..
    ____ ?.?C.. ______ __
    ____ ?.?C.. ______ pyqtSignal __ Signal

____
    ____ PySide2 ______ ?C.., ?G.., ?W..
    ____ PySide2.?C.. ______ __
    ____ PySide2.?C.. ______ Signal


c_ EqualizerBar(?W...QWidget):

    ___ __init__  bars, steps, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setSizePolicy(
            ?W...QSizePolicy.MinimumExpanding,
            ?W...QSizePolicy.MinimumExpanding
        )

        __ isinstance(steps, list):
            # list of colours.
            self.n_steps _ le.(steps)
            self.steps _ steps

        ____ isinstance(steps, int):
            # int number of bars, defaults to red.
            self.n_steps _ steps
            self.steps _ ['red'] * steps

        ____
            raise TypeError('steps must be a list or int')

        # Bar appearance.
        self.n_bars _ bars
        self._x_solid_percent _ 0.8
        self._y_solid_percent _ 0.8
        self._background_color _ ?G...?C..('black')
        self._padding _ 25  # n-pixel gap around edge.

        # Bar behaviour
        self._timer _ N..
        self.setDecayFrequencyMs(100)
        self._decay _ 10

        # Ranges
        self._vmin _ 0
        self._vmax _ 100

        # Current values are stored in a list.
        self._values _ [0.0] * bars


    ___ paintEvent  e):
        painter _ ?G...QPainter(self)

        brush _ ?G...QBrush()
        brush.sC..(self._background_color)
        brush.setStyle(__.SolidPattern)
        rect _ ?C...QRect(0, 0, painter.device().width(), painter.device().height())
        painter.fillRect(rect, brush)

        # Define our canvas.
        d_height _ painter.device().height() - (self._padding * 2)
        d_width _ painter.device().width() - (self._padding * 2)

        # Draw the bars.
        step_y _ d_height / self.n_steps
        bar_height _ step_y * self._y_solid_percent
        bar_height_space _ step_y * (1 - self._x_solid_percent) / 2

        step_x _ d_width / self.n_bars
        bar_width _ step_x * self._x_solid_percent
        bar_width_space _ step_x * (1 - self._y_solid_percent) / 2

        for b in range(self.n_bars):

            # Calculate the y-stop position for this bar, from the value in range.
            pc _ (self._values[b] - self._vmin) / (self._vmax - self._vmin)
            n_steps_to_draw _ int(pc * self.n_steps)

            for n in range(n_steps_to_draw):
                brush.sC..(?G...?C..(self.steps[n]))
                rect _ ?C...QRect(
                    self._padding + (step_x * b) + bar_width_space,
                    self._padding + d_height - ((1 + n) * step_y) + bar_height_space,
                    bar_width,
                    bar_height
                )
                painter.fillRect(rect, brush)

        painter.end()

    ___ sizeHint(self):
        r_ ?C...QSize(20, 120)

    ___ _trigger_refresh(self):
        self.update()

    ___ setDecay  f):
        self._decay _ float(f)

    ___ setDecayFrequencyMs  ms):
        __ self._timer:
            self._timer.stop()

        __ ms:
            self._timer _ ?C...?T..
            self._timer.setInterval(ms)
            self._timer.timeout.c..(self._decay_beat)
            self._timer.start()

    ___ _decay_beat(self):
        self._values _ [
            max(0, v - self._decay)
            for v in self._values
        ]
        self.update()  # Redraw new position.

    ___ setValues  v):
        self._values _ v
        self.update()

    ___ values(self):
        r_ self._values

    ___ setRange  vmin, vmax):
        assert float(vmin) < float(vmax)
        self._vmin, self._vmax _ float(vmin), float(vmax)

    ___ sC..  color):
        self.steps _ [color] * self._bar.n_steps
        self.update()

    ___ setColors  colors):
        self.n_steps _ le.(colors)
        self.steps _ colors
        self.update()


    ___ setBarPadding  i):
        self._padding _ int(i)
        self.update()


    ___ setBarSolidPercent  f):
        self._bar_solid_percent _ float(f)
        self.update()


    ___ setBackgroundColor  color):
        self._background_color _ ?G...?C..(color)
        self.update()

