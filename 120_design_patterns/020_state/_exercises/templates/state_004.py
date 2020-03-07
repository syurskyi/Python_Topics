"""State pattern

A state machine is an abstract machine with two main components:
  - states. A state is the current status of a system. A state machine can have
    only one active state at any point in time.
  - transitions. A transition is a switch from the current state to a new one.

Basic example with the transitions library
https://github.com/tyarkoni/transitions
"""
______ r...
____ tr...______ M..E..
____ transitions.extensions ______ GM..


c_ Process o..

    states = ["sleeping", "waiting", "running", "terminated"]

    ___ __init__(self, name):
        self.name = name

        # initialize the state machine
        self.machine = GraphMachine(model=self, states=self.states, initial="sleeping")

        # add transitions
        self.machine.add_transition(
            trigger="wake_up", source="sleeping", dest="waiting"
        )
        self.machine.add_transition(
            trigger="start", source="waiting", dest="running", before="display_message"
        )
        self.machine.add_transition(
            trigger="interrupt", source="*", dest="terminated", after="display_warning"
        )
        self.machine.add_transition(
            trigger="random_trigger",
            source="*",
            dest="terminated",
            conditions=["is_valid"],
        )

        # create image of the state machine (requires GraphViz and pygraphviz)
        self.graph.draw("my_state_diagram.png", prog="dot")

    ___ is_valid(self):
        return random.random() < 0.5

    ___ display_message(self):
        print("I'm starting...")

    ___ display_warning(self):
        print("I've just got an interrupt!")

    ___ random_termination(self):
        print("terminated")


___ main():
    p = Process("p1")
    print("initial state: {}".format(p.state))

    old = p.state
    print("\nwake_up trigger")
    p.wake_up()
    print("{} -> {}".format(old, p.state))

    old = p.state
    print("\nstart trigger")
    p.start()
    print("{} -> {}".format(old, p.state))

    old = p.state
    print("\nrandom trigger (stay in current state or go to terminated 50/50)")
    p.random_trigger()
    print("{} -> {}".format(old, p.state))

    old = p.state
    print("\ninterrupt trigger")
    p.interrupt()
    print("{} -> {}".format(old, p.state))

    print('\nFrom "terminated" we cannot trigger a "start" event')
    try:
        p.start()
    except MachineError as e:
        print(e)


if __name__ == "__main__":
    main()
