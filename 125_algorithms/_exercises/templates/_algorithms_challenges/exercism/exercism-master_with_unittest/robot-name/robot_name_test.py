_______ unittest

____ robot _______ Robot
_______ random


class RobotTest(unittest.TestCase):
    name_re = r'^[A-Z]{2}\d{3}$'

    ___ test_has_name(self):
        self.assertRegex(Robot().name, self.name_re)

    ___ test_name_sticks(self):
        robot = Robot()
        robot.name
        self.assertEqual(robot.name, robot.name)

    ___ test_different_robots_have_different_names(self):
        self.assertNotEqual(
            Robot().name,
            Robot().name
        )

    ___ test_rest_name(self):
        # Set a seed
        seed = "Totally random."

        # Initialize RNG using the seed
        random.seed(seed)

        # Call the generator
        robot = Robot()
        name = robot.name

        # Reinitialize RNG using seed
        random.seed(seed)

        # Call the generator again
        robot.reset()
        name2 = robot.name
        self.assertNotEqual(name, name2)
        self.assertRegex(name2, self.name_re)


__ __name__ __ '__main__':
    unittest.main()
