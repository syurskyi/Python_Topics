class Purchase:
    ___ __init__(
            self, city, zipcode, state, beds,
            baths, sq__ft, home_type, sale_date, price,
            latitude, longitude):
        self.longitude  longitude
        self.latitude  latitude
        self.price  price
        self.sale_date  sale_date
        self.type  home_type
        self.sq__ft  sq__ft
        self.baths  baths
        self.beds  beds
        self.state  state
        self.zip  zipcode
        self.city  city

    @staticmethod
    ___ create_from_dict(lookup):
        return Purchase(
            lookup['city'],
            lookup['zip'],
            lookup['state'],
            i..(lookup['beds']),
            i..(lookup['baths']),
            i..(lookup['sq__ft']),
            lookup['type'],
            lookup['sale_date'],
            float(lookup['price']),
            float(lookup['latitude']),
            float(lookup['longitude']))
