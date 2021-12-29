____ dataclasses _______ dataclass



@dataclass(order=True)
class Bite:
    number: int
    title: s..
    level: s.. = "Beginner"





    ___ __post_init__(self):
        self.title = self.title.capitalize()






