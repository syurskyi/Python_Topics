______ sys
____ ? ______ ?W.. as qtw
____ ? ______ QtCore as qtc
____ ? ______ QtGui as qtg
____ collections ______ deque

# install via pip
____ psutil ______ cpu_percent
______ math

class GraphWidget(qtw.QWidget):
    """A widget to display a running graph of information"""

    crit_color _ qtg.QColor(255, 0, 0)  # red
    warn_color _ qtg.QColor(255, 255, 0)  # yellow
    good_color _ qtg.QColor(0, 255, 0)  # green

    ___ __init__(
        self, *args, data_width_20,
        minimum_0, maximum_100,
        warn_val_50, crit_val_75, scale_10,
        **kwargs
    ):
        super().__init__(*args, **kwargs)
        self.minimum _ minimum
        self.maximum _ maximum
        self.warn_val _ warn_val
        self.scale _ scale
        self.crit_val _ crit_val
        self.values _ deque([self.minimum] * data_width, maxlen_data_width)
        self.setFixedWidth(data_width * scale)

    ___ add_value(self, value):
        value _ max(value, self.minimum)
        value _ min(value, self.maximum)
        self.values.append(value)
        self.update()

    ___ val_to_y(self, value):
        data_range _ self.maximum - self.minimum
        value_fraction _ value / data_range
        y_offset _ round(value_fraction * self.height())
        y _ self.height() - y_offset
        return y

    ___ paintEvent(self, paint_event):
        painter _ qtg.QPainter(self)

        # draw the background
        brush _ qtg.QBrush(qtg.QColor(48, 48, 48))
        painter.setBrush(brush)
        painter.drawRect(0, 0, self.width(), self.height())

        # draw the boundary lines
        pen _ qtg.QPen()
        pen.setDashPattern([1, 0])

        # warning line
        warn_y _ self.val_to_y(self.warn_val)
        pen.setColor(self.warn_color)
        painter.setPen(pen)
        painter.drawLine(0, warn_y, self.width(), warn_y)

        # critical line
        crit_y _ self.val_to_y(self.crit_val)
        pen.setColor(self.crit_color)
        painter.setPen(pen)
        painter.drawLine(0, crit_y, self.width(), crit_y)

        # set up gradient brush
        gradient _ qtg.QLinearGradient(
            qtc.QPointF(0, self.height()), qtc.QPointF(0, 0))
        gradient.setColorAt(0, self.good_color)
        gradient.setColorAt(
            self.warn_val/(self.maximum - self.minimum),
            self.warn_color)
        gradient.setColorAt(
            self.crit_val/(self.maximum - self.minimum),
            self.crit_color)
        brush _ qtg.QBrush(gradient)
        painter.setBrush(brush)
        painter.setPen(qtc.Qt.NoPen)

        # Draw the paths for the chart
        self.start_value _ getattr(self, 'start_value', self.minimum)
        last_value _ self.start_value
        self.start_value _ self.values[0]
        for indx, value in enumerate(self.values):
            x _ (indx + 1) * self.scale
            last_x _ indx * self.scale
            y _ self.val_to_y(value)
            last_y _ self.val_to_y(last_value)
            path _ qtg.QPainterPath()
            path.moveTo(x, self.height())
            path.lineTo(last_x, self.height())
            path.lineTo(last_x, last_y)
            # Straight tops
            #path.lineTo(x, y)

            # Curvy tops
            c_x _ round(self.scale * .5) + last_x
            c1 _ (c_x, last_y)
            c2 _ (c_x, y)
            path.cubicTo(*c1, *c2, x, y)

            # Draw path
            painter.drawPath(path)
            last_value _ value


class MainWindow(qtw.QMainWindow):

    ___ __init__(self):
        """MainWindow constructor."""
        super().__init__()
        # Code starts here
        self.graph _ GraphWidget(self)
        self.setCentralWidget(self.graph)

        self.timer _ qtc.QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.c..(self.update_graph)
        self.timer.start()

        # Code ends here
        self.s..

    ___ update_graph(self):
        # If your CPU usage is too boring, try this:
        #import random
        #cpu_usage = random.randint(1, 100)
        cpu_usage _ cpu_percent()
        self.graph.add_value(cpu_usage)


if __name__ == '__main__':
    app _ qtw.?A..(sys.argv)
    # it's required to save a reference to MainWindow.
    # if it goes out of scope, it will be destroyed.
    mw _ MainWindow()
    sys.exit(app.exec())
