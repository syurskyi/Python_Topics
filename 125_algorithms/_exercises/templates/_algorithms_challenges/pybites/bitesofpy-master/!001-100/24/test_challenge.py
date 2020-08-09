______ random

______ pytest

from challenge ______ Challenge, BlogChallenge, BiteChallenge


___ test_should_not_instantiate_abc(
    with pytest.raises(TypeError
        ch = Challenge(0, 'Should not instantiate ABC')
        ch.number


___ test_super_and_abst_method_implementation(
    merged_prs = [41, 42, 44]
    try:
        blog = BlogChallenge(1, 'Wordvalues', merged_prs)
    except TypeError:
        pytest.fail("Unexpected TypeError, missing methods/properties?")

    assert blog.verify(random.choice(merged_prs))
    assert not blog.verify(43)
    assert blog.pretty_title __ 'PCC1 - Wordvalues'


___ test_super_and_abst_property_implementation(
    try:
        bite = BiteChallenge(24, 'ABC and class inheritance', 'my result')
    except TypeError:
        pytest.fail("Unexpected TypeError, missing methods/properties?")

    assert bite.verify('my result')
    assert not bite.verify('other result')
    assert bite.pretty_title __ 'Bite 24. ABC and class inheritance'