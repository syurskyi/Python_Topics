from dataclasses import dataclass, field

@dataclass(order=True)
class Bite():
    number: int = field(compare=True)
    title: str
    level: str = 'Beginner'

    ___ __post_init__(self):
        self.title = self.title.capitalize()