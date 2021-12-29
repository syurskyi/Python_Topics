_______ unittest
____ robot_simulator _______ Robot, NORTH, EAST, SOUTH, WEST


class RobotTests(unittest.TestCase):

    ___ test_init(self):
        robot = Robot()
        self.assertEqual(robot.coordinates, (0, 0))
        self.assertEqual(robot.bearing, NORTH)

    ___ test_setup(self):
        robot = Robot(SOUTH, -1, 1)
        self.assertEqual(robot.coordinates, (-1, 1))
        self.assertEqual(robot.bearing, SOUTH)

    ___ test_turn_right(self):
        robot = Robot()
        ___ direction __ [EAST, SOUTH, WEST, NORTH]:
            robot.turn_right()
            self.assertEqual(robot.bearing, direction)

    ___ test_turn_left(self):
        robot = Robot()
        ___ direction __ [WEST, SOUTH, EAST, NORTH]:
            robot.turn_left()
            self.assertEqual(robot.bearing, direction)

    ___ test_advance_positive_north(self):
        robot = Robot(NORTH, 0, 0)
        robot.advance()
        self.assertEqual(robot.coordinates, (0, 1))
        self.assertEqual(robot.bearing, NORTH)

    ___ test_advance_positive_east(self):
        robot = Robot(EAST, 0, 0)
        robot.advance()
        self.assertEqual(robot.coordinates, (1, 0))
        self.assertEqual(robot.bearing, EAST)

    ___ test_advance_negative_south(self):
        robot = Robot(SOUTH, 0, 0)
        robot.advance()
        self.assertEqual(robot.coordinates, (0, -1))
        self.assertEqual(robot.bearing, SOUTH)

    ___ test_advance_positive_west(self):
        robot = Robot(WEST, 0, 0)
        robot.advance()
        self.assertEqual(robot.coordinates, (-1, 0))
        self.assertEqual(robot.bearing, WEST)

    ___ test_simulate_prog1(self):
        robot = Robot(NORTH, 0, 0)
        robot.simulate("LAAARALA")
        self.assertEqual(robot.coordinates, (-4, 1))
        self.assertEqual(robot.bearing, WEST)

    ___ test_simulate_prog2(self):
        robot = Robot(EAST, 2, -7)
        robot.simulate("RRAAAAALA")
        self.assertEqual(robot.coordinates, (-3, -8))
        self.assertEqual(robot.bearing, SOUTH)

    ___ test_simulate_prog3(self):
        robot = Robot(SOUTH, 8, 4)
        robot.simulate("LAAARRRALLLL")
        self.assertEqual(robot.coordinates, (11, 5))
        self.assertEqual(robot.bearing, NORTH)


__ __name__ __ '__main__':
    # Sort test methods by order of definition
    # https://stackoverflow.com/a/18499093
    loader = unittest.TestLoader()
    get_line_number = l.... f: getattr(RobotTests, f).__code__.co_firstlineno
    line_compare = l.... a, b: get_line_number(a) - get_line_number(b)
    loader.sortTestMethodsUsing = line_compare

    unittest.main(testLoader=loader, failfast=True, verbosity=2)
