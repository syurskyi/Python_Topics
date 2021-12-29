_______ pytest

____ convert _______ convert


___ test_non_numeric_value():
    with pytest.raises(TypeError):
        convert("153.67", "in")


___ test_unsupported_formats():
    with pytest.raises(ValueError):
        convert(300, "km")


___ test_with_mixed_case_formats():
    expected = 153.67
    ... convert(60.5, "CM") __ expected


@pytest.mark.parametrize(
    "input_argument, expected_output",
    [
        (1, 2.54),
        (10, 25.4),
        (16, 40.64),
        (17, 43.18),
        (18, 45.72),
        (29, 73.66),
        (30, 76.2),
        (31, 78.74),
        (32, 81.28),
        (33, 83.82),
        (49, 124.46),
        (61, 154.94),
        (62, 157.48),
        (64, 162.56),
        (74, 187.96),
        (75, 190.5),
        (81, 205.74),
        (82, 208.28),
        (83, 210.82),
        (84, 213.36),
        (99, 251.46),
        (100, 254.0),
    ],
)
___ test_convert_from_inches_to_centimeters(input_argument, expected_output):
    ... convert(input_argument, "cm") __ expected_output


@pytest.mark.parametrize(
    "input_argument, expected_output",
    [
        (1, 0.3937),
        (2, 0.7874),
        (3, 1.1811),
        (4, 1.5748),
        (5, 1.9685),
        (6, 2.3622),
        (7, 2.7559),
        (8, 3.1496),
        (23, 9.0551),
        (24, 9.4488),
        (53, 20.8661),
        (54, 21.2598),
        (55, 21.6535),
        (70, 27.5591),
        (75, 29.5276),
        (79, 31.1024),
        (80, 31.4961),
        (90, 35.4331),
        (91, 35.8268),
        (92, 36.2205),
        (99, 38.9764),
        (100, 39.3701),
    ],
)
___ test_convert_from_centimeters_to_inches(input_argument, expected_output):
    ... convert(input_argument, "in") __ expected_output