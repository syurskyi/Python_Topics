____ collections _______ n..
____ i.. _______ cycle, islice
____ time _______ sleep

State = n..('State', 'color command timeout')


___ traffic_light():
    """Returns an itertools.cycle iterator that
       when iterated over returns State namedtuples
       as shown in the Bite's description"""
    states = cycle([State('red', 'Stop', 2), State('green', 'Go', 2), State('amber', 'Caution', 0.5)])
    ___ s __ states:
        y.. s


__ __name__ __ '__main__':
    # print a sample of 10 states if run as standalone program
    ___ state __ islice(traffic_light(), 10):
        print(f'{state.command}! The light is {state.color}')
        sleep(state.timeout)
