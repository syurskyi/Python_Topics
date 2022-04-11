_______ unittest
____ robot_simulator _______ Robot, NORTH, EAST, SOUTH, WEST


c_ RobotTests(unittest.TestCase

    ___ test_init
        robot Robot()
        assertEqual(robot.coordinates, (0, 0
        assertEqual(robot.bearing, NORTH)

    ___ test_setup
        robot Robot(SOUTH, -1, 1)
        assertEqual(robot.coordinates, (-1, 1
        assertEqual(robot.bearing, SOUTH)

    ___ test_turn_right
        robot Robot()
        ___ direction __ [EAST, SOUTH, WEST, NORTH]:
            robot.turn_right()
            assertEqual(robot.bearing, direction)

    ___ test_turn_left
        robot Robot()
        ___ direction __ [WEST, SOUTH, EAST, NORTH]:
            robot.turn_left()
            assertEqual(robot.bearing, direction)

    ___ test_advance_positive_north
        robot Robot(NORTH, 0, 0)
        robot.advance()
        assertEqual(robot.coordinates, (0, 1
        assertEqual(robot.bearing, NORTH)

    ___ test_advance_positive_east
        robot Robot(EAST, 0, 0)
        robot.advance()
        assertEqual(robot.coordinates, (1, 0
        assertEqual(robot.bearing, EAST)

    ___ test_advance_negative_south
        robot Robot(SOUTH, 0, 0)
        robot.advance()
        assertEqual(robot.coordinates, (0, -1
        assertEqual(robot.bearing, SOUTH)

    ___ test_advance_positive_west
        robot Robot(WEST, 0, 0)
        robot.advance()
        assertEqual(robot.coordinates, (-1, 0
        assertEqual(robot.bearing, WEST)

    ___ test_simulate_prog1
        robot Robot(NORTH, 0, 0)
        robot.simulate("LAAARALA")
        assertEqual(robot.coordinates, (-4, 1
        assertEqual(robot.bearing, WEST)

    ___ test_simulate_prog2
        robot Robot(EAST, 2, -7)
        robot.simulate("RRAAAAALA")
        assertEqual(robot.coordinates, (-3, -8
        assertEqual(robot.bearing, SOUTH)

    ___ test_simulate_prog3
        robot Robot(SOUTH, 8, 4)
        robot.simulate("LAAARRRALLLL")
        assertEqual(robot.coordinates, (11, 5
        assertEqual(robot.bearing, NORTH)


__ _____ __ _____
    # Sort test methods by order of definition
    # https://stackoverflow.com/a/18499093
    loader unittest.TestLoader()
    get_line_number l.... f: getattr(RobotTests, f).__code__.co_firstlineno
    line_compare l.... a, b: get_line_number(a) - get_line_number(b)
    loader.sortTestMethodsUsing line_compare

    unittest.main(testLoader=loader, failfast=T.., verbosity=2)
