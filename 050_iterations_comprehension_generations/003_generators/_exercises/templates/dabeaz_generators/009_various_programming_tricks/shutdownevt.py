# shutdownevt.py
#
# Example of a generator that uses an event to shut down

______ ti__

___ follow(thefile,shutdown=N..):
    thefile.s..(0,2)
    w____ T..
        __ shutdown and shutdown.isSet(): break
        line = thefile.readline()
        __ no. line:
           ti__.s..(0.1)
           c...
        y... line

______ t___

shutdown_event = t___.Event()

___ run():
    lines = follow(o..("run/foo/access-log"),shutdown_event)
    ___ line __ lines:
        print line,

    print "Done"


# Run the above in a separate thread
t = t___.T...(t.._run)
t.s..

# Wait a while then shut down


ti__.s..(60)
print "Shutting down"

shutdown_event.se.()

