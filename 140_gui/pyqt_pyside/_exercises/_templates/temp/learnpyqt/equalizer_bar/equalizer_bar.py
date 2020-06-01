______ sys
if 'PyQt5' in sys.modules:
    ____ ? ______ QtCore, QtGui, ?W..
    ____ ?.QtCore ______ Qt
    ____ ?.QtCore ______ pyqtSignal as Signal

else:
    ____ PySide2 ______ QtCore, QtGui, ?W..
    ____ PySide2.QtCore ______ Qt
    ____ PySide2.QtCore ______ Signal


class EqualizerBar(?W...QWidget):

    ___ __init__(self, bars, steps, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setSizePolicy(
            ?W...QSizePolicy.MinimumExpanding,
            ?W...QSizePolicy.MinimumExpanding
        )

        if isinstance(steps, list):
            # list of colours.
            self.n_steps _ len(steps)
            self.steps _ steps

        elif isinstance(steps, int):
            # int number of bars, defaults to red.
            self.n_steps _ steps
            self.steps _ ['red'] * steps

        else:
            raise TypeError('steps must be a list or int')

        # Bar appearance.
        self.n_bars _ bars
        self._x_solid_percent _ 0.8
        self._y_solid_percent _ 0.8
        self._background_color _ QtGui.QColor('black')
        self._padding _ 25  # n-pixel gap around edge.

        # Bar behaviour
        self._timer _ None
        self.setDecayFrequencyMs(100)
        self._decay _ 10

        # Ranges
        self._vmin _ 0
        self._vmax _ 100

        # Current values are stored in a list.
        self._values _ [0.0] * bars


    ___ paintEvent(self, e):
        painter _ QtGui.QPainter(self)

        brush _ QtGui.QBrush()
        brush.setColor(self._background_color)
        brush.setStyle(Qt.SolidPattern)
        rect _ QtCore.QRect(0, 0, painter.device().width(), painter.device().height())
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
                brush.setColor(QtGui.QColor(self.steps[n]))
                rect _ QtCore.QRect(
                    self._padding + (step_x * b) + bar_width_space,
                    self._padding + d_height - ((1 + n) * step_y) + bar_height_space,
                    bar_width,
                    bar_height
                )
                painter.fillRect(rect, brush)

        painter.end()

    ___ sizeHint(self):
        return QtCore.QSize(20, 120)

    ___ _trigger_refresh(self):
        self.update()

    ___ setDecay(self, f):
        self._decay _ float(f)

    ___ setDecayFrequencyMs(self, ms):
        if self._timer:
            self._timer.stop()

        if ms:
            self._timer _ QtCore.QTimer()
            self._timer.setInterval(ms)
            self._timer.timeout.c..(self._decay_beat)
            self._timer.start()

    ___ _decay_beat(self):
        self._values _ [
            max(0, v - self._decay)
            for v in self._values
        ]
        self.update()  # Redraw new position.

    ___ setValues(self, v):
        self._values _ v
        self.update()

    ___ values(self):
        return self._values

    ___ setRange(self, vmin, vmax):
        assert float(vmin) < float(vmax)
        self._vmin, self._vmax _ float(vmin), float(vmax)

    ___ setColor(self, color):
        self.steps _ [color] * self._bar.n_steps
        self.update()

    ___ setColors(self, colors):
        self.n_steps _ len(colors)
        self.steps _ colors
        self.update()


    ___ setBarPadding(self, i):
        self._padding _ int(i)
        self.update()


    ___ setBarSolidPercent(self, f):
        self._bar_solid_percent _ float(f)
        self.update()


    ___ setBackgroundColor(self, color):
        self._background_color _ QtGui.QColor(color)
        self.update()

