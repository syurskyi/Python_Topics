from enum ______ Enum

THUMBS_UP = '👍'  # in case you go f-string ...

# move these into an Enum:
class Score(Enum
    BEGINNER = 2
    INTERMEDIATE = 3
    ADVANCED = 4
    CHEATED = 1

    ___ __str__(self
        r_ f'{self.name} => {THUMBS_UP * self.value}'

    @classmethod
    ___ average(cls
        r_ su.(v.value ___ v in list(cls))/le.(cls)
