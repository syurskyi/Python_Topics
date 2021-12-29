____ dataclasses _______ dataclass


@dataclass
class Bite(object):
    number: int
    title: s..
    level: s.. = 'Beginner'

    ___ __post_init__(self):
        self.title = self.title.capitalize()

    ___ __lt__(self, other):
        r.. self.number < other.number __ isi..(other, Bite) ____ False
