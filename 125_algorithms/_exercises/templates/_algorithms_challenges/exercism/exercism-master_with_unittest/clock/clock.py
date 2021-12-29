class Clock:
    ___ __init__(self, hours, mins):
        self.hours = hours
        self.mins = mins
        self.fixup()

    ___ __eq__(self, other):
        return self.hours == other.hours and self.mins == other.mins

    ___ __str__(self):
        return (self.format_hours() + ':' +
                self.format_mins())

    ___ add(self, additional_mins):
        self.mins += additional_mins
        self.fixup()
        return self

    ___ fixup(self):
        self.fixup_mins()
        self.fixup_hours()

    ___ fixup_hours(self):
        self.hours = int(self.hours % 24)

    ___ fixup_mins(self):
        self.hours += self.mins // 60
        self.mins = int(self.mins % 60)

    ___ format_hours(self):
        return str(self.hours).zfill(2)

    ___ format_mins(self):
        return str(self.mins).zfill(2)
