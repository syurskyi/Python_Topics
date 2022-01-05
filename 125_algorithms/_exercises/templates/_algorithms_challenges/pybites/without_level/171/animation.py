____ i.. _______ cycle
_______ sys
____ time _______ time, sleep

SPINNER_STATES = ['-', '\\', '|', '/']  # had to escape \
STATE_TRANSITION_TIME = 0.1


___ spinner(seconds):
    """Make a terminal loader/spinner animation using the imports aboveself.
       Takes seconds argument = time for the spinner to runself.
       Does not return anything, only prints to stdout."""
    t = time()
    c = cycle(SPINNER_STATES)
    w... T...
        __ time() > t + seconds:
            _____
        print _*\r{next(c)}', end='', file=sys.stdout, flush=T..)
        sleep(STATE_TRANSITION_TIME)


__ _____ __ _____
    spinner(2)
