____ decompress _______ decompress


___ test_empty_string
    ... decompress('', {'[', 'L'}) __ ''


___ test_empty_table
    ... decompress('Hello World!', {}) __ 'Hello World!'


___ test_no_conversions
    ... decompress('Hello World!', {'*': 'o', '#': 'h'}) __ 'Hello World!'


___ test_example
    table = {'$': 's',
             '%': 'y',
             '/': 't'
             }

    ... decompress('P%Bi/e$', table) __ 'PyBites'


___ test_short
    table = {'*': 'c',
             '#': '00',
             '$': '*y',
             }

    ... decompress('$3#', table) __ 'cy300'


___ test_long
    table = {'#': 'hem',
             '@': 'T#',
             '$': 't#',
             '&': '$ as',
             '*': ' do ',
             '%': ' to',
             '^': ' someone ',
             '~': 'for ',
             '+': '~&',
             }

    ... decompress("@ as can*has%*+ can't. And^has% speak up + has no voices.", table) __ "Them as can do has to " \
                                                                                             "do for them as can't. " \
                                                                                             "And someone has to " \
                                                                                             "speak up for them as " \
                                                                                             "has no voices."