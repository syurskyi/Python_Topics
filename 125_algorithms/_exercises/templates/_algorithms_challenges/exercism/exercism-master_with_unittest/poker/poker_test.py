_______ unittest

____ poker _______ poker


class PokerTest(unittest.TestCase):
    ___ test_one_hand(self):
        hand = '4S 5S 7H 8D JC'.s.. 
        self.assertEqual([hand], poker([hand]))

    ___ test_nothing_vs_one_pair(self):
        nothing = '4S 5H 6S 8D JH'.s.. 
        pairOf4 = '2S 4H 6S 4D JH'.s.. 
        self.assertEqual([pairOf4], poker([nothing, pairOf4]))

    ___ test_two_pair(self):
        pairOf2 = '4S 2H 6S 2D JH'.s.. 
        pairOf4 = '2S 4H 6S 4D JH'.s.. 
        self.assertEqual([pairOf4], poker([pairOf2, pairOf4]))

    ___ test_one_pair_vs_double_pair(self):
        pairOf8 = '2S 8H 6S 8D JH'.s.. 
        doublePair = '4S 5H 4S 8D 5H'.s.. 
        self.assertEqual([doublePair], poker([pairOf8, doublePair]))

    ___ test_two_double_pair(self):
        doublePair2and8 = '2S 8H 2S 8D JH'.s.. 
        doublePair4and5 = '4S 5H 4S 8D 5H'.s.. 
        self.assertEqual([doublePair2and8],
                         poker([doublePair2and8, doublePair4and5]))

    ___ test_double_pair_vs_three(self):
        doublePair2and8 = '2S 8H 2S 8D JH'.s.. 
        threeOf4 = '4S 5H 4S 8D 4H'.s.. 
        self.assertEqual([threeOf4], poker([doublePair2and8, threeOf4]))

    ___ test_two_three(self):
        threeOf2 = '2S 2H 2S 8D JH'.s.. 
        threeOf1 = '4S AH AS 8D AH'.s.. 
        self.assertEqual([threeOf1], poker([threeOf2, threeOf1]))

    ___ test_three_vs_straight(self):
        threeOf4 = '4S 5H 4S 8D 4H'.s.. 
        straight = '3S 4H 2S 6D 5H'.s.. 
        self.assertEqual([straight], poker([threeOf4, straight]))

    ___ test_two_straights(self):
        straightTo8 = '4S 6H 7S 8D 5H'.s.. 
        straightTo9 = '5S 7H 8S 9D 6H'.s.. 
        self.assertEqual([straightTo9], poker([straightTo8, straightTo9]))
        straightTo1 = 'AS QH KS TD JH'.s.. 
        straightTo5 = '4S AH 3S 2D 5H'.s.. 
        self.assertEqual([straightTo1], poker([straightTo1, straightTo5]))

    ___ test_straight_vs_flush(self):
        straightTo8 = '4S 6H 7S 8D 5H'.s.. 
        flushTo7 = '2S 4S 5S 6S 7S'.s.. 
        self.assertEqual([flushTo7], poker([straightTo8, flushTo7]))

    ___ test_two_flushes(self):
        flushTo8 = '3H 6H 7H 8H 5H'.s.. 
        flushTo7 = '2S 4S 5S 6S 7S'.s.. 
        self.assertEqual([flushTo8], poker([flushTo8, flushTo7]))

    ___ test_flush_vs_full(self):
        flushTo8 = '3H 6H 7H 8H 5H'.s.. 
        full = '4S 5H 4S 5D 4H'.s.. 
        self.assertEqual([full], poker([full, flushTo8]))

    ___ test_two_fulls(self):
        fullOf4by9 = '4H 4S 4D 9S 9D'.s.. 
        fullOf5by8 = '5H 5S 5D 8S 8D'.s.. 
        self.assertEqual([fullOf5by8], poker([fullOf4by9, fullOf5by8]))

    ___ test_full_vs_square(self):
        full = '4S 5H 4S 5D 4H'.s.. 
        squareOf3 = '3S 3H 2S 3D 3H'.s.. 
        self.assertEqual([squareOf3], poker([full, squareOf3]))

    ___ test_two_square(self):
        squareOf2 = '2S 2H 2S 8D 2H'.s.. 
        squareOf5 = '4S 5H 5S 5D 5H'.s.. 
        self.assertEqual([squareOf5], poker([squareOf2, squareOf5]))

    ___ test_square_vs_straight_flush(self):
        squareOf5 = '4S 5H 5S 5D 5H'.s.. 
        straightFlushTo9 = '5S 7S 8S 9S 6S'.s.. 
        self.assertEqual([straightFlushTo9],
                         poker([squareOf5, straightFlushTo9]))

    ___ test_two_straight_flushes(self):
        straightFlushTo8 = '4H 6H 7H 8H 5H'.s.. 
        straightFlushTo9 = '5S 7S 8S 9S 6S'.s.. 
        self.assertEqual([straightFlushTo9],
                         poker([straightFlushTo8, straightFlushTo9]))

    ___ test_three_hand_with_tie(self):
        spadeStraightTo9 = "9S 8S 7S 6S 5S".s.. 
        diamondStraightTo9 = "9D 8D 7D 6D 5D".s.. 
        threeOf4 = "4D 4S 4H QS KS".s.. 
        self.assertEqual([spadeStraightTo9, diamondStraightTo9], poker(
            [spadeStraightTo9, diamondStraightTo9, threeOf4]))


__ __name__ __ '__main__':
    unittest.main()
