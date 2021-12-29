_______ random


class Robot(object):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    ___ __init__(self):
        self._name = N..
        self._past_names = set()

    ___ prefix(self):
        r.. ''.join([
            random.choice(self.alphabet)
            ___ _ __ r..(0, 2)
        ])

    ___ suffix(self):
        r.. ''.join([
            s..(random.choice(r..(0, 10)))
            ___ _ __ r..(0, 3)
        ])

    ___ get_name(self):
        __ n.. self._name:

            # Collision detection
            w... T...
                self._name = self.prefix() + self.suffix()
                __ self._name n.. __ self._past_names:
                    self._past_names.add(self._name)
                    break

        r.. self._name

    ___ del_name(self):
        self._name = N..

    name = property(get_name, N.., del_name)

    ___ reset(self):
        del self.name
