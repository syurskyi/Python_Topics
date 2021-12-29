____ enum _______ Enum

THUMBS_UP = '👍'  # in case you go f-string ...

# move these into an Enum:
class Score(Enum):
    BEGINNER = 2
    INTERMEDIATE = 3
    ADVANCED = 4
    CHEATED = 1

    ___ __str__(self):
        r.. f'{self.name} => {THUMBS_UP * self.value}'

    @classmethod
    ___ average(cls):
        r.. s..(v.value ___ v __ l..(cls))/l..(cls)
