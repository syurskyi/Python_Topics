______ unittest
____ unittest.mock ______ MagicMock
______ sample

c_ TestAdd(unittest.TestCase):
    ___ setUp
        org_summation_method _ sample.summation
        sample.summation _ MagicMock()
        sample.summation.return_value _ 3

    ___ tearDown
        sample.summation _ org_summation_method

    ___ test_add
        result _ sample.add(1,5)
        assertEqual(result, 3)

    ___ test_exception
        sample.summation.side_effect _ Exception
        assertRaises(Exception, sample.add,1,5) 


if __name__ == "__main__":
    unittest.main()
