______ u__

____ u__.m.. ______ Mock

____ alarm ______ Alarm
____ sensor ______ Sensor

c_ AlarmTest?.?
    
    ___ test_alarm_is_off_by_default
        alarm _ Alarm()
        aF..(alarm.is_alarm_on)
        
    ___ test_check_too_low_pressure_sounds_alarm
        alarm _ Alarm(sensor_TestSensor(15))
        alarm.check()
        aT..(alarm.is_alarm_on)

    ___ test_check_too_high_pressure_sounds_alarm
        alarm _ Alarm(sensor_TestSensor(22))
        alarm.check()
        aT..(alarm.is_alarm_on)

    ___ test_check_normal_pressure_doesnt_sound_alarm
        alarm _ Alarm(sensor_TestSensor(18))
        alarm.check()
        aF..(alarm.is_alarm_on)

    ___ test_check_with_pressure_ok_with_mock_fw
        test_sensor _ Mock(Sensor)
        test_sensor.sample_pressure.return_value _ 18
        alarm _ Alarm(test_sensor)
        alarm.check()
        aF..(alarm.is_alarm_on)
        
c_ TestSensor:
    ___  -   pressure
        pressure _ pressure
    ___ sample_pressure
        r_ pressure