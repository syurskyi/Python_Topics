import os
import sys
import time
import socket
import traceback

from PySide2.QtCore import QObject, QThread, Signal, Slot
from PySide2.QtWidgets import QApplication, QMessageBox

from . import g
from .version import VERSION
from .resources import Resources
from .loggers import ConsoleLogger
from .config import get_config_var
from .gui.darkpalette import DarkPalette
from .gui.mainwindow import MainWindow


class BackgroundJob(QObject):

    finished = Signal()
    crashed = Signal(str)

    def __init__(self):
        super().__init__()
        self.exit_requested = False

    @Slot()
    def start(self):
        try:
            self.run()
        except Exception:
            self.crashed.emit(traceback.format_exc())

    @Slot()
    def stop(self):
        self.exit_requested = True

    def run(self):
        g.log.info('ThisApplication v%s | %s | %s' % (VERSION, time.strftime('%r | %A, %B %d, %Y'), socket.gethostname()))
        g.log.debug('Running from %s%s' % (sys.executable, ' (frozen)' if hasattr(sys, 'frozen') else ''))

        testvar_value = get_config_var('testvar', 'hardcoded fallback')
        message_value = get_config_var('message', '')
        g.log.info('- THISAPPLICATION_TESTVAR: %s' % testvar_value)
        g.log.info("- message: '%s'" % message_value)

        i = 0
        while not self.exit_requested:
            i += 1
            if i < 5:
                g.log.info('I am doing work in the background!')
            elif i == 5:
                g.log.warning('Help! I\'m about to crash!')
            else:
                raise RuntimeError('Oh no! A crash!')
            time.sleep(2.0)

        self.finished.emit()


class MainApplication(QApplication):

    def __init__(self, argv):
        super().__init__(argv)

        self.setApplicationName('ThisApplication')
        self.setStyle('Fusion')
        self.setPalette(DarkPalette())
        self.setStyleSheet("""
            QPushButton::disabled {
                background-color: #303030;
                color: #2e2e2e;
            }
        """)

        self.log = ConsoleLogger.new(__name__)
        self.r = Resources()
        g.init(self.log, self.r)

        self.main = MainWindow()
        self.main.setWindowIcon(self.r.iconApp)
        self.main.show()

        self.exceptionDialog = None
        sys.excepthook = self.handleGlobalException

        self.thread = QThread()
        self.job = BackgroundJob()
        if True:
            self.job.crashed.connect(self.onThreadCrash)
            self.job.moveToThread(self.thread)
            self.job.finished.connect(self.thread.quit)
            self.thread.started.connect(self.job.start)
            self.thread.finished.connect(self.quit)
            self.aboutToQuit.connect(self.onUserQuit)
            self.thread.start()
        else:
            self.job.run()

    def onUserQuit(self):
        if self.thread and self.job:
            self.job.stop()
            self.thread.quit()
            self.thread.wait()

    def onThreadCrash(self, s):
        lines = ['A problem has occurred and this application must exit.', '']
        g.log.critical('>>> ENCOUNTERED AN UNHANDLED EXCEPTION IN WORKER THREAD!')
        for line in s.splitlines():
            g.log.critical(line)
            lines.append(line)
        g.log.critical('>>> THIS ERROR IS FATAL. THE APPLICATION MUST BE RESTARTED.')
        lines.append('')
        lines.append('Please copy and paste the text from this message box to report the issue.')

        QMessageBox.critical(None, 'Error', '\n'.join(lines))
        self.exit(1)

    @staticmethod
    def handleGlobalException(exc_type, exc_val, exc_tb):
        lines = ['A problem has occurred and this application must exit.', '']
        g.log.critical('>>> ENCOUNTERED AN UNHANDLED APPLICATION EXCEPTION!')
        for exc_line in traceback.format_exception(exc_type, exc_val, exc_tb):
            for line in exc_line.splitlines():
                g.log.critical(line)
                lines.append(line)
        g.log.critical('>>> THIS ERROR MAY BE FATAL. THE APPLICATION MAY NOT WORK AS EXPECTED UNTIL RESTARTED.')
        lines.append('')
        lines.append('Please copy and paste the text from this message box to report the issue.')

        QMessageBox.critical(None, 'Error', '\n'.join(lines))

    @classmethod
    def run(cls):
        app = cls(sys.argv)
        result = app.exec_()
        sys.exit(result)
