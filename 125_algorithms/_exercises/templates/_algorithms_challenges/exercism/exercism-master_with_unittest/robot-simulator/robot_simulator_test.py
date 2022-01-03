_______ unittest

____ robot_simulator _______ Robot, NORTH, EAST, SOUTH, WEST


c_ RobotTests(unittest.TestCase):

    ___ test_init
        robot = Robot()
        assertEqual((0, 0), robot.coordinates)
        assertEqual(NORTH, robot.bearing)

    ___ test_setup
        robot = Robot(SOUTH, -1, 1)
        assertEqual((-1, 1), robot.coordinates)
        assertEqual(SOUTH, robot.bearing)

    ___ test_turn_right
        robot = Robot()
        ___ direction __ [EAST, SOUTH, WEST, NORTH]:
            robot.turn_right()
            assertEqual(robot.bearing, direction)

    ___ test_turn_left
        robot = Robot()
        ___ direction __ [WEST, SOUTH, EAST, NORTH]:
            robot.turn_left()
            assertEqual(robot.bearing, direction)

    ___ test_advance_positive_north
        robot = Robot(NORTH, 0, 0)
        robot.advance()
        assertEqual((0, 1), robot.coordinates)
        assertEqual(NORTH, robot.bearing)

    ___ test_advance_positive_east
        robot = Robot(EAST, 0, 0)
        robot.advance()
        assertEqual((1, 0), robot.coordinates)
        assertEqual(EAST, robot.bearing)

    ___ test_advance_negative_south
        robot = Robot(SOUTH, 0, 0)
        robot.advance()
        assertEqual((0, -1), robot.coordinates)
        assertEqual(SOUTH, robot.bearing)

    ___ test_advance_positive_west
        robot = Robot(WEST, 0, 0)
        robot.advance()
        assertEqual((-1, 0), robot.coordinates)
        assertEqual(WEST, robot.bearing)

    ___ test_simulate_prog1
        robot = Robot(NORTH, 0, 0)
        robot.simulate("LAAARALA")
        assertEqual((-4, 1), robot.coordinates)
        assertEqual(WEST, robot.bearing)

    ___ test_simulate_prog2
        robot = Robot(EAST, 2, -7)
        robot.simulate("RRAAAAALA")
        assertEqual((-3, -8), robot.coordinates)
        assertEqual(SOUTH, robot.bearing)

    ___ test_simulate_prog3
        robot = Robot(SOUTH, 8, 4)
        robot.simulate("LAAARRRALLLL")
        assertEqual((11, 5), robot.coordinates)
        assertEqual(NORTH, robot.bearing)


__ __name__ __ '__main__':
    unittest.main()
