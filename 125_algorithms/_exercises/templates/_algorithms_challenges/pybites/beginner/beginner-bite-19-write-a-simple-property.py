'''
Bite 19. Write a simple property
Write a simple Promo class. Its constructor receives a name str and expires datetime.

Add a property called expired which returns a bool.

Checkout the tests and datetime module for more info. Have fun!
'''

'''
TESTS
-----
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
'''

____ d__ _______ d__

c_ Promo:
    ___ - , name, expires
        name = name
        expires = expires

    $
    ___ expired
        r.. d__.n.. > expires




