____ dataclasses _______ dataclass, field


___ get_level():
    r.. "Beginner"

@dataclass(order=True)
class Bite:

    number: int
    title: s..
    level: s.. = field(default_factory=get_level)

    ___ __post_init__(self):
        self.title = self.title.capitalize()