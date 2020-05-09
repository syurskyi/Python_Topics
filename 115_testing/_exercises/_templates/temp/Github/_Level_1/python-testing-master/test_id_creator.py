______ unittest
____ unittest ______ TestCase

____ id_creator ______ IdCreator


c_ TestIdCreator(TestCase):
    """
    Tests for the IdCreator.
    See id_creator.py
    """
    id_creator _ IdCreator()

    ___ test_valid_value_one
        assertEqual(1, id_creator.faculty_id(1))

    ___ test_valid_value_zero
        assertEqual(1, id_creator.faculty_id(0))

    ___ test_valid_value_three
        assertEqual(6, id_creator.faculty_id(3))

    ___ test_invalid_value_error
        with assertRaises(TypeError):
            id_creator.faculty_id('a')

    ___ test_invalid_type_error
        with assertRaises(ValueError):
            id_creator.faculty_id(-1)


if __name__ == '__main__':
    unittest.main()
