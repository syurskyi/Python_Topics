____ enum _______ Enum



THUMBS_UP = '👍'  # in case you go f-string ...

# move these into an Enum:

c_ Score(Enum):
    BEGINNER = 2
    INTERMEDIATE = 3
    ADVANCED = 4
    CHEATED = 1

    

    ___ __str__
        r.. f"{name} => {THUMBS_UP * value}"



    @classmethod
    ___ average(cls):
        r.. (cls.BEGINNER.value + cls.INTERMEDIATE.value + cls.ADVANCED.value + cls.CHEATED.value)/4


