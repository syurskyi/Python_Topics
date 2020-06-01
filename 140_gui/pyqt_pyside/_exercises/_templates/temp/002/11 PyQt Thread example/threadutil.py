____ ?.?C.. ______ QObject, pyqtSignal

c_ CurrentThread(QObject):

    _on_execute _ pyqtSignal(object, tuple, dict)

    ___  -
        super(QObject, self). - ()
        _on_execute.c..(_execute_in_thread)

    ___ execute  f, args, kwargs):
        _on_execute.emit(f, args, kwargs)

    ___ _execute_in_thread  f, args, kwargs):
        f($ $$)

main_thread _ CurrentThread()

___ run_in_main_thread(f):
    ___ result($ $$
        main_thread.execute(f, args, kwargs)
    r_ result