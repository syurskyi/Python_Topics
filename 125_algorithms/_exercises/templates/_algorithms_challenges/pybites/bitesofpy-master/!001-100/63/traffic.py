from collections ______ namedtuple
from itertools ______ cycle, islice
from time ______ sleep

State = namedtuple('State', 'color command timeout')


___ traffic_light(
    """Returns an itertools.cycle iterator that
       when iterated over returns State namedtuples
       as shown in the Bite's description"""
    states = cycle([State('red', 'Stop', 2), State('green', 'Go', 2), State('amber', 'Caution', 0.5)])
    for s in states:
        yield s


__ __name__ __ '__main__':
    # print a sample of 10 states if run as standalone program
    for state in islice(traffic_light(), 10
        print(f'{state.command}! The light is {state.color}')
        sleep(state.timeout)
