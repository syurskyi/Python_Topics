class Clock(object
    ___ __init__(self, hour, minute
        hour += minute // 60
        self.hour = hour % 24
        self.minute = minute % 60

    ___ __repr__(self
        r_ '{:02}:{:02}'.format(self.hour, self.minute)

    ___ __eq__(self, other
        r_ self.hour __ other.hour and self.minute __ other.minute

    ___ __add__(self, minutes
        r_ Clock(self.hour, self.minute + minutes) 

    ___ __sub__(self, minutes
        r_ Clock(self.hour, self.minute - minutes) 
