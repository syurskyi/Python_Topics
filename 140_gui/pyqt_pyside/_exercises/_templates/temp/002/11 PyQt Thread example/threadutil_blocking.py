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
____ ?.?C.. ______ pS.., ?O.., ?T..
____ ?.?W.. ______ ?A..
____ th.. ______ Event, get_ident

___ run_in_thread(thread_fn):
    ___ decorator(f):
        @wraps(f)
        ___ result($ $$
            thread _ thread_fn()
            r_ Executor.i.. .run_in_thread(thread, f, args, kwargs)
        r_ result
    r_ decorator

___ _main_thread
    app _ ?A...i.. 
    __ app:
        r_ app.thread()
    # We reach here in tests that don't (want to) create a QApplication.
    __ int(?T...currentThreadId()) __ get_ident
        r_ ?T...currentThread()
    raise RuntimeError('Could not determine main thread')

run_in_main_thread _ run_in_thread(_main_thread)

___ is_in_main_thread
    r_ ?T...currentThread() __ _main_thread()

c_ Executor:

    _INSTANCE _ N..

    @classmethod
    ___ instance(cls):
        __ cls._INSTANCE __ N..:
            cls._INSTANCE _ cls(?A...instance())
        r_ cls._INSTANCE
    ___  -   app):
        _pending_tasks _   # list
        _app_is_about_to_quit _ F..
        app.aboutToQuit.c..(_about_to_quit)
    ___ _about_to_quit
        _app_is_about_to_quit _ T..
        ___ task __ _pending_tasks:
            task.set_exception(SystemExit())
            task.has_run.set()
    ___ run_in_thread  thread, f, args, kwargs):
        __ ?T...currentThread() __ thread:
            r_ f($ $$)
        ____ _app_is_about_to_quit:
            # In this case, the target thread's event loop most likely is not
            # running any more. This would mean that our task (which is
            # submitted to the event loop via signals/slots) is never run.
            raise SystemExit()
        task _ Task(f, args, kwargs)
        _pending_tasks.ap..(task)
        ___
            receiver _ Receiver(task)
            receiver.moveToThread(thread)
            sender _ Sender()
            sender.signal.c..(receiver.slot)
            sender.signal.e..()
            task.has_run.wait()
            r_ task.result
        finally:
            _pending_tasks.remove(task)

c_ Task:
    ___  -   fn, args, kwargs):
        _fn _ fn
        _args _ args
        _kwargs _ kwargs
        has_run _ Event()
        _result _ _exception _ N..
    ___ __call__
        ___
            _result _ _fn(*_args, **_kwargs)
        _____ E.. __ e:
            _exception _ e
        finally:
            has_run.set()
    ___ set_exception  exception):
        _exception _ exception
    @property
    ___ result
        __ no. has_run.is_set
            raise ValueError("Hasn't run.")
        __ _exception:
            raise _exception
        r_ _result

c_ Sender(?O..):
    signal _ pS..()

c_ Receiver(?O..):
    ___  -   callback, parent_None):
        s_. - (parent)
        callback _ callback
    ___ slot
        callback()