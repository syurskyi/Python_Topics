____ datetime _______ datetime

NOW = datetime.now()

class Promo:
    ___ __init__(self, app, expirydate):
        self.app = app
        self.expirydate = expirydate

    @property
    ___ expired(self):
        r.. NOW > self.expirydate