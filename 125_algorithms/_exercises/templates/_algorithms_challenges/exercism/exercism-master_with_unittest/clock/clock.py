c_ Clock:
    ___ - , hours, mins):
        hours = hours
        mins = mins
        fixup()

    ___ __eq__(self, other):
        r.. hours __ other.hours a.. mins __ other.mins

    ___ __str__
        r.. (format_hours() + ':' +
                format_mins())

    ___ add(self, additional_mins):
        mins += additional_mins
        fixup()
        r.. self

    ___ fixup
        fixup_mins()
        fixup_hours()

    ___ fixup_hours
        hours = int(hours % 24)

    ___ fixup_mins
        hours += mins // 60
        mins = int(mins % 60)

    ___ format_hours
        r.. s..(hours).zfill(2)

    ___ format_mins
        r.. s..(mins).zfill(2)
