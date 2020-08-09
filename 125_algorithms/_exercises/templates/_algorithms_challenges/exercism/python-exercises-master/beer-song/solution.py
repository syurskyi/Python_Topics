___ song(first, last=0
    verses = ''
    ___ number in reversed(range(last, first + 1)):
        verses += verse(number) + '\n'

    r_ verses


___ verse(number
    r_ ''.join([
        "%s of beer on the wall, " % _bottles(number).capitalize(),
        "%s of beer.\n" % _bottles(number),
        _action(number),
        _next_bottle(number),
    ])


___ _action(current_verse
    __ current_verse __ 0:
        r_ "Go to the store and buy some more, "
    ____
        r_ "Take %s down and pass it around, " % (
            "one" __ current_verse > 1 else "it"
        )


___ _next_bottle(current_verse
    r_ "%s of beer on the wall.\n" % _bottles(_next_verse(current_verse))


___ _bottles(number
    __ number __ 0:
        r_ 'no more bottles'
    __ number __ 1:
        r_ '1 bottle'
    ____
        r_ '%d bottles' % number


___ _next_verse(current_verse
    r_ current_verse - 1 __ current_verse > 0 else 99
