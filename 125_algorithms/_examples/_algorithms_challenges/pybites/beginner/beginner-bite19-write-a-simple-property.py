"""
Write a simple Promo class. Its constructor receives a name str and expires datetime.

Add a property called expired which returns a bool.

Checkout the tests and datetime module for more info. Have fun!

from datetime import timedelta

from simple_property import Promo, NOW


def test_promo_expired():
    past_time = NOW - timedelta(seconds=3)
    twitter_promo = Promo('twitter', past_time)
    assert twitter_promo.expired


def test_promo_not_expired():
    future_date = NOW + timedelta(days=1)
    newsletter_promo = Promo('newsletter', future_date)
    assert not newsletter_promo.expired

"""

from datetime import datetime
from datetime import timedelta
NOW = datetime.now()


class Promo:

    def __init__(self, name, expires=NOW):
        self.name = name
        self.expires = expires

    @property
    def expired(self):
        return datetime.now() > self.expires

p = Promo('blackfriday', NOW + timedelta(days=5))

print(p.expired)
