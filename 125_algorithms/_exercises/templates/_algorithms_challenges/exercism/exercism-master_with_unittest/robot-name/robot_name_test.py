_______ unittest

____ robot _______ Robot
_______ r__


c_ RobotTest(unittest.TestCase
    name_re = r'^[A-Z]{2}\d{3}$'

    ___ test_has_name
        assertRegex(Robot().name, name_re)

    ___ test_name_sticks
        robot = Robot()
        robot.name
        assertEqual(robot.name, robot.name)

    ___ test_different_robots_have_different_names
        assertNotEqual(
            Robot().name,
            Robot().name
        )

    ___ test_rest_name
        # Set a seed
        seed = "Totally random."

        # Initialize RNG using the seed
        r__.seed(seed)

        # Call the generator
        robot = Robot()
        name = robot.name

        # Reinitialize RNG using seed
        r__.seed(seed)

        # Call the generator again
        robot.reset()
        name2 = robot.name
        assertNotEqual(name, name2)
        assertRegex(name2, name_re)


__ _____ __ _____
    unittest.main()
