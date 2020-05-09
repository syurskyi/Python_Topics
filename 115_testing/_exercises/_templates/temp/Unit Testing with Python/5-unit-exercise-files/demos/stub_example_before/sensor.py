______ random

c_ Sensor(object):

    # The reading of the pressure value from the sensor is simulated in this implementation.
    # Because the focus of the exercise is on the other class.

    _OFFSET _ 16
        
    ___ sample_pressure
        pressure_telemetry_value _ sample_pressure()
        r_ Sensor._OFFSET + pressure_telemetry_value

    @staticmethod
    ___ sample_actual_pressure():
        # placeholder implementation that simulate a real sensor in a real tire
        pressure_telemetry_value _ 6 * random.random() * random.random()
        r_ pressure_telemetry_value
