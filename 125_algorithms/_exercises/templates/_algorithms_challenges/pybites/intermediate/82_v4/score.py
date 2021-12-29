from enum import Enum

THUMBS_UP = '👍'  # in case you go f-string ...


class Score(Enum):
    BEGINNER = 2
    INTERMEDIATE = 3
    ADVANCED = 4
    CHEATED = 1

    ___ __str__(self):
        return f'{self.name} => {THUMBS_UP * self.value}'

    ___ average():
        vals = [s.value for s in Score.__members__.values()]
        return sum(vals) / len(vals)
