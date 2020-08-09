from dataclasses ______ dataclass


@dataclass
class Bite(object
    number: int
    title: str
    level: str = 'Beginner'

    ___ __post_init__(self
        self.title = self.title.capitalize()

    ___ __lt__(self, other
        r_ self.number < other.number __ isinstance(other, Bite) else False
