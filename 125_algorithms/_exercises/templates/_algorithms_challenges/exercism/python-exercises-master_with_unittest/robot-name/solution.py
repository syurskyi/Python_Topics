_______ r__


c_ Robot(o..
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    ___ -
        _name = N..
        _past_names = s..()

    ___ prefix
        r.. ''.j..([
            r__.c..(alphabet)
            ___ _ __ r..(0, 2)
        ])

    ___ suffix
        r.. ''.j..([
            s..(r__.c..(r..(0, 10)))
            ___ _ __ r..(0, 3)
        ])

    ___ get_name
        __ n.. _name:

            # Collision detection
            w... T...
                _name = prefix() + suffix()
                __ _name n.. __ _past_names:
                    _past_names.add(_name)
                    _____

        r.. _name

    ___ del_name
        _name = N..

    name = property(get_name, N.., del_name)

    ___ reset
        del name
