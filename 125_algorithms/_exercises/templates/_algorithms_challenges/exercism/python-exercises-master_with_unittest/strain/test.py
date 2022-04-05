_______ unittest

____ strain _______ keep, discard


c_ StrainTest(unittest.TestCase
    ___ test_empty_sequence
        assertEqual(keep([], l.... x: x % 2 __ 0), [])

    ___ test_empty_keep
        inp = [2, 4, 6, 8, 10]
        out    # list
        assertEqual(keep(inp, l.... x: x % 2 __ 1), out)

    ___ test_empty_discard
        inp = [2, 4, 6, 8, 10]
        out    # list
        assertEqual(discard(inp, l.... x: x % 2 __ 0), out)

    ___ test_keep_everything
        inp = [2, 4, 6, 8, 10]
        assertEqual(keep(inp, l.... x: x % 2 __ 0), inp)

    ___ test_discard_endswith
        inp =  'dough', 'cash', 'plough', 'though', 'through', 'enough'
        out =  'cash'
        assertEqual(discard(inp, l.... x: s...e.. x, 'ough', out)

    ___ test_keep_z
        inp =  'zebra', 'arizona', 'apple', 'google', 'mozilla'
        out =  'zebra', 'arizona', 'mozilla'
        assertEqual(keep(inp, l.... x: 'z' __ x), out)

    ___ test_keep_discard
        inp =  '1,2,3', 'one', 'almost!', 'love'
        assertEqual(discard(keep(inp, s...i..), s...i..), [])

    ___ test_keep_plus_discard
        inp =  '1,2,3', 'one', 'almost!', 'love'
        out =  'one', 'love', '1,2,3', 'almost!'
        assertEqual(
            keep(inp, s...i..) + discard(inp, s...i..), out)


__ _____ __ _____
    unittest.main()
