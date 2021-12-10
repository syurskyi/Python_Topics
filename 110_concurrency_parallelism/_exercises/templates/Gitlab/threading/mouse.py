from threading import Thread
import time

""" The Mouse class is a Thread by itself. There must be an __init__ calling
Super __init__ with self as an argument. Also, there must be an "run" def. """
class Mouse(Thread):           # Mouse is a thread.

    def run(self):
        while True:            # It keeps the thread alive the whole time.
            print 'The mouse runs.'
            time.sleep(10)

    def __init__(self):
        Thread.__init__(self)  # Thread.__init__.
        self.daemon = True     # Always set daemon flag True.
        self.start()           # Starts the thread.
