from curry import rounder_int, rounder_detailed


def test_rounder_int_partial():
    a__ rounder_int(1.3434587383) == 1
    a__ rounder_int(10.42342) == 10
    a__ rounder_int(1.99) == 2


def test_rounder_detailed_partial():
    a__ rounder_detailed(1.344587383) == 1.3446
    a__ rounder_detailed(10.42342) == 10.4234
    a__ rounder_detailed(1.99) == 1.9900