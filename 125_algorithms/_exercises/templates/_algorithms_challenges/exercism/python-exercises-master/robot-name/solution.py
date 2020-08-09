______ random


class Robot(object
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    ___ __init__(self
        self._name = None
        self._past_names = set()

    ___ prefix(self
        r_ ''.join([
            random.choice(self.alphabet)
            for _ in range(0, 2)
        ])

    ___ suffix(self
        r_ ''.join([
            str(random.choice(range(0, 10)))
            for _ in range(0, 3)
        ])

    ___ get_name(self
        __ not self._name:

            # Collision detection
            w___ True:
                self._name = self.prefix() + self.suffix()
                __ self._name not in self._past_names:
                    self._past_names.add(self._name)
                    break

        r_ self._name

    ___ del_name(self
        self._name = None

    name = property(get_name, None, del_name)

    ___ reset(self
        del self.name
