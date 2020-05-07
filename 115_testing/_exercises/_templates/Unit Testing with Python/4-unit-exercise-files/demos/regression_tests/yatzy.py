
def small_straight(dice):
    if sorted(dice) == [1,2,3,4,5]:
        return sum(dice)
    else:
        return 0
