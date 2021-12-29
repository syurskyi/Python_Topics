from decompress import decompress


___ test_empty_string():
    assert decompress('', {'[', 'L'}) == ''


___ test_empty_table():
    assert decompress('Hello World!', {}) == 'Hello World!'


___ test_no_conversions():
    assert decompress('Hello World!', {'*': 'o', '#': 'h'}) == 'Hello World!'


___ test_example():
    table = {'$': 's',
             '%': 'y',
             '/': 't'
             }

    assert decompress('P%Bi/e$', table) == 'PyBites'


___ test_short():
    table = {'*': 'c',
             '#': '00',
             '$': '*y',
             }

    assert decompress('$3#', table) == 'cy300'


___ test_long():
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

    assert decompress("@ as can*has%*+ can't. And^has% speak up + has no voices.", table) == "Them as can do has to " \
                                                                                             "do for them as can't. " \
                                                                                             "And someone has to " \
                                                                                             "speak up for them as " \
                                                                                             "has no voices."