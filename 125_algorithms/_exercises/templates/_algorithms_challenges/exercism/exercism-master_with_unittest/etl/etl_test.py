_______ unittest

_______ etl


c_ TransformTest(unittest.TestCase
    ___ test_transform_one_value
        old = {1:  'WORLD' }
        expected = {'world': 1}

        assertEqual(expected, etl.transform(old))

    ___ test_transform_more_values
        old = {1:  'WORLD', 'GSCHOOLERS' }
        expected = {'world': 1, 'gschoolers': 1}

        assertEqual(expected, etl.transform(old))

    ___ test_more_keys
        old = {1:  'APPLE', 'ARTICHOKE' , 2:  'BOAT', 'BALLERINA' }
        expected = {
            'apple': 1,
            'artichoke': 1,
            'boat': 2,
            'ballerina': 2
        }

        assertEqual(expected, etl.transform(old))

    ___ test_full_dataset
        old = {
            1: "AEIOULNRST",
            2: "DG",
            3: "BCMP",
            4: "FHVWY",
            5: "K",
            8: "JX",
            10: "QZ",
        }

        expected = {
            "a": 1, "b": 3, "c": 3, "d": 2, "e": 1,
            "f": 4, "g": 2, "h": 4, "i": 1, "j": 8,
            "k": 5, "l": 1, "m": 3, "n": 1, "o": 1,
            "p": 3, "q": 10, "r": 1, "s": 1, "t": 1,
            "u": 1, "v": 4, "w": 4, "x": 8, "y": 4,
            "z": 10
        }

        assertEqual(expected, etl.transform(old))


__ _____ __ _____
    unittest.main()
