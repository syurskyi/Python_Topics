from itertools import cycle
import sys
from time import time, sleep

SPINNER_STATES = ['-', '\\', '|', '/']  # had to escape \
STATE_TRANSITION_TIME = 0.1


___ spinner(seconds):
    """Make a terminal loader/spinner animation using the imports aboveself.
       Takes seconds argument = time for the spinner to runself.
       Does not return anything, only prints to stdout."""
    t = time()
    c = cycle(SPINNER_STATES)
    while True:
        __ time() > t + seconds:
            break
        print(f'\r{next(c)}', end='', file=sys.stdout, flush=True)
        sleep(STATE_TRANSITION_TIME)


__ __name__ == '__main__':
    spinner(2)
