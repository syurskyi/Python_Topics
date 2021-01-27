from datetime import timedelta
import inspect

from simple_property import Promo, NOW


def test_promo_expired():
    past_time = NOW - timedelta(seconds=3)
    twitter_promo = Promo('twitter', past_time)
    a__ twitter_promo.expired


def test_promo_not_expired():
    future_date = NOW + timedelta(days=1)
    newsletter_promo = Promo('newsletter', future_date)
    a__ not newsletter_promo.expired


def test_uses_property():
    a__ 'property' in inspect.getsource(Promo)