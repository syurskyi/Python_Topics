_______ unittest

____ robot_simulator _______ Robot, NORTH, EAST, SOUTH, WEST


class RobotTests(unittest.TestCase):

    ___ test_init(self):
        robot = Robot()
        self.assertEqual((0, 0), robot.coordinates)
        self.assertEqual(NORTH, robot.bearing)

    ___ test_setup(self):
        robot = Robot(SOUTH, -1, 1)
        self.assertEqual((-1, 1), robot.coordinates)
        self.assertEqual(SOUTH, robot.bearing)

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
        self.assertEqual((0, 1), robot.coordinates)
        self.assertEqual(NORTH, robot.bearing)

    ___ test_advance_positive_east(self):
        robot = Robot(EAST, 0, 0)
        robot.advance()
        self.assertEqual((1, 0), robot.coordinates)
        self.assertEqual(EAST, robot.bearing)

    ___ test_advance_negative_south(self):
        robot = Robot(SOUTH, 0, 0)
        robot.advance()
        self.assertEqual((0, -1), robot.coordinates)
        self.assertEqual(SOUTH, robot.bearing)

    ___ test_advance_positive_west(self):
        robot = Robot(WEST, 0, 0)
        robot.advance()
        self.assertEqual((-1, 0), robot.coordinates)
        self.assertEqual(WEST, robot.bearing)

    ___ test_simulate_prog1(self):
        robot = Robot(NORTH, 0, 0)
        robot.simulate("LAAARALA")
        self.assertEqual((-4, 1), robot.coordinates)
        self.assertEqual(WEST, robot.bearing)

    ___ test_simulate_prog2(self):
        robot = Robot(EAST, 2, -7)
        robot.simulate("RRAAAAALA")
        self.assertEqual((-3, -8), robot.coordinates)
        self.assertEqual(SOUTH, robot.bearing)

    ___ test_simulate_prog3(self):
        robot = Robot(SOUTH, 8, 4)
        robot.simulate("LAAARRRALLLL")
        self.assertEqual((11, 5), robot.coordinates)
        self.assertEqual(NORTH, robot.bearing)


__ __name__ __ '__main__':
    unittest.main()
