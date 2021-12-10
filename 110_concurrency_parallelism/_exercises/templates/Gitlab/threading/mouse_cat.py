from threading import Thread
import time

def mouse_runs():                # The mouse action.
    while True:                  # It keeps the thread alive.
        print "The mouse runs."
        time.sleep(4)            # It waits 4 seconds till it's next move.

def cat_chases_mouse():          # The cat's action.
    while True:                  # It keeps the thread alive.
        print "The cat chases the rat."
        time.sleep(5)            # It waits 5 seconds till it's next move.

def action():

    mouse_thread = Thread(target=mouse_runs) # Sets the def as target.
    cat_thread = Thread(target=cat_chases_mouse)

    mouse_thread.setDaemon(True) # Always set daemon as True.
    cat_thread.setDaemon(True)   # Always set daemon as True.

    mouse_thread.start()         # It starts the mouse thread.
    cat_thread.start()           # It starts the cat thread.

if __name__ == "__main__":       # In case of execution by using terminal.

    action()

    while True:
        time.sleep(1)            # Without this wait time, the thread would
                                 # consume 90% up of CPU processing time.
