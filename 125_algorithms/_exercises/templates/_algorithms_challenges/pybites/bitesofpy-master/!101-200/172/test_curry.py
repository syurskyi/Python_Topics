from curry ______ rounder_int, rounder_detailed


___ test_rounder_int_partial(
    assert rounder_int(1.3434587383) __ 1
    assert rounder_int(10.42342) __ 10
    assert rounder_int(1.99) __ 2


___ test_rounder_detailed_partial(
    assert rounder_detailed(1.344587383) __ 1.3446
    assert rounder_detailed(10.42342) __ 10.4234
    assert rounder_detailed(1.99) __ 1.9900