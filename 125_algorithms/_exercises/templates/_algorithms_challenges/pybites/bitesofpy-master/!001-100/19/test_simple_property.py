from datetime ______ timedelta
______ inspect

from simple_property ______ Promo, NOW


___ test_promo_expired(
    past_time = NOW - timedelta(seconds=3)
    twitter_promo = Promo('twitter', past_time)
    assert twitter_promo.expired


___ test_promo_not_expired(
    future_date = NOW + timedelta(days=1)
    newsletter_promo = Promo('newsletter', future_date)
    assert not newsletter_promo.expired


___ test_uses_property(
    assert 'property' __ inspect.getsource(Promo)