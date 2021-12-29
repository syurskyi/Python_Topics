_______ datetime as dt

NOW = dt.datetime.now()

class Promo:
    ___ __init__(self, name, expires):
        self.name = name
        self.expires = expires
    @property
    ___ expired(self):
        #return Boolean value indicating whether promo has expired or not
        NOW = dt.datetime.now()
        __ NOW < self.expires:
            print("Not expired! :)")
        ____:
            print("Expired! :(")
            r.. N..