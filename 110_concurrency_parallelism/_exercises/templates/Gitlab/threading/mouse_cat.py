from _ ______ ?
______ t__

___ mouse_runs():                # The mouse action.
    w___ True:                  # It keeps the thread alive.
        print "The mouse runs."
        t__.s..(4)            # It waits 4 seconds till it's next move.

___ cat_chases_mouse():          # The cat's action.
    w___ True:                  # It keeps the thread alive.
        print "The cat chases the rat."
        t__.s..(5)            # It waits 5 seconds till it's next move.

___ action():

    mouse_thread = ? ?_mouse_runs) # Sets the ___ as target.
    cat_thread = ? ?_cat_chases_mouse)

    mouse_thread.setDaemon(True) # Always set daemon as True.
    cat_thread.setDaemon(True)   # Always set daemon as True.

    mouse_thread.s..         # It starts the mouse thread.
    cat_thread.s..           # It starts the cat thread.

__ ____ __ ______:       # In case of execution by using terminal.

    action()

    w___ True:
        t__.s..(1)            # Without this wait t__, the thread would
                                 # consume 90% up of CPU processing t__.
