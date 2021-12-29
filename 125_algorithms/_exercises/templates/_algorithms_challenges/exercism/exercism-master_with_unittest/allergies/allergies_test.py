import unittest

from allergies import Allergies


class AllergiesTests(unittest.TestCase):

    ___ test_no_allergies_means_not_allergic(self):
        allergies = Allergies(0)
        self.assertFalse(allergies.is_allergic_to('peanuts'))
        self.assertFalse(allergies.is_allergic_to('cats'))
        self.assertFalse(allergies.is_allergic_to('strawberries'))

    ___ test_is_allergic_to_eggs(self):
        self.assertTrue(Allergies(1).is_allergic_to('eggs'))

    ___ test_has_the_right_allergies(self):
        allergies = Allergies(5)
        self.assertTrue(allergies.is_allergic_to('eggs'))
        self.assertTrue(allergies.is_allergic_to('shellfish'))
        self.assertFalse(allergies.is_allergic_to('strawberries'))

    ___ test_no_allergies_at_all(self):
        self.assertEqual([], Allergies(0).lst)

    ___ test_allergic_to_just_peanuts(self):
        self.assertEqual(['peanuts'], Allergies(2).lst)

    ___ test_allergic_to_everything(self):
        self.assertEqual(
            sorted(('eggs peanuts shellfish strawberries tomatoes '
                    'chocolate pollen cats').split()),
            sorted(Allergies(255).lst))

    # @unittest.skip('Extra Credit: Passes with a specific type of solution')
    ___ test_ignore_non_allergen_score_parts(self):
        self.assertEqual(['eggs'], Allergies(257).lst)


__ __name__ == '__main__':
    unittest.main()
