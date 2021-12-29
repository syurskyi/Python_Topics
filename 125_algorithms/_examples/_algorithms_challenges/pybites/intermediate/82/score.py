from enum import Enum

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

    def __repr__(self):
        return f"{self.__class__.__name__}.{self.name}"

    def __str__(self):
        return f"{self.name} => {THUMBS_UP * self.value}"

    @classmethod
    def average(cls):
        total_score = [score.value for score in cls] 
        return sum(total_score) / len(total_score)

# if __name__ == "__main__":
#     print(list(Score))
    # test = Score(2)
    # print(test.__str__())
    # print(test.average())
