
c_ Clock(object):
    'Clock that displays 24 hour clock that rollsover properly'

    ___ - , hour, minute):
        hour = hour
        minute = minute
        cleanup()

    ___ __repr__
        r.. "%02d:%02d" % (hour, minute)

    ___ __eq__(self, other):
        r.. repr(self) __ repr(other)

    ___ add(self, minutes):
        minute += minutes
        r.. cleanup()

    ___ cleanup
        hour += minute // 60
        hour %= 24
        minute %= 60
        r.. self
