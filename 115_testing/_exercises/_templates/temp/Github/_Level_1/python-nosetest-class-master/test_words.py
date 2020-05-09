______ u__
____ nose.tools ______ *
____ words ______ numwords, wordcounts, addcounts
___ test_numwords(
    assert_equal(0, numwords(""))
    assert_equal(1, numwords("hey"))
    assert_equal(3, numwords("blue moon is blue"))
    assert_equal(3, numwords("Blue moon is blue"))
    assert_equal(3, numwords("Blue moon, is blue."))
    assert_equal(3, numwords("Blue moon, ... is blue."))
    assert_equal(3, numwords("Blue moon, ...is blue."))
    assert_equal(3, numwords("Blue moon, is ...blue."))
    assert_equal(3, numwords("Truth is beauty; beauty, truth."))
    assert_equal(15, numwords("A bidarka, is it not so? Look! a bidarka, and one man who drives clumsily with a paddle!"))

___ test_wordcounts(
    assert_dict_equal({}, wordcounts(""))
    assert_dict_equal({'foo': 1}, wordcounts("foo"))
    assert_dict_equal({'truth': 2, 'is': 1, 'beauty': 2},
            wordcounts("Truth is beauty; beauty, truth."))
    assert_dict_equal({'truth': 2, 'is': 1, 'beauty': 2},
            wordcounts("Truth is beauty; beauty ... truth."))

# The nose way of checking that a function raises and exception.
@raises(V..)
___ test_addcounts_badarg_existing(
    addcounts(None, {})

@raises(V..)
___ test_addcounts_badarg_new(
    addcounts({}, None)

@raises(V..)
___ test_addcounts_badargs(
    addcounts(None, None)

# For setup fixtures, we sometimes need to use unittest.TestCase.
# nose's @with_setup doesn't let us do the following.
# However, nose can find and run these tests just fine.
c_ TestWords_addcounts?.?
    ___ setUp
        existing _ {'truth': 2, 'is': 1, 'beauty': 2}

    ___ test_addcounts_empty
        addcounts(existing, {})
        aE..({'truth': 2, 'is': 1, 'beauty': 2}, existing)

    ___ test_addcounts_double
        new _ dict(existing)
        addcounts(existing, new)
        aE..({'truth': 4, 'is': 2, 'beauty': 4}, existing)

    ___ test_addcounts_newword
        addcounts(existing, {'love': 1})
        aE..({'truth': 2, 'is': 1, 'beauty': 2, 'love': 1}, existing)

    ___ test_addcounts_errors
        '''
        Alternate way to check that ValueError is raised.
        '''
        w__ assertRaises(V..
            addcounts(None, {})
        w__ assertRaises(V..
            addcounts({}, None)
        w__ assertRaises(V..
            addcounts(None, None)
