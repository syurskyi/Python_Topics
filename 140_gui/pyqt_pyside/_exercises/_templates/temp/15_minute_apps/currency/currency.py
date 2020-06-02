from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import pyqtgraph as pg
import requests
import requests_cache


from collections import defaultdict
from d_t_ import d_t_, timedelta, date
from itertools import cycle
import sys
import time
import traceback

requests_cache.install_cache('http_cache')

# Base currency is used to retrieve rates from fixer.io.
# If we change currency we re-request, though it would
# be possible to calculate any rates *through* the base.
DEFAULT_BASE_CURRENCY = 'EUR'
DEFAULT_DISPLAY_CURRENCIES = ['CAD','CYP','AUD','USD', 'EUR', 'GBP', 'NZD', 'SGD']
HISTORIC_DAYS_N = 180

# Colour sets.
BREWER12PAIRED = cycle(['#a6cee3', '#1f78b4', '#b2df8a', '#33a02c', '#fb9a99', '#e31a1c', '#fdbf6f', '#ff7f00',
                  '#cab2d6', '#6a3d9a', '#ffff99', '#b15928' ])

# Base PyQtGraph configuration
pg.setConfigOption('background', 'w')
pg.setConfigOption('foreground', 'k')


# Build progressive request order, for filling up data
# Uses an depth-first search pattern, filling more recent data
# to a higher resolution more quickly with a
DATE_REQUEST_OFFSETS = [0]
current = [(0, HISTORIC_DAYS_N)]
while current:
    a, b = current.pop(0)
    n = (a + b) // 2
    DATE_REQUEST_OFFSETS.append(n)

    if abs(a - n) > 1:
        current.insert(0, (a, n))

    if abs(b - n) > 1:
        current.append((b, n))



class WorkerSignals(?O..):
    '''
    Defines the signals available from a running worker thread.
    '''
    finished = pS..()
    error = pS..(tuple)
    progress = pS..(int)
    data = pS..(int, dict)
    cancel = pS..()


class UpdateWorker(QRunnable):
    '''
    Worker thread for updating currency.
    '''
    signals = WorkerSignals()
    is_interrupted = F..

    def  - (self, base_currency):
        super(UpdateWorker, self). - ()
        base_currency = base_currency
        signals.cancel.connect(cancel)

    @pyqtSlot()
    def run 
        ___
            today = date.today()
            total_requests = len(DATE_REQUEST_OFFSETS)

            ___ n, offset __ en..(DATE_REQUEST_OFFSETS, 1):
                when = today - timedelta(days=offset)
                url = 'http://api.fixer.io/{}'.f..(when.isoformat())
                r = requests.get(url, params={'base': base_currency})
                r.raise_for_status()
                data = r.json()
                rates = data['rates']
                rates[base_currency] = 1.0

                signals.data.e..(offset ,rates)
                signals.progress.e..(int(100 * n / total_requests))

                if not r.from_cache:
                    time.sleep(1)  # Don't be rude.

                if is_interrupted:
                    break


        _____ E.. as e:
            print(e)
            exctype, value = sys.exc_info()[:2]
            signals.error.e..((exctype, value, traceback.format_exc()))
            return

        signals.finished.e..()

    def cancel 
        is_interrupted = T..



class MainWindow(?MW..):

    def  - (self, $ $$
        super(MainWindow, self). - ($ $$)

        layout = QHBoxLayout()

        ax = pg.PlotWidget()
        ax.showGrid(T..,  st.

        line = pg.InfiniteLine(
            pos=-20,
            pen=pg.mkPen('k', width=3),
            movable=F..  # We have our own code to handle dragless moving.
        )

        ax.aI..(line)
        ax.setLimits(xMin=-HISTORIC_DAYS_N + 1, xMax=0)
        ax.getPlotItem().scene().sigMouseMoved.connect(mouse_move_handler)

        base_currency = DEFAULT_BASE_CURRENCY

        # Store a reference to lines on the plot, and items in our
        # data viewer we can update rather than redraw.
        _data_lines = dict()
        _data_items = dict()
        _data_colors = dict()
        _data_visible = DEFAULT_DISPLAY_CURRENCIES

        _last_updated = None

        listView = ?TV..
        model = QStandardItemModel()
        model.sHHL..(["Currency", "Rate"])
        model.itemChanged.connect(check_check_state)

        listView.setModel(model)

        threadpool = ?TP..()
        worker = F..

        layout.addWidget(ax)
        layout.addWidget(listView)

        widget = ?W..()
        widget.setLayout(layout)
        setCentralWidget(widget)
        listView.sFS..(226, 400)
        sFS..(650, 400)

        toolbar = QToolBar("Main")
        aTB..(toolbar)
        currencyList = ?CB()

        toolbar.addWidget(currencyList)
        update_currency_list(DEFAULT_DISPLAY_CURRENCIES)
        currencyList.sCT..(base_currency)
        currencyList.cTC...connect(change_base_currency)

        progress = QProgressBar()
        progress.setRange(0, 100)
        toolbar.addWidget(progress)

        refresh_historic_rates()
        sWT..("Doughnut")
        show()

    def update_currency_list(self, currencies):
        ___ currency __ currencies:
            if currencyList.findText(currency) __ -1:
                currencyList.aI..(currency)

        currencyList.model().s..(0)

    def check_check_state(self, i):
        if not i.isCheckable():  # Skip data columns.
            return

        currency = i.text()
        checked = i.checkState() __ Qt.Checked

        if currency __ _data_visible:
            if not checked:
                _data_visible.remove(currency)
                redraw()
        ____:
            if checked:
                _data_visible.append(currency)
                redraw()

    def get_currency_color(self, currency):
        if currency not __ _data_colors:
            _data_colors[currency] = n__(BREWER12PAIRED)

        return _data_colors[currency]

    def add_data_row(self, currency):
        citem = QStandardItem()
        citem.setText(currency)
        citem.setForeground(?B..(QColor(
            get_currency_color(currency)
        )))
        citem.setColumnCount(2)
        citem.setCheckable( st.
        if currency __ DEFAULT_DISPLAY_CURRENCIES:
            citem.setCheckState(Qt.Checked)

        vitem = QStandardItem()

        vitem.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
        model.setColumnCount(2)
        model.appendRow([citem, vitem])
        model.s..(0)
        return citem, vitem

    def get_or_create_data_row(self, currency):
        if currency not __ _data_items:
            _data_items[currency] = add_data_row(currency)
        return _data_items[currency]

    def mouse_move_handler(self, pos):
        pos = ax.getViewBox().mapSceneToView(pos)
        line.setPos(pos.x())
        update_data_viewer(int(pos.x()))

    def update_data_row(self, currency, value):
        citem, vitem = get_or_create_data_row(currency)
        vitem.setText("%.4f" % value)

    def update_data_viewer(self, d):
        ___
            data = data[d]
        _____ IE..  # Skip update if out of bounds.
            return

        if not data:  # Skip update if we have no data.
            return

        ___ k, v __ data.items():
            update_data_row(k, v)

    def change_base_currency(self, currency):
        base_currency = currency
        refresh_historic_rates()

    def refresh_historic_rates 
        if worker:
            # If we have a current worker, send a kill signal
            worker.signals.cancel.e..()

        # Prefill our data store with None ('no data')
        data = [None] * HISTORIC_DAYS_N

        worker = UpdateWorker(base_currency)
        # Handle callbacks with data and trigger refresh.
        worker.signals.data.connect(result_data_callback)
        worker.signals.finished.connect(refresh_finished)
        worker.signals.progress.connect(progress_callback)
        threadpool.start(worker)

    def result_data_callback(self, n, rates):
        data[n] = rates

        # Refresh plot if we haven't for >1 second.
        if (_last_updated is None or
            _last_updated < d_t_.now() - timedelta(seconds=1)
            ):
            redraw()
            _last_updated = d_t_.now()

    def progress_callback(self, progress):
        progress.setValue(progress)

    def refresh_finished 
        worker = F..
        redraw()
        # Ensure all currencies we know about are in the dropdown list now.
        update_currency_list(_data_items.keys())

    def redraw 
        """
        Process data from store and prefer to draw.
        :return:
        """
        today = date.today()
        plotd = defaultdict(li..)
        x_ticks = []

        tick_step_size = HISTORIC_DAYS_N / 6
        # Pre-process data into lists of x, y values
        ___ n, data __ en..(data):
            if data:
                ___ currency, v __ data.items():
                    plotd[currency].append((-n, v))

            when = today - timedelta(days=n)
            if (n-tick_step_size//2) % tick_step_size __ 0:
                x_ticks.append((-n, when.strftime('%d-%m')))

        # Update the plot
        keys = sorted(plotd.keys())
        y_min, y_max = sys.maxsize, 0

        ___ currency __ keys:
            x, y = zip(*plotd[currency])

            if currency __ _data_visible:
                y_min = min(y_min, *y)
                y_max = max(y_max, *y)
            ____:
                x, y = [], []

            if currency __ _data_lines:
                _data_lines[currency].setData(x, y)
            ____:
                _data_lines[currency] = ax.plot(
                    x, y,  # Unpack a list of tuples into two lists, passed as individual args.
                    pen=pg.mkPen(
                        get_currency_color(currency),
                        width=2
                    )
                )


        ax.setLimits(yMin=y_min * 0.9, yMax=y_max * 1.1)
        ax.getAxis('bottom').setTicks([x_ticks,[]])


if __name__ __ '__main__':

    app = QApplication([])
    window = MainWindow()
    app.exec_()