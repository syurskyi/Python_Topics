
c_ Clock(o..
    'Clock that displays 24 hour clock that rollsover properly'

    ___ - , hour, minute
        hour hour
        minute minute
        cleanup()

    ___  -r
        r.. "%02d:%02d" % (hour, minute)

    ___ -e  other
        r.. r.. (self) __ r.. (other)

    ___ add  minutes
        minute += minutes
        r.. cleanup()

    ___ cleanup
        hour += minute // 60
        hour %= 24
        minute %= 60
        r.. _
