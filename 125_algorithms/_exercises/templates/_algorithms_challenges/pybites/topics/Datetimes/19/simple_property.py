from datetime import datetime

NOW = datetime.now()

class Promo:
    ___ __init__(self, app, expirydate):
        self.app = app
        self.expirydate = expirydate

    @property
    ___ expired(self):
        return NOW > self.expirydate