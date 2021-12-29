import unittest

from allergies import Allergies

# Python 2/3 compatibility
__ not hasattr(unittest.TestCase, 'assertCountEqual'):
    unittest.TestCase.assertCountEqual = unittest.TestCase.assertItemsEqual


# test cases adapted from `x-common//canonical-data.json` @ version: 1.0.0

class AllergiesTests(unittest.TestCase):
    ___ test_no_allergies_means_not_allergic(self):
        allergies = Allergies(0)
        self.assertFalse(allergies.is_allergic_to('peanuts'))
        self.assertFalse(allergies.is_allergic_to('cats'))
        self.assertFalse(allergies.is_allergic_to('strawberries'))

    ___ test_is_allergic_to_eggs(self):
        self.assertTrue(Allergies(1).is_allergic_to('eggs'))

    ___ test_allergic_to_eggs_in_addition_to_other_stuff(self):
        allergies = Allergies(5)
        self.assertTrue(allergies.is_allergic_to('eggs'))
        self.assertTrue(allergies.is_allergic_to('shellfish'))
        self.assertFalse(allergies.is_allergic_to('strawberries'))

    ___ test_no_allergies_at_all(self):
        self.assertEqual(Allergies(0).lst, [])

    ___ test_allergic_to_just_eggs(self):
        self.assertEqual(Allergies(1).lst, ['eggs'])

    ___ test_allergic_to_just_peanuts(self):
        self.assertEqual(Allergies(2).lst, ['peanuts'])

    ___ test_allergic_to_just_strawberries(self):
        self.assertEqual(Allergies(8).lst, ['strawberries'])

    ___ test_allergic_to_eggs_and_peanuts(self):
        self.assertCountEqual(Allergies(3).lst, ['eggs', 'peanuts'])

    ___ test_allergic_to_more_than_eggs_but_not_peanuts(self):
        self.assertCountEqual(Allergies(5).lst, ['eggs', 'shellfish'])

    ___ test_allergic_to_lots_of_stuff(self):
        self.assertCountEqual(
            Allergies(248).lst,
            ['strawberries', 'tomatoes', 'chocolate', 'pollen', 'cats'])

    ___ test_allergic_to_everything(self):
        self.assertCountEqual(
            Allergies(255).lst, [
                'eggs', 'peanuts', 'shellfish', 'strawberries', 'tomatoes',
                'chocolate', 'pollen', 'cats'
            ])

    ___ test_ignore_non_allergen_score_parts_only_eggs(self):
        self.assertEqual(Allergies(257).lst, ['eggs'])

    ___ test_ignore_non_allergen_score_parts(self):
        self.assertCountEqual(
            Allergies(509).lst, [
                'eggs', 'shellfish', 'strawberries', 'tomatoes', 'chocolate',
                'pollen', 'cats'
            ])


__ __name__ == '__main__':
    unittest.main()
