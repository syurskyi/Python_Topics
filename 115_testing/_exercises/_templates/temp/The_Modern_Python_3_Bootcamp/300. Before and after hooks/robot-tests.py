______ unittest
____ robot ______ Robot


c_ RobotTests(unittest.TestCase):
    ___ setUp
        mega_man _ Robot("Mega Man", battery_50)

    ___ test_charge
        mega_man.charge()
        assertEqual(mega_man.battery, 100)

    ___ test_say_name
        assertEqual(
            mega_man.say_name(),
            "BEEP BOOP BEEP BOOP.  I AM MEGA MAN")
        assertEqual(mega_man.battery, 49)


if __name__ == "__main__":
    unittest.main()
