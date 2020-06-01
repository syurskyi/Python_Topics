____ ?.QtCore ______ QObject, pyqtSignal

c_ CurrentThread(QObject):

    _on_execute _ pyqtSignal(object, tuple, dict)

    ___ __init__(self):
        super(QObject, self).__init__()
        self._on_execute.c..(self._execute_in_thread)

    ___ execute  f, args, kwargs):
        self._on_execute.emit(f, args, kwargs)

    ___ _execute_in_thread  f, args, kwargs):
        f(*args, **kwargs)

main_thread _ CurrentThread()

___ run_in_main_thread(f):
    ___ result(*args, **kwargs):
        main_thread.execute(f, args, kwargs)
    r_ result