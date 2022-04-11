_______ unittest

____ allergies _______ Allergies

# Python 2/3 compatibility
__ n.. hasattr(unittest.TestCase, 'assertCountEqual'
    unittest.TestCase.assertCountEqual unittest.TestCase.assertItemsEqual


# test cases adapted from `x-common//canonical-data.json` @ version: 1.0.0

c_ AllergiesTests(unittest.TestCase
    ___ test_no_allergies_means_not_allergic
        allergies Allergies(0)
        assertFalse(allergies.is_allergic_to('peanuts'
        assertFalse(allergies.is_allergic_to('cats'
        assertFalse(allergies.is_allergic_to('strawberries'

    ___ test_is_allergic_to_eggs
        assertTrue(Allergies(1).is_allergic_to('eggs'

    ___ test_allergic_to_eggs_in_addition_to_other_stuff
        allergies Allergies(5)
        assertTrue(allergies.is_allergic_to('eggs'
        assertTrue(allergies.is_allergic_to('shellfish'
        assertFalse(allergies.is_allergic_to('strawberries'

    ___ test_no_allergies_at_all
        assertEqual(Allergies(0).lst, [])

    ___ test_allergic_to_just_eggs
        assertEqual(Allergies(1).lst,  'eggs' )

    ___ test_allergic_to_just_peanuts
        assertEqual(Allergies(2).lst,  'peanuts' )

    ___ test_allergic_to_just_strawberries
        assertEqual(Allergies(8).lst,  'strawberries' )

    ___ test_allergic_to_eggs_and_peanuts
        assertCountEqual(Allergies(3).lst,  'eggs', 'peanuts' )

    ___ test_allergic_to_more_than_eggs_but_not_peanuts
        assertCountEqual(Allergies(5).lst,  'eggs', 'shellfish' )

    ___ test_allergic_to_lots_of_stuff
        assertCountEqual(
            Allergies(248).lst,
             'strawberries', 'tomatoes', 'chocolate', 'pollen', 'cats' )

    ___ test_allergic_to_everything
        assertCountEqual(
            Allergies(255).lst, [
                'eggs', 'peanuts', 'shellfish', 'strawberries', 'tomatoes',
                'chocolate', 'pollen', 'cats'
            ])

    ___ test_ignore_non_allergen_score_parts_only_eggs
        assertEqual(Allergies(257).lst,  'eggs' )

    ___ test_ignore_non_allergen_score_parts
        assertCountEqual(
            Allergies(509).lst, [
                'eggs', 'shellfish', 'strawberries', 'tomatoes', 'chocolate',
                'pollen', 'cats'
            ])


__ _____ __ _____
    unittest.main()
