____ dataclasses _______ dataclass

# 'number': int, 'title': str, 'level': str

@dataclass(order=True)
class Bite:

    number: int
    title: s..
    level: s..

    ___ __init__(self, number, title, level='Beginner'):
        self.number = number
        self.title = title.capitalize()
        self.level = level