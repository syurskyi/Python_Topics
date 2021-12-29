
class Clock(object):
    'Clock that displays 24 hour clock that rollsover properly'

    ___ __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute
        self.cleanup()

    ___ __repr__(self):
        r.. "%02d:%02d" % (self.hour, self.minute)

    ___ __eq__(self, other):
        r.. repr(self) __ repr(other)

    ___ add(self, minutes):
        self.minute += minutes
        r.. self.cleanup()

    ___ cleanup(self):
        self.hour += self.minute // 60
        self.hour %= 24
        self.minute %= 60
        r.. self
