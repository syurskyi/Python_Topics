____ enum _______ Enum

THUMBS_UP = '👍'  # in case you go f-string ...


class Score(Enum):
    BEGINNER = 2
    INTERMEDIATE = 3
    ADVANCED = 4
    CHEATED = 1

    ___ __str__(self):
        r.. f'{self.name} => {THUMBS_UP * self.value}'

    ___ average():
        vals = [s.value ___ s __ Score.__members__.values()]
        r.. s..(vals) / l..(vals)
