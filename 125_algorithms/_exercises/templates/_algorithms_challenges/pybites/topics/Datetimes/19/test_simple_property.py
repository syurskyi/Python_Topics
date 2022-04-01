____ d__ _______ t..
_______ i___

____ simple_property _______ Promo, NOW


___ test_promo_expired
    past_time = NOW - t..(seconds=3)
    twitter_promo = Promo('twitter', past_time)
    ... twitter_promo.expired


___ test_promo_not_expired
    future_date = NOW + t..(d.._1)
    newsletter_promo = Promo('newsletter', future_date)
    ... n.. newsletter_promo.expired


___ test_uses_property
    ... 'property' __ i___.getsource(Promo)