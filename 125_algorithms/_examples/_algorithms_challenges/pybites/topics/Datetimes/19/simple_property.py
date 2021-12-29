from datetime import datetime

NOW = datetime.now()

class Promo:
    def __init__(self, app, expirydate):
        self.app = app
        self.expirydate = expirydate

    @property
    def expired(self):
        return NOW > self.expirydate