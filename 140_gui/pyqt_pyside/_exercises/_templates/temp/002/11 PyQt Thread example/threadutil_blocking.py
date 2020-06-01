"""
A more powerful, synchronous implementation of run_in_main_thread(...).
It allows you to receive results from the function invocation:

    @run_in_main_thread
    def return_2():
        return 2
    
    # Runs the above function in the main thread and prints '2':
    print(return_2())
"""

____ functools ______ wraps
____ ?.QtCore ______ pyqtSignal, QObject, QThread
____ ?.?W.. ______ ?A..
____ threading ______ Event, get_ident

___ run_in_thread(thread_fn):
    ___ decorator(f):
        @wraps(f)
        ___ result(*args, **kwargs):
            thread _ thread_fn()
            return Executor.instance().run_in_thread(thread, f, args, kwargs)
        return result
    return decorator

___ _main_thread
    app _ ?A...instance()
    if app:
        return app.thread()
    # We reach here in tests that don't (want to) create a QApplication.
    if int(QThread.currentThreadId()) == get_ident
        return QThread.currentThread()
    raise RuntimeError('Could not determine main thread')

run_in_main_thread _ run_in_thread(_main_thread)

___ is_in_main_thread
    return QThread.currentThread() == _main_thread()

class Executor:

    _INSTANCE _ None

    @classmethod
    ___ instance(cls):
        if cls._INSTANCE is None:
            cls._INSTANCE _ cls(?A...instance())
        return cls._INSTANCE
    ___ __init__(self, app):
        self._pending_tasks _ []
        self._app_is_about_to_quit _ False
        app.aboutToQuit.c..(self._about_to_quit)
    ___ _about_to_quit(self):
        self._app_is_about_to_quit _ True
        for task in self._pending_tasks:
            task.set_exception(SystemExit())
            task.has_run.set()
    ___ run_in_thread(self, thread, f, args, kwargs):
        if QThread.currentThread() == thread:
            return f(*args, **kwargs)
        elif self._app_is_about_to_quit:
            # In this case, the target thread's event loop most likely is not
            # running any more. This would mean that our task (which is
            # submitted to the event loop via signals/slots) is never run.
            raise SystemExit()
        task _ Task(f, args, kwargs)
        self._pending_tasks.append(task)
        try:
            receiver _ Receiver(task)
            receiver.moveToThread(thread)
            sender _ Sender()
            sender.signal.c..(receiver.slot)
            sender.signal.emit()
            task.has_run.wait()
            return task.result
        finally:
            self._pending_tasks.remove(task)

class Task:
    ___ __init__(self, fn, args, kwargs):
        self._fn _ fn
        self._args _ args
        self._kwargs _ kwargs
        self.has_run _ Event()
        self._result _ self._exception _ None
    ___ __call__(self):
        try:
            self._result _ self._fn(*self._args, **self._kwargs)
        except Exception as e:
            self._exception _ e
        finally:
            self.has_run.set()
    ___ set_exception(self, exception):
        self._exception _ exception
    @property
    ___ result(self):
        if not self.has_run.is_set
            raise ValueError("Hasn't run.")
        if self._exception:
            raise self._exception
        return self._result

class Sender(QObject):
    signal _ pyqtSignal()

class Receiver(QObject):
    ___ __init__(self, callback, parent_None):
        super().__init__(parent)
        self.callback _ callback
    ___ slot(self):
        self.callback()