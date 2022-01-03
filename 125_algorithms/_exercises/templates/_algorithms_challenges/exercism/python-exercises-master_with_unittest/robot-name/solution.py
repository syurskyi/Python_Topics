_______ random


c_ Robot(object):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    ___ - ):
        _name = N..
        _past_names = set()

    ___ prefix
        r.. ''.j..([
            random.choice(alphabet)
            ___ _ __ r..(0, 2)
        ])

    ___ suffix
        r.. ''.j..([
            s..(random.choice(r..(0, 10)))
            ___ _ __ r..(0, 3)
        ])

    ___ get_name
        __ n.. _name:

            # Collision detection
            w... T...
                _name = prefix() + suffix()
                __ _name n.. __ _past_names:
                    _past_names.add(_name)
                    break

        r.. _name

    ___ del_name
        _name = N..

    name = property(get_name, N.., del_name)

    ___ reset
        del name
