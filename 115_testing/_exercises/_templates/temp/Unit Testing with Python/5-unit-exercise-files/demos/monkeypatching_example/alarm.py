
____ sensor ______ Sensor

c_ Alarm(object

    ___  - 
        _low_pressure_threshold _ 17
        _high_pressure_threshold _ 21
        _sensor _ Sensor()
        _is_alarm_on _ False

    ___ check
        psi_pressure_value _ _sensor.sample_pressure()
        __ psi_pressure_value < _low_pressure_threshold o. _high_pressure_threshold < psi_pressure_value:
            _is_alarm_on _ True

    @property
    ___ is_alarm_on
        r_ _is_alarm_on
