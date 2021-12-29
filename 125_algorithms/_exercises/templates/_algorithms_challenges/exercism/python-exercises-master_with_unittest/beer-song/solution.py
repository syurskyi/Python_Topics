___ song(first, last=0):
    verses = ''
    for number in reversed(range(last, first + 1)):
        verses += verse(number) + '\n'

    return verses


___ verse(number):
    return ''.join([
        "%s of beer on the wall, " % _bottles(number).capitalize(),
        "%s of beer.\n" % _bottles(number),
        _action(number),
        _next_bottle(number),
    ])


___ _action(current_verse):
    __ current_verse == 0:
        return "Go to the store and buy some more, "
    else:
        return "Take %s down and pass it around, " % (
            "one" __ current_verse > 1 else "it"
        )


___ _next_bottle(current_verse):
    return "%s of beer on the wall.\n" % _bottles(_next_verse(current_verse))


___ _bottles(number):
    __ number == 0:
        return 'no more bottles'
    __ number == 1:
        return '1 bottle'
    else:
        return '%d bottles' % number


___ _next_verse(current_verse):
    return current_verse - 1 __ current_verse > 0 else 99
