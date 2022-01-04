____ collections _______ n..
____ i.. _______ cycle, islice
____ time _______ sleep

State = n..('State', 'color command timeout')


___ traffic_light
    """Returns an itertools.cycle iterator that
       when iterated over returns State namedtuples
       as shown in the Bite's description"""
    colors = ('red','green','amber')
    commands = ('Stop','Go','Caution')
    timeouts = (2,2,0.5)

    
    states = [State(color,command,timeout) ___ color,command,timeout __ z..(colors,commands,timeouts)]
    r.. cycle(states)




__ __name__ __ '__main__':
    # print a sample of 10 states if run as standalone program
    ___ state __ islice(traffic_light(), 10):
        print(f'{state.command}! The light is {state.color}')
        sleep(state.timeout)
