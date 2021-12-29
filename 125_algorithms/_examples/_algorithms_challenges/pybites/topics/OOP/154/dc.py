from dataclasses import dataclass

# 'number': int, 'title': str, 'level': str

@dataclass(order=True)
class Bite:

    number: int
    title: str
    level: str

    def __init__(self, number, title, level='Beginner'):
        self.number = number
        self.title = title.capitalize()
        self.level = level