from dataclasses import dataclass, field


def get_level():
    return "Beginner"

@dataclass(order=True)
class Bite:

    number: int
    title: str
    level: str = field(default_factory=get_level)

    def __post_init__(self):
        self.title = self.title.capitalize()