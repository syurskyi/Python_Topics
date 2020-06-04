______ ___
____ ? ______ ?W.. __ qtw
____ ? ______ ?C.. __ qtc
____ ? ______ ?G.. __ qtg
____ collections ______ deque

# install via pip
____ psutil ______ cpu_percent
______ m__

c_ GraphWidget ?.?W..
    """A widget to display a running graph of information"""

    crit_color _ qtg.?C..(255, 0, 0)  # red
    warn_color _ qtg.?C..(255, 255, 0)  # yellow
    good_color _ qtg.?C..(0, 255, 0)  # green

    ___  - (
        self, $ data_width_20,
        minimum_0, maximum_100,
        warn_val_50, crit_val_75, scale_10,
        $$
    ):
        s_. - ($ $$)
        minimum _ minimum
        maximum _ maximum
        warn_val _ warn_val
        scale _ scale
        crit_val _ crit_val
        values _ deque([minimum] * data_width, maxlen_data_width)
        sFW..(data_width * scale)

    ___ add_value  value):
        value _ max(value, minimum)
        value _ min(value, maximum)
        values.ap..(value)
        update()

    ___ val_to_y  value):
        data_range _ maximum - minimum
        value_fraction _ value / data_range
        y_offset _ round(value_fraction * height())
        y _ height() - y_offset
        r_ y

    ___ paintEvent  paint_event):
        painter _ qtg.QPainter

        # draw the background
        brush _ qtg.?B..(qtg.?C..(48, 48, 48))
        painter.sB..(brush)
        painter.drawRect(0, 0, width(), height())

        # draw the boundary lines
        pen _ qtg.?P..()
        pen.setDashPattern([1, 0])

        # warning line
        warn_y _ val_to_y(warn_val)
        pen.sC..(warn_color)
        painter.sP..(pen)
        painter.drawLine(0, warn_y, width(), warn_y)

        # critical line
        crit_y _ val_to_y(crit_val)
        pen.sC..(crit_color)
        painter.sP..(pen)
        painter.drawLine(0, crit_y, width(), crit_y)

        # set up gradient brush
        gradient _ qtg.QLinearGradient(
            qtc.QPointF(0, height()), qtc.QPointF(0, 0))
        gradient.setColorAt(0, good_color)
        gradient.setColorAt(
            warn_val/(maximum - minimum),
            warn_color)
        gradient.setColorAt(
            crit_val/(maximum - minimum),
            crit_color)
        brush _ qtg.?B..(gradient)
        painter.sB..(brush)
        painter.sP..(qtc.__.NoPen)

        # Draw the paths for the chart
        start_value _ getattr  'start_value', minimum)
        last_value _ start_value
        start_value _ values[0]
        ___ indx, value __ en..(values):
            x _ (indx + 1) * scale
            last_x _ indx * scale
            y _ val_to_y(value)
            last_y _ val_to_y(last_value)
            pa__ _ qtg.QPainterPath()
            pa__.moveTo(x, height())
            pa__.lineTo(last_x, height())
            pa__.lineTo(last_x, last_y)
            # Straight tops
            #path.lineTo(x, y)

            # Curvy tops
            c_x _ round(scale * .5) + last_x
            c1 _ (c_x, last_y)
            c2 _ (c_x, y)
            pa__.cubicTo(*c1, *c2, x, y)

            # Draw path
            painter.drawPath(pa__)
            last_value _ value


c_ MainWindow(qtw.?MW..):

    ___  -
        """MainWindow constructor."""
        s_. - ()
        # Code starts here
        graph _ GraphWidget
        sCW..(graph)

        timer _ qtc.?T..
        timer.sI..(1000)
        timer.timeout.c..(update_graph)
        timer.start()

        # Code ends here
        s..

    ___ update_graph
        # If your CPU usage is too boring, try this:
        #import random
        #cpu_usage = random.randint(1, 100)
        cpu_usage _ cpu_percent()
        graph.add_value(cpu_usage)


__ ______ __ ______
    app _ qtw.?A..(___.a..
    # it's required to save a reference to MainWindow.
    # if it goes out of scope, it will be destroyed.
    mw _ MainWindow()
    ___.e.. ?.e..
