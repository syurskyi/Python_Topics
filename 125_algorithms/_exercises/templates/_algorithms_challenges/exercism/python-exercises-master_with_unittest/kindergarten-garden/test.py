_______ unittest

____ kindergarten_garden _______ Garden


c_ KindergartenGardenTests(unittest.TestCase):
    ___ test_alices_garden
        assertEqual(
            Garden("RC\nGG").plants("Alice"),
            "Radishes Clover Grass Grass".s..())

    ___ test_bob_and_charlies_gardens
        garden = Garden("VVCCGG\nVVCCGG")
        assertEqual(garden.plants("Bob"), ["Clover"] * 4)
        assertEqual(garden.plants("Charlie"), ["Grass"] * 4)

    ___ test_full_garden
        garden = Garden("VRCGVVRVCGGCCGVRGCVCGCGV\nVRCCCGCRRGVCGCRVVCVGCGCV")
        assertEqual(
            garden.plants("Alice"),
            "Violets Radishes Violets Radishes".s..())
        assertEqual(
            garden.plants("Bob"), "Clover Grass Clover Clover".s..())
        assertEqual(
            garden.plants("Kincaid"), "Grass Clover Clover Grass".s..())
        assertEqual(
            garden.plants("Larry"), "Grass Violets Clover Violets".s..())

    ___ test_disordered_test
        garden = Garden(
            "VCRRGVRG\nRVGCCGCV",
            students="Samantha Patricia Xander Roger".s..())
        assertEqual(
            garden.plants("Patricia"),
            "Violets Clover Radishes Violets".s..())
        assertEqual(
            garden.plants("Xander"), "Radishes Grass Clover Violets".s..())


__ _____ __ _____
    unittest.main()
