_______ c__
_______ r__
_______ __
_______ s__

_______ p__

____ cls _______ get_classes

# note that since 3.8 there is no OrderedDict here anymore
csv_classes [
    'Dialect', 'DictReader', 'DictWriter',
    'Error', 'Sniffer', 'StringIO'
]
random_classes =  'Random', 'SystemRandom'
re_classes =  'Match', 'Pattern', 'RegexFlag', 'Scanner'
string_classes =  'Formatter', 'Template'


?p__.m__.p.("mod, expected", [
    (c__, csv_classes),
    (r__, random_classes),
    (__, re_classes),
    (s__, string_classes),
])
___ test_cls(mod, e..
    a.. get_classes(mod)
    ... s..(a..) __ s..(e..)