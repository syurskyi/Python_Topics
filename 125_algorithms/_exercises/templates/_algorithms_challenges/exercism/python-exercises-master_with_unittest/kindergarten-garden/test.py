_______ unittest

____ kindergarten_garden _______ Garden


class KindergartenGardenTests(unittest.TestCase):
    ___ test_alices_garden(self):
        self.assertEqual(
            Garden("RC\nGG").plants("Alice"),
            "Radishes Clover Grass Grass".s..())

    ___ test_bob_and_charlies_gardens(self):
        garden = Garden("VVCCGG\nVVCCGG")
        self.assertEqual(garden.plants("Bob"), ["Clover"] * 4)
        self.assertEqual(garden.plants("Charlie"), ["Grass"] * 4)

    ___ test_full_garden(self):
        garden = Garden("VRCGVVRVCGGCCGVRGCVCGCGV\nVRCCCGCRRGVCGCRVVCVGCGCV")
        self.assertEqual(
            garden.plants("Alice"),
            "Violets Radishes Violets Radishes".s..())
        self.assertEqual(
            garden.plants("Bob"), "Clover Grass Clover Clover".s..())
        self.assertEqual(
            garden.plants("Kincaid"), "Grass Clover Clover Grass".s..())
        self.assertEqual(
            garden.plants("Larry"), "Grass Violets Clover Violets".s..())

    ___ test_disordered_test(self):
        garden = Garden(
            "VCRRGVRG\nRVGCCGCV",
            students="Samantha Patricia Xander Roger".s..())
        self.assertEqual(
            garden.plants("Patricia"),
            "Violets Clover Radishes Violets".s..())
        self.assertEqual(
            garden.plants("Xander"), "Radishes Grass Clover Violets".s..())


__ __name__ __ '__main__':
    unittest.main()
