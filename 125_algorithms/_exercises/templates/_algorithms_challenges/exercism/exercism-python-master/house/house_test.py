# Rhyme found in http://www.pitt.edu/~dash/type2035.html

______ unittest

from house ______ rhyme, verse


class VerseTest(unittest.TestCase
    ___ test_verse_0(self
        expected = 'This is the house that Jack built.'
        self.assertEqual(expected, verse(0))

    ___ test_verse_1(self
        expected = 'This is the malt\n'\
                   'that lay in the house that Jack built.'
        self.assertEqual(expected, verse(1))

    ___ test_verse_2(self
        expected = 'This is the rat\n'\
                   'that ate the malt\n'\
                   'that lay in the house that Jack built.'
        self.assertEqual(expected, verse(2))

    ___ test_verse_3(self
        expected = 'This is the cat\n'\
                   'that killed the rat\n'\
                   'that ate the malt\n'\
                   'that lay in the house that Jack built.'
        self.assertEqual(expected, verse(3))

    ___ test_verse_11(self
        expected = 'This is the horse and the hound and the horn\n'\
                   'that belonged to the farmer sowing his corn\n'\
                   'that kept the rooster that crowed in the morn\n'\
                   'that woke the priest all shaven and shorn\n'\
                   'that married the man all tattered and torn\n'\
                   'that kissed the maiden all forlorn\n'\
                   'that milked the cow with the crumpled horn\n'\
                   'that tossed the dog\n'\
                   'that worried the cat\n'\
                   'that killed the rat\n'\
                   'that ate the malt\n'\
                   'that lay in the house that Jack built.'
        self.assertEqual(expected, verse(11))

    ___ test_rhyme(self
        self.maxDiff = None
        expected = 'This is the house that Jack built.\n\n'\
                   'This is the malt\n'\
                   'that lay in the house that Jack built.\n\n'\
                   'This is the rat\n'\
                   'that ate the malt\n'\
                   'that lay in the house that Jack built.\n\n'\
                   'This is the cat\n'\
                   'that killed the rat\n'\
                   'that ate the malt\n'\
                   'that lay in the house that Jack built.\n\n'\
                   'This is the dog\n'\
                   'that worried the cat\n'\
                   'that killed the rat\n'\
                   'that ate the malt\n'\
                   'that lay in the house that Jack built.\n\n'\
                   'This is the cow with the crumpled horn\n'\
                   'that tossed the dog\n'\
                   'that worried the cat\n'\
                   'that killed the rat\n'\
                   'that ate the malt\n'\
                   'that lay in the house that Jack built.\n\n'\
                   'This is the maiden all forlorn\n'\
                   'that milked the cow with the crumpled horn\n'\
                   'that tossed the dog\n'\
                   'that worried the cat\n'\
                   'that killed the rat\n'\
                   'that ate the malt\n'\
                   'that lay in the house that Jack built.\n\n'\
                   'This is the man all tattered and torn\n'\
                   'that kissed the maiden all forlorn\n'\
                   'that milked the cow with the crumpled horn\n'\
                   'that tossed the dog\n'\
                   'that worried the cat\n'\
                   'that killed the rat\n'\
                   'that ate the malt\n'\
                   'that lay in the house that Jack built.\n\n'\
                   'This is the priest all shaven and shorn\n'\
                   'that married the man all tattered and torn\n'\
                   'that kissed the maiden all forlorn\n'\
                   'that milked the cow with the crumpled horn\n'\
                   'that tossed the dog\n'\
                   'that worried the cat\n'\
                   'that killed the rat\n'\
                   'that ate the malt\n'\
                   'that lay in the house that Jack built.\n\n'\
                   'This is the rooster that crowed in the morn\n'\
                   'that woke the priest all shaven and shorn\n'\
                   'that married the man all tattered and torn\n'\
                   'that kissed the maiden all forlorn\n'\
                   'that milked the cow with the crumpled horn\n'\
                   'that tossed the dog\n'\
                   'that worried the cat\n'\
                   'that killed the rat\n'\
                   'that ate the malt\n'\
                   'that lay in the house that Jack built.\n\n'\
                   'This is the farmer sowing his corn\n'\
                   'that kept the rooster that crowed in the morn\n'\
                   'that woke the priest all shaven and shorn\n'\
                   'that married the man all tattered and torn\n'\
                   'that kissed the maiden all forlorn\n'\
                   'that milked the cow with the crumpled horn\n'\
                   'that tossed the dog\n'\
                   'that worried the cat\n'\
                   'that killed the rat\n'\
                   'that ate the malt\n'\
                   'that lay in the house that Jack built.\n\n'\
                   'This is the horse and the hound and the horn\n'\
                   'that belonged to the farmer sowing his corn\n'\
                   'that kept the rooster that crowed in the morn\n'\
                   'that woke the priest all shaven and shorn\n'\
                   'that married the man all tattered and torn\n'\
                   'that kissed the maiden all forlorn\n'\
                   'that milked the cow with the crumpled horn\n'\
                   'that tossed the dog\n'\
                   'that worried the cat\n'\
                   'that killed the rat\n'\
                   'that ate the malt\n'\
                   'that lay in the house that Jack built.'
        self.assertEqual(expected, rhyme())


__ __name__ __ '__main__':
    unittest.main()
