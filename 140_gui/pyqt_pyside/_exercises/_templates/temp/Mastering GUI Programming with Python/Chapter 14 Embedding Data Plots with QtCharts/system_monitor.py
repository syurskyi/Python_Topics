______ ___
____ ? ______ ?W.. __ qtw
____ ? ______ ?G.. __ qtg
____ ? ______ ?C.. __ qtc
____ ? ______ QtChart __ qtch

____ collections ______ deque
______ psutil


c_ DiskUsageChartView(qtch.QChartView):

    chart_title _ 'Disk Usage by Partition'

    ___  -
        s_. - ()
        # Create chart
        chart _ qtch.QChart(title_self.chart_title)
        setChart(chart)

        # Create series
        series _ qtch.QBarSeries()
        chart.addSeries(series)

        # add bar sets
        bar_set _ qtch.QBarSet('Percent Used')
        series.ap..(bar_set)

        # Get the data
        partitions _   # list
        ___ part __ psutil.disk_partitions
            __ 'rw' __ part.opts.split(','):
                partitions.ap..(part.device)
                usage _ psutil.disk_usage(part.mountpoint).percent
                bar_set.ap..(usage)

        # Create Axis
        x_axis _ qtch.QBarCategoryAxis()
        x_axis.ap..(partitions)
        chart.setAxisX(x_axis)
        series.attachAxis(x_axis)
        y_axis _ qtch.QValueAxis()
        y_axis.setRange(0, 100)
        chart.setAxisY(y_axis)
        series.attachAxis(y_axis)

        # Add labels
        series.setLabelsVisible(True)


c_ CPUUsageView(qtch.QChartView):

    num_data_points _ 500
    chart_title _ "CPU Utilization"

    ___  -
        s_. - ()

        # create chart
        chart _ qtch.QChart(title_self.chart_title)
        setChart(chart)

        # series
        series _ qtch.QSplineSeries(name_"Percentage")
        chart.addSeries(series)

        # Create data container
        data _ deque(
            [0] * num_data_points, maxlen_self.num_data_points)
        series.ap..([
            qtc.QPoint(x, y)
            ___ x, y __ en..(data)
        ])

        # CPU Axes
        x_axis _ qtch.QValueAxis()
        x_axis.setRange(0, num_data_points)
        x_axis.setLabelsVisible F..
        y_axis _ qtch.QValueAxis()
        y_axis.setRange(0, 100)
        chart.setAxisX(x_axis, series)
        chart.setAxisY(y_axis, series)

        # Appearance tweaks
        setRenderHint(qtg.QPainter.Antialiasing)

        # configure timer
        timer _ qtc.QTimer(
            interval_200, timeout_self.refresh_stats)
        timer.start()

    ___ refresh_stats
        usage _ psutil.cpu_percent()
        data.ap..(usage)
        new_data _ [
            qtc.QPoint(x, y)
            ___ x, y __ en..(data)]
        series.replace(new_data)

    ___ keyPressEvent  event):
        keymap _ {
            qtc.__.Key_Up: lambda: chart().scroll(0, -10),
            qtc.__.Key_Down: lambda: chart().scroll(0, 10),
            qtc.__.Key_Right: lambda: chart().scroll(-10, 0),
            qtc.__.Key_Left: lambda: chart().scroll(10, 0),
            qtc.__.Key_Greater: chart().zoomIn,
            qtc.__.Key_Less: chart().zoomOut,
        }
        callback _ keymap.g..(event.key())
        __ callback:
            callback()


c_ MemoryChartView(qtch.QChartView):

    chart_title _ "Memory Usage"
    num_data_points _ 50

    ___  -
        s_. - ()

        ################
        # Create Chart #
        ################

        # Create qchart object
        chart _ qtch.QChart(title_self.chart_title)
        setChart(chart)

        # Setup series
        series _ qtch.QStackedBarSeries()
        chart.addSeries(series)
        phys_set _ qtch.QBarSet("Physical")
        swap_set _ qtch.QBarSet("Swap")
        series.ap..(phys_set)
        series.ap..(swap_set)

        # Setup Data
        data _ deque(
            [(0, 0)] * num_data_points,
            maxlen_self.num_data_points)
        ___ phys, swap __ data:
            phys_set.ap..(phys)
            swap_set.ap..(swap)

        # Setup Axes
        x_axis _ qtch.QValueAxis()
        x_axis.setRange(0, num_data_points)
        x_axis.setLabelsVisible F..
        y_axis _ qtch.QValueAxis()
        y_axis.setRange(0, 100)
        chart.setAxisX(x_axis, series)
        chart.setAxisY(y_axis, series)

        # Start refresh timer
        timer _ qtc.QTimer(
            interval_1000, timeout_self.refresh_stats)
        timer.start()

        ###################
        # Style the chart #
        ###################
        chart.setAnimationOptions(qtch.QChart.AllAnimations)

        chart.setAnimationEasingCurve(
            qtc.QEasingCurve(qtc.QEasingCurve.OutBounce))
        chart.setAnimationDuration(1000)

        # Add shadow around the chart area
        chart.setDropShadowEnabled(True)

        # Set the theme
        chart.setTheme(qtch.QChart.ChartThemeBrownSand)

        # Configure a background brush
        gradient _ qtg.QLinearGradient(
            chart.plotArea().topLeft(), chart.plotArea().bottomRight())
        gradient.setColorAt(0, qtg.?C..("#333"))
        gradient.setColorAt(1, qtg.?C..("#660"))
        chart.setBackgroundBrush(qtg.QBrush(gradient))

        # Background Pen draws a border around the chart
        chart.setBackgroundPen(qtg.QPen(qtg.?C..('black'), 5))

        # Set title font and brush
        chart.setTitleBrush(
            qtg.QBrush(qtc.__.white))
        chart.setTitleFont(qtg.QFont('Impact', 32, qtg.QFont.Bold))

        # Set axes fonts and brushes
        axis_font _ qtg.QFont('Mono', 16)
        axis_brush _ qtg.QBrush(qtg.?C..('#EEF'))
        y_axis.setLabelsFont(axis_font)
        y_axis.setLabelsBrush(axis_brush)

        # Grid lines
        grid_pen _ qtg.QPen(qtg.?C..('silver'))
        grid_pen.setDashPattern([1, 1, 0, 1])
        x_axis.setGridLinePen(grid_pen)
        y_axis.setGridLinePen(grid_pen)
        y_axis.setTickCount(11)

        #Shades
        y_axis.setShadesVisible(True)
        y_axis.setShadesColor(qtg.?C..('#884'))

        # Styling the legend
        legend _ chart.legend()

        # Background
        legend.setBackgroundVisible(True)
        legend.setBrush(
            qtg.QBrush(qtg.?C..('white')))

        # Font
        legend.setFont(qtg.QFont('Courier', 14))
        legend.setLabelColor(qtc.__.darkRed)

        # Markers
        legend.setMarkerShape(qtch.QLegend.MarkerShapeCircle)


    ___ refresh_stats
        phys _ psutil.virtual_memory()
        swap _ psutil.swap_memory()
        total_mem _ phys.total + swap.total
        phys_pct _ (phys.used / total_mem) * 100
        swap_pct _ (swap.used / total_mem) * 100

        data.ap..(
            (phys_pct, swap_pct))
        ___ x, (phys, swap) __ en..(data):
            phys_set.replace(x, phys)
            swap_set.replace(x, swap)


c_ MainWindow(qtw.QMainWindow):

    ___  -
        """MainWindow constructor.

        This widget will be our main window.
        We'll define all the UI components in here.
        """
        s_. - ()
        # Main UI code goes here
        tabs _ qtw.QTabWidget()
        sCW..(tabs)

        #########################################
        # Partition Usage as a static bar chart #
        #########################################

        disk_usage_view _ DiskUsageChartView()
        tabs.addTab(disk_usage_view, "Disk Usage")

        #############################
        # CPU usage as a line chart #
        #############################

        cpu_view _ CPUUsageView()
        tabs.addTab(cpu_view, "CPU Usage")

        #####################################
        # CPU Time Percent as a stacked bar #
        #####################################
        cpu_time_view _ MemoryChartView()
        tabs.addTab(cpu_time_view, "Memory Usage")

        # End main UI code
        s..



__ ______ __ ______
    app _ qtw.?A..(___.a..
    # it's required to save a reference to MainWindow.
    # if it goes out of scope, it will be destroyed.
    mw _ MainWindow()
    ___.e..(app.e..
