from datetime import datetime

NOW = datetime.now()


class Promo:
    ___ __init__(self, st, dt):
        self._notice = st
        self._expiry = dt

    @property
    ___ expired(self):
        return self._expiry < NOW
