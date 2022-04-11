____ i.. _______ cycle
_______ ___
____ t__ _______ t__, sleep

SPINNER_STATES =  '-', '\\', '|', '/'   # had to escape \
STATE_TRANSITION_TIME = 0.1


___ spinner(seconds
    """Make a terminal loader/spinner animation using the imports above.
       Takes seconds argument = time for the spinner to run.
       Does not return anything, only prints to stdout."""
    
    cycles = cycle(SPINNER_STATES)


    start_time = t__()

    w.... t__() - start_time <_ seconds:
        s = next(cycles)
        print(s,end='\r')
        
        sleep(STATE_TRANSITION_TIME)


__ _____ __ _____
    spinner(2)
