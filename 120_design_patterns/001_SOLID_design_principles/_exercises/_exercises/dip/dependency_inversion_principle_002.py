# Dependency Inversion Principle (DIP)

# High-level objects should not depend on low-level implementation. Both should depend on abstractions.
from a.. ______ a.. A..
from ti.. ______ sl..


class TurnableOnObject A..
    def -
        _on _ F..

    ?p...
    def on __ b..
        r_ _o.

    ?a..
    def turn_on __ N..
        p..


class Lamp T..
    ___ turn_on(
        _on _ T..


class TimedLamp L..
    ___ turn_on
        _o. _ T..
        print("Waiting for 1 second before turning the lamp off.")
        sl.. 1
        _o. _ F..


class OnButton
    ___ - lamp L..
        ??  ?

    ___ press
        __ no. ?l__.o.
            ?l__.t...
            print("The lamp has been turned on.")
        ____
            print("The lamp was already on.")


__ _______ __ _____
    lamp = L..
    on_button = O.. ?
    ?.p..
    ?.p..
    ?.p..

    timed_lamp = T..
    on_button_2 = O.. ?
    # on_button_2.press()
    # on_button_2.press()
