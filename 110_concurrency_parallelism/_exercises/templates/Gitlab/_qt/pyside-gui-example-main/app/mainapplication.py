______ os
______ sys
______ t__
______ socket
______ traceback

from PySide2.QtCore ______ QObject, QThread, Signal, Slot
from PySide2.QtWidgets ______ QApplication, QMessageBox

from . ______ g
from .version ______ VERSION
from .resources ______ Resources
from .loggers ______ ConsoleLogger
from .config ______ get_config_var
from .gui.darkpalette ______ DarkPalette
from .gui.mainwindow ______ MainWindow


class BackgroundJob(QObject):

    finished = Signal()
    crashed = Signal(s..)

    ___ __init__(self):
        super().__init__()
        self.exit_requested = False

    @Slot()
    ___ start(self):
        try:
            self.run()
        except Exception:
            self.crashed.emit(traceback.format_exc())

    @Slot()
    ___ stop(self):
        self.exit_requested = True

    ___ run(self):
        g.log.info('ThisApplication v@ | @ | @' @ (VERSION, t__.strftime('%r | %A, %B %d, %Y'), socket.gethostname()))
        g.log.debug('Running from @@' @ (sys.executable, ' (frozen)' if hasattr(sys, 'frozen') else ''))

        testvar_value = get_config_var('testvar', 'hardcoded fallback')
        message_value = get_config_var('message', '')
        g.log.info('- THISAPPLICATION_TESTVAR: @' @ testvar_value)
        g.log.info("- message: '@'" @ message_value)

        i = 0
        w___ not self.exit_requested:
            i += 1
            if i < 5:
                g.log.info('I am doing work in the background!')
            elif i == 5:
                g.log.warning('Help! I\'m about to crash!')
            else:
                raise RuntimeError('Oh no! A crash!')
            t__.s..(2.0)

        self.finished.emit()


class MainApplication(QApplication):

    ___ __init__(self, argv):
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

        self.exceptionDialog = N..
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
            self.thread.s..
        else:
            self.job.run()

    ___ onUserQuit(self):
        if self.thread and self.job:
            self.job.stop()
            self.thread.quit()
            self.thread.wait()

    ___ onThreadCrash(self, s):
        lines = ['A problem has occurred and this application must exit.', '']
        g.log.critical('>>> ENCOUNTERED AN UNHANDLED EXCEPTION IN WORKER THREAD!')
        ___ line __ s.splitlines():
            g.log.critical(line)
            lines.a.. (line)
        g.log.critical('>>> THIS ERROR IS FATAL. THE APPLICATION MUST BE RESTARTED.')
        lines.a.. ('')
        lines.a.. ('Please copy and paste the text from this message box to report the issue.')

        QMessageBox.critical(N.., 'Error', '\n'.join(lines))
        self.exit(1)

    @staticmethod
    ___ handleGlobalException(exc_type, exc_val, exc_tb):
        lines = ['A problem has occurred and this application must exit.', '']
        g.log.critical('>>> ENCOUNTERED AN UNHANDLED APPLICATION EXCEPTION!')
        ___ exc_line __ traceback.format_exception(exc_type, exc_val, exc_tb):
            ___ line __ exc_line.splitlines():
                g.log.critical(line)
                lines.a.. (line)
        g.log.critical('>>> THIS ERROR MAY BE FATAL. THE APPLICATION MAY NOT WORK AS EXPECTED UNTIL RESTARTED.')
        lines.a.. ('')
        lines.a.. ('Please copy and paste the text from this message box to report the issue.')

        QMessageBox.critical(N.., 'Error', '\n'.join(lines))

    @classmethod
    ___ run(cls):
        app = cls(sys.argv)
        result = app.exec_()
        sys.exit(result)
