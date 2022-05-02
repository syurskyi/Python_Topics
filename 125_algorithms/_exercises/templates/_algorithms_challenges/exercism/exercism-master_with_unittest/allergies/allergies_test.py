_______ unittest

____ allergies _______ Allergies


c_ AllergiesTests(unittest.TestCase

    ___ test_no_allergies_means_not_allergic
        allergies Allergies(0)
        assertFalse(allergies.is_allergic_to('peanuts'
        assertFalse(allergies.is_allergic_to('cats'
        assertFalse(allergies.is_allergic_to('strawberries'

    ___ test_is_allergic_to_eggs
        assertTrue(Allergies(1).is_allergic_to('eggs'

    ___ test_has_the_right_allergies
        allergies Allergies(5)
        assertTrue(allergies.is_allergic_to('eggs'
        assertTrue(allergies.is_allergic_to('shellfish'
        assertFalse(allergies.is_allergic_to('strawberries'

    ___ test_no_allergies_at_all
        assertEqual(   # list, Allergies(0).lst)

    ___ test_allergic_to_just_peanuts
        assertEqual( 'peanuts' , Allergies(2).lst)

    ___ test_allergic_to_everything
        assertEqual(
            s..(('eggs peanuts shellfish strawberries tomatoes '
                    'chocolate pollen cats').s..,
            s..(Allergies(255).lst

    # @unittest.skip('Extra Credit: Passes with a specific type of solution')
    ___ test_ignore_non_allergen_score_parts
        assertEqual( 'eggs' , Allergies(257).lst)


__ _____ __ _____
    unittest.main()
