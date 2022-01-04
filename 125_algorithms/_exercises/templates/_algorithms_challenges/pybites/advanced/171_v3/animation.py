____ i.. _______ cycle
_______ sys
____ time _______ time, sleep

SPINNER_STATES = ['-', '\\', '|', '/']  # had to escape \
STATE_TRANSITION_TIME = 0.1


___ spinner(seconds):
    """Make a terminal loader/spinner animation using the imports aboveself.
       Takes seconds argument = time for the spinner to runself.
       Does not return anything, only prints to stdout."""
    end = time() + seconds
    spin = cycle(SPINNER_STATES)
    ___ s __ spin:
        print(f'{s}\r', end='', flush=T..)
        # sys.stdout.flush()
        sleep(STATE_TRANSITION_TIME)
        __ time() > end:
            break


__ _____ __ _____
    spinner(2)
