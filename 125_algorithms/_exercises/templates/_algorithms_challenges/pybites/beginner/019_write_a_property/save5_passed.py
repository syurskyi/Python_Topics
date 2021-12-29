_______ datetime as dt

NOW = dt.datetime.now()

class Promo:
    ___ __init__(self, name, expires):
        self.name = name
        self.expires = expires

    @property
    ___ expired(self):
        __ NOW > self.expires:
            print("Not expired! :)")
            r.. True
        ____:
            print("Expired! :(")
            r.. False