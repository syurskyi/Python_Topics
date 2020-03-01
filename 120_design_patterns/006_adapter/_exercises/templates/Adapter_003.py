#!/usr/bin/env python
# Written by: DGC

#==============================================================================
c_ RCCar o..

    ___ -
        .speed _ 0

    ___ change_speed speed
        ?   ?
        print("RC car is moving at " + st. ??

#==============================================================================
c_ RCAdapter o..

    ___ -
        ?car _ R..

    ___ move_forwards
        c__.c__ 10

    ___ move_backwards
        c__.c...-10

    ___ stop(self):
        self.car.change_speed(0)

#==============================================================================
c_ RemoteControl o..

    ___ __init__(self):
        self.adapter _ RCAdapter()

    ___ stick_up(self):
        self.adapter.move_forwards()

    ___ stick_down(self):
        self.adapter.move_backwards()

    ___ stick_middle(self):
        self.adapter.stop()

#==============================================================================
if (__name__ == "__main__"):
    controller _ RemoteControl()
    controller.stick_up()
    controller.stick_middle()
    controller.stick_down()
    controller.stick_middle()
    
