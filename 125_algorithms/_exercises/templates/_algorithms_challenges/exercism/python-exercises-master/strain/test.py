______ unittest

from strain ______ keep, discard


class StrainTest(unittest.TestCase
    ___ test_empty_sequence(self
        self.assertEqual(keep([], lambda x: x % 2 __ 0), [])

    ___ test_empty_keep(self
        inp = [2, 4, 6, 8, 10]
        out = []
        self.assertEqual(keep(inp, lambda x: x % 2 __ 1), out)

    ___ test_empty_discard(self
        inp = [2, 4, 6, 8, 10]
        out = []
        self.assertEqual(discard(inp, lambda x: x % 2 __ 0), out)

    ___ test_keep_everything(self
        inp = [2, 4, 6, 8, 10]
        self.assertEqual(keep(inp, lambda x: x % 2 __ 0), inp)

    ___ test_discard_endswith(self
        inp = ['dough', 'cash', 'plough', 'though', 'through', 'enough']
        out = ['cash']
        self.assertEqual(discard(inp, lambda x: str.endswith(x, 'ough')), out)

    ___ test_keep_z(self
        inp = ['zebra', 'arizona', 'apple', 'google', 'mozilla']
        out = ['zebra', 'arizona', 'mozilla']
        self.assertEqual(keep(inp, lambda x: 'z' in x), out)

    ___ test_keep_discard(self
        inp = ['1,2,3', 'one', 'almost!', 'love']
        self.assertEqual(discard(keep(inp, str.isalpha), str.isalpha), [])

    ___ test_keep_plus_discard(self
        inp = ['1,2,3', 'one', 'almost!', 'love']
        out = ['one', 'love', '1,2,3', 'almost!']
        self.assertEqual(
            keep(inp, str.isalpha) + discard(inp, str.isalpha), out)


__ __name__ __ '__main__':
    unittest.main()
