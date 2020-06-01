______ sys
____ ? ______ ?W.. as qtw
____ ? ______ QtGui as qtg
____ ? ______ QtCore as qtc
____ ? ______ QtChart as qtch

____ collections ______ deque
______ psutil


class DiskUsageChartView(qtch.QChartView):

    chart_title _ 'Disk Usage by Partition'

    ___ __init__(self):
        super().__init__()
        # Create chart
        chart _ qtch.QChart(title_self.chart_title)
        self.setChart(chart)

        # Create series
        series _ qtch.QBarSeries()
        chart.addSeries(series)

        # add bar sets
        bar_set _ qtch.QBarSet('Percent Used')
        series.append(bar_set)

        # Get the data
        partitions _ []
        for part in psutil.disk_partitions
            if 'rw' in part.opts.split(','):
                partitions.append(part.device)
                usage _ psutil.disk_usage(part.mountpoint).percent
                bar_set.append(usage)

        # Create Axis
        x_axis _ qtch.QBarCategoryAxis()
        x_axis.append(partitions)
        chart.setAxisX(x_axis)
        series.attachAxis(x_axis)
        y_axis _ qtch.QValueAxis()
        y_axis.setRange(0, 100)
        chart.setAxisY(y_axis)
        series.attachAxis(y_axis)

        # Add labels
        series.setLabelsVisible(True)


class CPUUsageView(qtch.QChartView):

    num_data_points _ 500
    chart_title _ "CPU Utilization"

    ___ __init__(self):
        super().__init__()

        # create chart
        chart _ qtch.QChart(title_self.chart_title)
        self.setChart(chart)

        # series
        self.series _ qtch.QSplineSeries(name_"Percentage")
        chart.addSeries(self.series)

        # Create data container
        self.data _ deque(
            [0] * self.num_data_points, maxlen_self.num_data_points)
        self.series.append([
            qtc.QPoint(x, y)
            for x, y in enumerate(self.data)
        ])

        # CPU Axes
        x_axis _ qtch.QValueAxis()
        x_axis.setRange(0, self.num_data_points)
        x_axis.setLabelsVisible(False)
        y_axis _ qtch.QValueAxis()
        y_axis.setRange(0, 100)
        chart.setAxisX(x_axis, self.series)
        chart.setAxisY(y_axis, self.series)

        # Appearance tweaks
        self.setRenderHint(qtg.QPainter.Antialiasing)

        # configure timer
        self.timer _ qtc.QTimer(
            interval_200, timeout_self.refresh_stats)
        self.timer.start()

    ___ refresh_stats(self):
        usage _ psutil.cpu_percent()
        self.data.append(usage)
        new_data _ [
            qtc.QPoint(x, y)
            for x, y in enumerate(self.data)]
        self.series.replace(new_data)

    ___ keyPressEvent(self, event):
        keymap _ {
            qtc.Qt.Key_Up: lambda: self.chart().scroll(0, -10),
            qtc.Qt.Key_Down: lambda: self.chart().scroll(0, 10),
            qtc.Qt.Key_Right: lambda: self.chart().scroll(-10, 0),
            qtc.Qt.Key_Left: lambda: self.chart().scroll(10, 0),
            qtc.Qt.Key_Greater: self.chart().zoomIn,
            qtc.Qt.Key_Less: self.chart().zoomOut,
        }
        callback _ keymap.get(event.key())
        if callback:
            callback()


class MemoryChartView(qtch.QChartView):

    chart_title _ "Memory Usage"
    num_data_points _ 50

    ___ __init__(self):
        super().__init__()

        ################
        # Create Chart #
        ################

        # Create qchart object
        chart _ qtch.QChart(title_self.chart_title)
        self.setChart(chart)

        # Setup series
        series _ qtch.QStackedBarSeries()
        chart.addSeries(series)
        self.phys_set _ qtch.QBarSet("Physical")
        self.swap_set _ qtch.QBarSet("Swap")
        series.append(self.phys_set)
        series.append(self.swap_set)

        # Setup Data
        self.data _ deque(
            [(0, 0)] * self.num_data_points,
            maxlen_self.num_data_points)
        for phys, swap in self.data:
            self.phys_set.append(phys)
            self.swap_set.append(swap)

        # Setup Axes
        x_axis _ qtch.QValueAxis()
        x_axis.setRange(0, self.num_data_points)
        x_axis.setLabelsVisible(False)
        y_axis _ qtch.QValueAxis()
        y_axis.setRange(0, 100)
        chart.setAxisX(x_axis, series)
        chart.setAxisY(y_axis, series)

        # Start refresh timer
        self.timer _ qtc.QTimer(
            interval_1000, timeout_self.refresh_stats)
        self.timer.start()

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
        gradient.setColorAt(0, qtg.QColor("#333"))
        gradient.setColorAt(1, qtg.QColor("#660"))
        chart.setBackgroundBrush(qtg.QBrush(gradient))

        # Background Pen draws a border around the chart
        chart.setBackgroundPen(qtg.QPen(qtg.QColor('black'), 5))

        # Set title font and brush
        chart.setTitleBrush(
            qtg.QBrush(qtc.Qt.white))
        chart.setTitleFont(qtg.QFont('Impact', 32, qtg.QFont.Bold))

        # Set axes fonts and brushes
        axis_font _ qtg.QFont('Mono', 16)
        axis_brush _ qtg.QBrush(qtg.QColor('#EEF'))
        y_axis.setLabelsFont(axis_font)
        y_axis.setLabelsBrush(axis_brush)

        # Grid lines
        grid_pen _ qtg.QPen(qtg.QColor('silver'))
        grid_pen.setDashPattern([1, 1, 0, 1])
        x_axis.setGridLinePen(grid_pen)
        y_axis.setGridLinePen(grid_pen)
        y_axis.setTickCount(11)

        #Shades
        y_axis.setShadesVisible(True)
        y_axis.setShadesColor(qtg.QColor('#884'))

        # Styling the legend
        legend _ chart.legend()

        # Background
        legend.setBackgroundVisible(True)
        legend.setBrush(
            qtg.QBrush(qtg.QColor('white')))

        # Font
        legend.setFont(qtg.QFont('Courier', 14))
        legend.setLabelColor(qtc.Qt.darkRed)

        # Markers
        legend.setMarkerShape(qtch.QLegend.MarkerShapeCircle)


    ___ refresh_stats(self):
        phys _ psutil.virtual_memory()
        swap _ psutil.swap_memory()
        total_mem _ phys.total + swap.total
        phys_pct _ (phys.used / total_mem) * 100
        swap_pct _ (swap.used / total_mem) * 100

        self.data.append(
            (phys_pct, swap_pct))
        for x, (phys, swap) in enumerate(self.data):
            self.phys_set.replace(x, phys)
            self.swap_set.replace(x, swap)


class MainWindow(qtw.QMainWindow):

    ___ __init__(self):
        """MainWindow constructor.

        This widget will be our main window.
        We'll define all the UI components in here.
        """
        super().__init__()
        # Main UI code goes here
        tabs _ qtw.QTabWidget()
        self.setCentralWidget(tabs)

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
        self.s..



if __name__ == '__main__':
    app _ qtw.?A..(sys.argv)
    # it's required to save a reference to MainWindow.
    # if it goes out of scope, it will be destroyed.
    mw _ MainWindow()
    sys.exit(app.exec())
