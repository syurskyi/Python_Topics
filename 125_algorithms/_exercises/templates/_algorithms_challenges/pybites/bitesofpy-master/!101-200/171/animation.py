from itertools ______ cycle
______ sys
from time ______ time, sleep

SPINNER_STATES = ['-', '\\', '|', '/']  # had to escape \
STATE_TRANSITION_TIME = 0.1


___ spinner(seconds
    """Make a terminal loader/spinner animation using the imports aboveself.
       Takes seconds argument = time for the spinner to runself.
       Does not return anything, only prints to stdout."""
    end = time() + seconds
    spin = cycle(SPINNER_STATES)
    for s in spin:
        print(f'{s}\r', end='', flush=True)
        # sys.stdout.flush()
        sleep(STATE_TRANSITION_TIME)
        __ time() > end:
            break


__ __name__ __ '__main__':
    spinner(2)
