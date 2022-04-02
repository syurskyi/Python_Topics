_______ unittest

____ garden _______ Garden


c_ KindergartenGardenTests(unittest.TestCase

    ___ test_alices_garden
        assertEqual("Radishes Clover Grass Grass".s.. ,
                         Garden("RC\nGG").plants("Alice"))

    ___ test_bob_and_charlies_gardens
        garden = Garden("VVCCGG\nVVCCGG")
        assertEqual(["Clover"] * 4, garden.plants("Bob"))
        assertEqual(["Grass"] * 4, garden.plants("Charlie"))

    ___ test_full_garden
        garden = Garden("VRCGVVRVCGGCCGVRGCVCGCGV\nVRCCCGCRRGVCGCRVVCVGCGCV")
        assertEqual("Violets Radishes Violets Radishes".s.. ,
                         garden.plants("Alice"))
        assertEqual("Clover Grass Clover Clover".s.. ,
                         garden.plants("Bob"))
        assertEqual("Grass Clover Clover Grass".s.. ,
                         garden.plants("Kincaid"))
        assertEqual("Grass Violets Clover Violets".s.. ,
                         garden.plants("Larry"))

    ___ test_disordered_test
        garden = Garden("VCRRGVRG\nRVGCCGCV",
                        students="Samantha Patricia Xander Roger".s..
        assertEqual("Violets Clover Radishes Violets".s.. ,
                         garden.plants("Patricia"))
        assertEqual("Radishes Grass Clover Violets".s.. ,
                         garden.plants("Xander"))


__ _____ __ _____
    unittest.main()
