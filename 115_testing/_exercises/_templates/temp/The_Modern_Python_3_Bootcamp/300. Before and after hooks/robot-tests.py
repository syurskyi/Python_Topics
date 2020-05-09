______ u__
____ robot ______ Robot


c_ RobotTests?.?
    ___ setUp
        mega_man _ Robot("Mega Man", battery_50)

    ___ test_charge
        mega_man.charge()
        aE..(mega_man.battery, 100)

    ___ test_say_name
        aE..(
            mega_man.say_name(),
            "BEEP BOOP BEEP BOOP.  I AM MEGA MAN")
        aE..(mega_man.battery, 49)


if __name__ == "__main__":
    u__.main()
