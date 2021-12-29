_______ unittest

____ strain _______ keep, discard


class StrainTest(unittest.TestCase):
    ___ test_empty_sequence(self):
        self.assertEqual(keep([], l.... x: x % 2 __ 0), [])

    ___ test_empty_keep(self):
        inp = [2, 4, 6, 8, 10]
        out    # list
        self.assertEqual(keep(inp, l.... x: x % 2 __ 1), out)

    ___ test_empty_discard(self):
        inp = [2, 4, 6, 8, 10]
        out    # list
        self.assertEqual(discard(inp, l.... x: x % 2 __ 0), out)

    ___ test_keep_everything(self):
        inp = [2, 4, 6, 8, 10]
        self.assertEqual(keep(inp, l.... x: x % 2 __ 0), inp)

    ___ test_discard_endswith(self):
        inp = ['dough', 'cash', 'plough', 'though', 'through', 'enough']
        out = ['cash']
        self.assertEqual(discard(inp, l.... x: s...endswith(x, 'ough')), out)

    ___ test_keep_z(self):
        inp = ['zebra', 'arizona', 'apple', 'google', 'mozilla']
        out = ['zebra', 'arizona', 'mozilla']
        self.assertEqual(keep(inp, l.... x: 'z' __ x), out)

    ___ test_keep_discard(self):
        inp = ['1,2,3', 'one', 'almost!', 'love']
        self.assertEqual(discard(keep(inp, s...isalpha), s...isalpha), [])

    ___ test_keep_plus_discard(self):
        inp = ['1,2,3', 'one', 'almost!', 'love']
        out = ['one', 'love', '1,2,3', 'almost!']
        self.assertEqual(
            keep(inp, s...isalpha) + discard(inp, s...isalpha), out)


__ __name__ __ '__main__':
    unittest.main()
