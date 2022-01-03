c_ Purchase:
    ___ __init__(
            self, city, zipcode, state, beds,
            baths, sq__ft, home_type, sale_date, price,
            latitude, longitude):
        longitude  longitude
        latitude  latitude
        price  price
        sale_date  sale_date
        t..  home_type
        sq__ft  sq__ft
        baths  baths
        beds  beds
        state  state
        z..  zipcode
        city  city

    @staticmethod
    ___ create_from_dict(lookup):
        r.. Purchase(
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
