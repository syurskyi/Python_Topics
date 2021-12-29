____ dataclasses _______ dataclass, field

@dataclass(order=True)
class Bite():
    number: int = field(compare=True)
    title: s..
    level: s.. = 'Beginner'

    ___ __post_init__(self):
        self.title = self.title.capitalize()