# shutdownevt.py
#
# Example of a generator that uses an event to shut down

______ time

___ follow(thefile,shutdown=N..):
    thefile.seek(0,2)
    while True:
        __ shutdown and shutdown.isSet(): break
        line = thefile.readline()
        __ not line:
           time.sleep(0.1)
           continue
        y... line

______ threading

shutdown_event = threading.Event()

___ run():
    lines = follow(o..("run/foo/access-log"),shutdown_event)
    ___ line __ lines:
        print line,

    print "Done"


# Run the above in a separate thread
t = threading.Thread(target=run)
t.start()

# Wait a while then shut down


time.sleep(60)
print "Shutting down"

shutdown_event.se.()

