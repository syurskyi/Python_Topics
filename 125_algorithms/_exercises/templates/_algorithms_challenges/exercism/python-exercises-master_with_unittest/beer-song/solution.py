___ song(first, last=0):
    verses = ''
    ___ number __ reversed(r..(last, first + 1)):
        verses += verse(number) + '\n'

    r.. verses


___ verse(number):
    r.. ''.j..([
        "%s of beer on the wall, " % _bottles(number).capitalize(),
        "%s of beer.\n" % _bottles(number),
        _action(number),
        _next_bottle(number),
    ])


___ _action(current_verse):
    __ current_verse __ 0:
        r.. "Go to the store and buy some more, "
    ____:
        r.. "Take %s down and pass it around, " % (
            "one" __ current_verse > 1 ____ "it"
        )


___ _next_bottle(current_verse):
    r.. "%s of beer on the wall.\n" % _bottles(_next_verse(current_verse))


___ _bottles(number):
    __ number __ 0:
        r.. 'no more bottles'
    __ number __ 1:
        r.. '1 bottle'
    ____:
        r.. '%d bottles' % number


___ _next_verse(current_verse):
    r.. current_verse - 1 __ current_verse > 0 ____ 99
