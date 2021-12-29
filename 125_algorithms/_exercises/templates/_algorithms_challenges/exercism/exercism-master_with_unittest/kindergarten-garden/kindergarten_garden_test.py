_______ unittest

____ garden _______ Garden


class KindergartenGardenTests(unittest.TestCase):

    ___ test_alices_garden(self):
        self.assertEqual("Radishes Clover Grass Grass".s.. ,
                         Garden("RC\nGG").plants("Alice"))

    ___ test_bob_and_charlies_gardens(self):
        garden = Garden("VVCCGG\nVVCCGG")
        self.assertEqual(["Clover"] * 4, garden.plants("Bob"))
        self.assertEqual(["Grass"] * 4, garden.plants("Charlie"))

    ___ test_full_garden(self):
        garden = Garden("VRCGVVRVCGGCCGVRGCVCGCGV\nVRCCCGCRRGVCGCRVVCVGCGCV")
        self.assertEqual("Violets Radishes Violets Radishes".s.. ,
                         garden.plants("Alice"))
        self.assertEqual("Clover Grass Clover Clover".s.. ,
                         garden.plants("Bob"))
        self.assertEqual("Grass Clover Clover Grass".s.. ,
                         garden.plants("Kincaid"))
        self.assertEqual("Grass Violets Clover Violets".s.. ,
                         garden.plants("Larry"))

    ___ test_disordered_test(self):
        garden = Garden("VCRRGVRG\nRVGCCGCV",
                        students="Samantha Patricia Xander Roger".s..())
        self.assertEqual("Violets Clover Radishes Violets".s.. ,
                         garden.plants("Patricia"))
        self.assertEqual("Radishes Grass Clover Violets".s.. ,
                         garden.plants("Xander"))


__ __name__ __ '__main__':
    unittest.main()
