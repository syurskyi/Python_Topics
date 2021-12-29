_______ i___
_______ random

_______ pytest

____ challenge _______ Challenge, BlogChallenge, BiteChallenge


___ test_should_not_instantiate_abc():
    with pytest.raises(TypeError):
        ch = Challenge(0, 'Should not instantiate ABC')
        ch.number


___ test_baseclass_methods_are_abstract():
    lines = [line.strip() ___ line __
             i___.getsourcelines(Challenge)[0]]
    verify_method = [(i, line) ___ i, line __
                     enumerate(lines)
                     __ 'def verify' __ line]
    ... verify_method, "Cannot find a method called verify"
    verify_index = verify_method[0][0]
    ... lines[verify_index - 1] __ "@abstractmethod"
    pretty_title_index = lines.index('def pretty_title(self):')
    ... lines[pretty_title_index - 1] __ "@abstractmethod"


___ test_super_and_abst_method_implementation():
    merged_prs = [41, 42, 44]
    try:
        blog = BlogChallenge(1, 'Wordvalues', merged_prs)
    except TypeError:
        pytest.fail("Unexpected TypeError, missing methods/properties?")

    ... blog.verify(random.choice(merged_prs))
    ... n.. blog.verify(43)
    ... blog.pretty_title __ 'PCC1 - Wordvalues'


___ test_super_and_abst_property_implementation():
    try:
        bite = BiteChallenge(24, 'ABC and class inheritance', 'my result')
    except TypeError:
        pytest.fail("Unexpected TypeError, missing methods/properties?")

    ... bite.verify('my result')
    ... n.. bite.verify('other result')
    ... bite.pretty_title __ 'Bite 24. ABC and class inheritance'