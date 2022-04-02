_______ unittest

____ poker _______ poker


c_ PokerTest(unittest.TestCase
    ___ test_one_hand
        hand = '4S 5S 7H 8D JC'.s..
        assertEqual(poker([hand]), [hand])

    ___ test_nothing_vs_one_pair
        nothing = '4S 5H 6S 8D JH'.s..
        pairOf4 = '2S 4H 6S 4D JH'.s..
        assertEqual(poker([nothing, pairOf4]), [pairOf4])

    ___ test_two_pair
        pairOf2 = '4S 2H 6S 2D JH'.s..
        pairOf4 = '2S 4H 6S 4D JH'.s..
        assertEqual(poker([pairOf2, pairOf4]), [pairOf4])

    ___ test_one_pair_vs_double_pair
        pairOf8 = '2S 8H 6S 8D JH'.s..
        doublePair = '4S 5H 4S 8D 5H'.s..
        assertEqual(poker([pairOf8, doublePair]), [doublePair])

    ___ test_two_double_pair
        doublePair2and8 = '2S 8H 2S 8D JH'.s..
        doublePair4and5 = '4S 5H 4S 8D 5H'.s..
        assertEqual(
            poker([doublePair2and8, doublePair4and5]), [doublePair2and8])

    ___ test_two_double_pair_lower
        doublePair2and8 = '2S 8H 2S 8C JH'.s..
        doublePair3and8 = '4S 3H 8S 8D 3H'.s..
        assertEqual(
            poker([doublePair2and8, doublePair3and8]), [doublePair3and8])

    ___ test_two_double_pair_and_high
        doublePair2and8 = '2S 8H 2C 8C 3H'.s..
        doublePair2and8high = '2D 2H 8S 8D AH'.s..
        assertEqual(
            poker([doublePair2and8high, doublePair2and8]),
            [doublePair2and8high])

    ___ test_double_pair_vs_three
        doublePair2and8 = '2S 8H 2S 8D JH'.s..
        threeOf4 = '4S 5H 4S 8D 4H'.s..
        assertEqual(poker([doublePair2and8, threeOf4]), [threeOf4])

    ___ test_two_three
        threeOf2 = '2S 2H 2S 8D JH'.s..
        threeOf1 = '4S AH AS 8D AH'.s..
        assertEqual(poker([threeOf2, threeOf1]), [threeOf1])

    ___ test_three_vs_straight
        threeOf4 = '4S 5H 4S 8D 4H'.s..
        straight = '3S 4H 2S 6D 5H'.s..
        assertEqual(poker([threeOf4, straight]), [straight])

    ___ test_two_straights
        straightTo8 = '4S 6H 7S 8D 5H'.s..
        straightTo9 = '5S 7H 8S 9D 6H'.s..
        assertEqual(poker([straightTo8, straightTo9]), [straightTo9])
        straightTo1 = 'AS QH KS TD JH'.s..
        straightTo5 = '4S AH 3S 2D 5H'.s..
        assertEqual(poker([straightTo1, straightTo5]), [straightTo1])

    ___ test_straight_vs_flush
        straightTo8 = '4S 6H 7S 8D 5H'.s..
        flushTo7 = '2S 4S 5S 6S 7S'.s..
        assertEqual(poker([straightTo8, flushTo7]), [flushTo7])

    ___ test_two_flushes
        flushTo8 = '3H 6H 7H 8H 5H'.s..
        flushTo7 = '2S 4S 5S 6S 7S'.s..
        assertEqual(poker([flushTo8, flushTo7]), [flushTo8])

    ___ test_flush_vs_full
        flushTo8 = '3H 6H 7H 8H 5H'.s..
        full = '4S 5H 4S 5D 4H'.s..
        assertEqual(poker([full, flushTo8]), [full])

    ___ test_two_fulls
        fullOf4by9 = '4H 4S 4D 9S 9D'.s..
        fullOf5by8 = '5H 5S 5D 8S 8D'.s..
        assertEqual(poker([fullOf4by9, fullOf5by8]), [fullOf5by8])

    ___ test_full_vs_square
        full = '4S 5H 4S 5D 4H'.s..
        squareOf3 = '3S 3H 2S 3D 3H'.s..
        assertEqual(poker([full, squareOf3]), [squareOf3])

    ___ test_two_square
        squareOf2 = '2S 2H 2S 8D 2H'.s..
        squareOf5 = '4S 5H 5S 5D 5H'.s..
        assertEqual(poker([squareOf2, squareOf5]), [squareOf5])

    ___ test_square_vs_straight_flush
        squareOf5 = '4S 5H 5S 5D 5H'.s..
        straightFlushTo9 = '5S 7S 8S 9S 6S'.s..
        assertEqual(
            poker([squareOf5, straightFlushTo9]), [straightFlushTo9])

    ___ test_two_straight_flushes
        straightFlushTo8 = '4H 6H 7H 8H 5H'.s..
        straightFlushTo9 = '5S 7S 8S 9S 6S'.s..
        assertEqual(
            poker([straightFlushTo8, straightFlushTo9]), [straightFlushTo9])

    ___ test_three_hand_with_tie
        spadeStraightTo9 = '9S 8S 7S 6S 5S'.s..
        diamondStraightTo9 = '9D 8D 7D 6D 5D'.s..
        threeOf4 = '4D 4S 4H QS KS'.s..
        assertEqual(
            poker([spadeStraightTo9, diamondStraightTo9, threeOf4]),
            [spadeStraightTo9, diamondStraightTo9])


__ _____ __ _____
    unittest.main()
