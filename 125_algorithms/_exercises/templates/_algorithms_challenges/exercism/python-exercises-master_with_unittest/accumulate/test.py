_______ unittest

____ accumulate _______ accumulate


c_ AccumulateTest(unittest.TestCase
    ___ test_empty_sequence
        assertEqual(accumulate([], l.... x: x / 2), [])

    ___ test_pow
        assertEqual(
            accumulate([1, 2, 3, 4, 5], l.... x: x * x), [1, 4, 9, 16, 25])

    ___ test_divmod
        assertEqual(
            accumulate([10, 17, 23], l.... x: divmod(x, 7,
            [(1, 3), (2, 3), (3, 2)])

    ___ test_composition
        inp = [10, 17, 23]
        assertEqual(
            accumulate(
                accumulate(inp, l.... x: divmod(x, 7,
                l.... x: 7 * x[0] + x[1]), inp)

    ___ test_capitalize
        assertEqual(
            accumulate( 'hello', 'world' , s...upper),  'HELLO', 'WORLD' )

    ___ test_recursive
        inp =  'a', 'b', 'c'
        out = [['a1', 'a2', 'a3' ,  'b1', 'b2', 'b3' ,  'c1', 'c2', 'c3']]
        assertEqual(
            accumulate(
                inp, l.... x: accumulate(l..('123'), l.... y: x + y, out)


__ _____ __ _____
    unittest.main()
