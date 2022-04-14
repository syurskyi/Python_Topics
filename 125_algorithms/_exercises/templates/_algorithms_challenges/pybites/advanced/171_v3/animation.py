____ i.. _______ cycle
_______ ___
____ t__ _______ t__, sleep

SPINNER_STATES =  '-', '\\', '|', '/'   # had to escape \
STATE_TRANSITION_TIME 0.1


___ spinner(seconds
    """Make a terminal loader/spinner animation using the imports aboveself.
       Takes seconds argument = time for the spinner to runself.
       Does not return anything, only prints to stdout."""
    end t__ + seconds
    spin cycle(SPINNER_STATES)
    ___ s __ spin:
        print _*{s}\r', e.._'', flush=T..)
        # sys.stdout.flush()
        sleep(STATE_TRANSITION_TIME)
        __ t__ > end:
            _____


__ _____ __ _____
    spinner(2)
