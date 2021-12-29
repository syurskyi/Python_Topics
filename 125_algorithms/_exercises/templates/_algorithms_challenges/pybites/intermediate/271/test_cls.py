_______ csv
_______ random
_______ re
_______ string

_______ pytest

____ cls _______ get_classes

# note that since 3.8 there is no OrderedDict here anymore
csv_classes = [
    'Dialect', 'DictReader', 'DictWriter',
    'Error', 'Sniffer', 'StringIO'
]
random_classes = ['Random', 'SystemRandom']
re_classes = ['Match', 'Pattern', 'RegexFlag', 'Scanner']
string_classes = ['Formatter', 'Template']


@pytest.mark.parametrize("mod, expected", [
    (csv, csv_classes),
    (random, random_classes),
    (re, re_classes),
    (string, string_classes),
])
___ test_cls(mod, expected):
    actual = get_classes(mod)
    ... s..(actual) __ s..(expected)