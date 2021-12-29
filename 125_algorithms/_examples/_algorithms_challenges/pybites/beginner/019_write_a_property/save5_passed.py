import datetime as dt

NOW = dt.datetime.now()

class Promo:
    def __init__(self, name, expires):
        self.name = name
        self.expires = expires

    @property
    def expired(self):
        if NOW > self.expires:
            print("Not expired! :)")
            return True
        else:
            print("Expired! :(")
            return False