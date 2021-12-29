____ enum _______ Enum

THUMBS_UP = '👍'  # in case you go f-string ...

# move these into an Enum:
# BEGINNER = 2
# INTERMEDIATE = 3
# ADVANCED = 4
# CHEATED = 1


class Score(Enum):
    
    BEGINNER = 2
    INTERMEDIATE = 3
    ADVANCED = 4
    CHEATED = 1

    ___ __repr__(self):
        r.. f"{self.__class__.__name__}.{self.name}"

    ___ __str__(self):
        r.. f"{self.name} => {THUMBS_UP * self.value}"

    @classmethod
    ___ average(cls):
        total_score = [score.value ___ score __ cls]
        r.. s..(total_score) / l..(total_score)

# if __name__ == "__main__":
#     print(list(Score))
    # test = Score(2)
    # print(test.__str__())
    # print(test.average())
