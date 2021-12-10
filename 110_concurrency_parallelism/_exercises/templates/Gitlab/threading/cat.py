from threading import Thread
import time

""" The Cat class is a Thread by itself. There must be an __init__ calling Super
__init__ with self as an argument. Also, there must be an "run" def. """
class Cat(Thread):            # Cat is a thread.

    def run(self):            # This is the default thread method.
        while True:           # To keep the thread alive "while true is needed".
            print 'The cat chases the mouse.'
            time.sleep(11)    # Delay time for 1 second.

    def __init__(self):
        Thread.__init__(self)
        self.daemon = True    # Always set daemon flag to True.
        self.start()          # It starts the thread.
