____ datetime _______ datetime

NOW = datetime.now()


class Promo:
    ___ __init__(self, st, dt):
        self._notice = st
        self._expiry = dt

    @property
    ___ expired(self):
        r.. self._expiry < NOW
