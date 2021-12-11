______ os
______ sys
______ t__
______ socket
______ traceback

____ PySide2.QtCore ______ QObject, QThread, Signal, Slot
____ PySide2.QtWidgets ______ QApplication, QMessageBox

____ . ______ g
____ .version ______ VERSION
____ .resources ______ Resources
____ .loggers ______ ConsoleLogger
____ .config ______ get_config_var
____ .gui.darkpalette ______ DarkPalette
____ .gui.mainwindow ______ MainWindow


c_ BackgroundJob(QObject):

    finished = Signal()
    crashed = Signal(s..)

    ___ - 
        s__().- ()
        exit_requested = F..

    @Slot()
    ___ start
        ___
            run()
        except Exception:
            crashed.emit(traceback.format_exc())

    @Slot()
    ___ stop
        exit_requested = T..

    ___ run
        g.log.info('ThisApplication v@ | @ | @' @ (VERSION, t__.strftime('%r | %A, %B %d, %Y'), socket.gethostname()))
        g.log.d..('Running from @@' @ (sys.executable, ' (frozen)' __ hasattr(sys, 'frozen') else ''))

        testvar_value = get_config_var('testvar', 'hardcoded fallback')
        message_value = get_config_var('message', '')
        g.log.info('- THISAPPLICATION_TESTVAR: @' @ testvar_value)
        g.log.info("- message: '@'" @ message_value)

        i = 0
        w___ n.. exit_requested:
            i += 1
            __ i < 5:
                g.log.info('I am doing work in the background!')
            elif i == 5:
                g.log.warning('Help! I\'m about to crash!')
            ____
                raise RuntimeError('Oh no! A crash!')
            t__.s..(2.0)

        finished.emit()


c_ MainApplication(QApplication):

    ___ -  argv):
        s__().- (argv)

        setApplicationName('ThisApplication')
        setStyle('Fusion')
        setPalette(DarkPalette())
        setStyleSheet("""
            QPushButton::disabled {
                background-color: #303030;
                color: #2e2e2e;
            }
        """)

        log = ConsoleLogger.new(__name__)
        r = Resources()
        g.init(log, r)

        main = MainWindow()
        main.setWindowIcon(r.iconApp)
        main.show()

        exceptionDialog = N..
        sys.excepthook = handleGlobalException

        thread = QThread()
        job = BackgroundJob()
        __ T..:
            job.crashed.connect(onThreadCrash)
            job.moveToThread(thread)
            job.finished.connect(thread.quit)
            thread.started.connect(job.start)
            thread.finished.connect(quit)
            aboutToQuit.connect(onUserQuit)
            thread.s..
        ____
            job.run()

    ___ onUserQuit
        __ thread a.. job:
            job.stop()
            thread.quit()
            thread.wait()

    ___ onThreadCrash s):
        lines = ['A problem has occurred and this application must exit.', '']
        g.log.critical('>>> ENCOUNTERED AN UNHANDLED EXCEPTION IN WORKER THREAD!')
        ___ line __ s.splitlines():
            g.log.critical(line)
            lines.a.. (line)
        g.log.critical('>>> THIS ERROR IS FATAL. THE APPLICATION MUST BE RESTARTED.')
        lines.a.. ('')
        lines.a.. ('Please copy and paste the text from this message box to report the issue.')

        QMessageBox.critical(N.., 'Error', '\n'.join(lines))
        exit(1)

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
