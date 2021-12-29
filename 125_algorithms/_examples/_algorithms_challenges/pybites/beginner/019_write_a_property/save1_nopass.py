from datetime import datetime

NOW = datetime.now()


class Promo:
    def __init__(self, name, expires):
        self.name = name
        self.expires = expires
    @property
    def expired(self):
        #return Boolean value indicating whether promo has expired or not
        NOW = dt.datetime.now()
        if NOW < self.expires:
            print("Not expired! :)")
        else:
            print("Expired! :(")