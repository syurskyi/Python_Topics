____ e.. _______ E..

THUMBS_UP = '👍'  # in case you go f-string ...

# move these into an Enum:
# BEGINNER = 2
# INTERMEDIATE = 3
# ADVANCED = 4
# CHEATED = 1


c_ Score(E..
    
    BEGINNER = 2
    INTERMEDIATE = 3
    ADVANCED = 4
    CHEATED = 1

    ___  -r
        r.. f"{__class__.__name__}.{name}"

    ___ __str__
        r.. f"{name} => {THUMBS_UP * value}"

    @classmethod
    ___ average(cls
        total_score = [score.value ___ score __ cls]
        r.. s..(total_score) / l..(total_score)

# if __name__ == "__main__":
#     print(list(Score))
    # test = Score(2)
    # print(test.__str__())
    # print(test.average())
