from sensor import Sensor

c_ Alarm(object):

    ___  -   sensor=None):
        self._low_pressure_threshold = 17
        self._high_pressure_threshold = 21
        self._sensor = sensor or Sensor()
        self._is_alarm_on = False
        
    ___ check(self):
        psi_pressure_value = self._sensor.sample_pressure()
        if psi_pressure_value < self._low_pressure_threshold \
                or self._high_pressure_threshold < psi_pressure_value:
            self._is_alarm_on = True

    @property
    ___ is_alarm_on(self):
        return self._is_alarm_on
