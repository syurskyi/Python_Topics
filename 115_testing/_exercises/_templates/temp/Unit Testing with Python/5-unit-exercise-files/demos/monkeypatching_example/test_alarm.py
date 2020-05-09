______ unittest
____ unittest.mock ______ *

____ alarm ______ Alarm

c_ AlarmTest(unittest.TestCase):
    
    ___ test_check_with_too_high_pressure
        with patch('alarm.Sensor') as test_sensor_class:
            test_sensor_instance _ Mock()
            test_sensor_instance.sample_pressure.return_value _ 22
            test_sensor_class.return_value_test_sensor_instance
            alarm _ Alarm()
            alarm.check()
            assertTrue(alarm.is_alarm_on)

    @patch("alarm.Sensor")
    ___ test_check_with_too_low_pressure  test_sensor_class):
        test_sensor_instance _ Mock()
        test_sensor_instance.sample_pressure.return_value _ 15
        test_sensor_class.return_value _ test_sensor_instance
        alarm _ Alarm()
        alarm.check()
        assertTrue(alarm.is_alarm_on)
