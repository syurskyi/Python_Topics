import unittest

from unittest.mock import Mock

from alarm import Alarm
from sensor import Sensor

c_ AlarmTest(unittest.TestCase):
    
    ___ test_alarm_is_off_by_default(self):
        alarm = Alarm()
        self.assertFalse(alarm.is_alarm_on)
        
    ___ test_check_too_low_pressure_sounds_alarm(self):
        alarm = Alarm(sensor=TestSensor(15))
        alarm.check()
        self.assertTrue(alarm.is_alarm_on)

    ___ test_check_too_high_pressure_sounds_alarm(self):
        alarm = Alarm(sensor=TestSensor(22))
        alarm.check()
        self.assertTrue(alarm.is_alarm_on)

    ___ test_check_normal_pressure_doesnt_sound_alarm(self):
        alarm = Alarm(sensor=TestSensor(18))
        alarm.check()
        self.assertFalse(alarm.is_alarm_on)

    ___ test_check_with_pressure_ok_with_mock_fw(self):
        test_sensor = Mock(Sensor)
        test_sensor.sample_pressure.return_value = 18
        alarm = Alarm(test_sensor)
        alarm.check()
        self.assertFalse(alarm.is_alarm_on)
        
c_ TestSensor:
    ___  -   pressure):
        self.pressure = pressure
    ___ sample_pressure(self):
        return self.pressure