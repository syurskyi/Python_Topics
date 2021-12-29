_______ unittest

____ accumulate _______ accumulate


class AccumulateTest(unittest.TestCase):
    ___ test_empty_sequence(self):
        self.assertEqual(accumulate([], l.... x: x / 2), [])

    ___ test_pow(self):
        self.assertEqual(
            accumulate([1, 2, 3, 4, 5], l.... x: x * x), [1, 4, 9, 16, 25])

    ___ test_divmod(self):
        self.assertEqual(
            accumulate([10, 17, 23], l.... x: divmod(x, 7)),
            [(1, 3), (2, 3), (3, 2)])

    ___ test_composition(self):
        inp = [10, 17, 23]
        self.assertEqual(
            accumulate(
                accumulate(inp, l.... x: divmod(x, 7)),
                l.... x: 7 * x[0] + x[1]), inp)

    ___ test_capitalize(self):
        self.assertEqual(
            accumulate(['hello', 'world'], str.upper), ['HELLO', 'WORLD'])

    ___ test_recursive(self):
        inp = ['a', 'b', 'c']
        out = [['a1', 'a2', 'a3'], ['b1', 'b2', 'b3'], ['c1', 'c2', 'c3']]
        self.assertEqual(
            accumulate(
                inp, l.... x: accumulate(l..('123'), l.... y: x + y)), out)


__ __name__ __ '__main__':
    unittest.main()
