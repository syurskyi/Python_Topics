_______ i___
_______ r__

_______ p__

____ challenge _______ Challenge, BlogChallenge, BiteChallenge


___ test_should_not_instantiate_abc
    w__ p__.r.. T..
        ch = Challenge(0, 'Should not instantiate ABC')
        ch.number


___ test_baseclass_methods_are_abstract
    lines = [line.s.. ___ line __
             i___.getsourcelines(Challenge)[0]]
    verify_method = [(i, line) ___ i, line __
                     e..(lines)
                     __ 'def verify' __ line]
    ... verify_method, "Cannot find a method called verify"
    verify_index = verify_method[0][0]
    ... lines[verify_index - 1] __ "@abstractmethod"
    pretty_title_index = lines.i.. 'def pretty_title(self):')
    ... lines[pretty_title_index - 1] __ "@abstractmethod"


___ test_super_and_abst_method_implementation
    merged_prs = [41, 42, 44]
    ___
        blog = BlogChallenge(1, 'Wordvalues', merged_prs)
    ______ T..:
        p__.fail("Unexpected TypeError, missing methods/properties?")

    ... blog.verify(r__.c..(merged_prs
    ... n.. blog.verify(43)
    ... blog.pretty_title __ 'PCC1 - Wordvalues'


___ test_super_and_abst_property_implementation
    ___
        bite = BiteChallenge(24, 'ABC and class inheritance', 'my result')
    ______ T..:
        p__.fail("Unexpected TypeError, missing methods/properties?")

    ... bite.verify('my result')
    ... n.. bite.verify('other result')
    ... bite.pretty_title __ 'Bite 24. ABC and class inheritance'