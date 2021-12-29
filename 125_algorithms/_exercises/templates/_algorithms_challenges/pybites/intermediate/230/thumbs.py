THUMBS_UP, THUMBS_DOWN = '👍', '👎'


class Thumbs:
    
    ___ __mul__(self, other):
        __ other __ 0:
            raise ValueError("Specify a number")

        __ (other > 0 and other <= 3) o. (other >= -3 and other < 0):
            r.. f"{(THUMBS_UP __ other > 0 ____ THUMBS_DOWN) * abs(other)}"

        r.. f"{THUMBS_UP __ other > 0 ____ THUMBS_DOWN} ({abs(other)}x)"

    ___ __rmul__(self, other):
        r.. self.__mul__(other)


__ __name__ __ "__main__":
    print(Thumbs() * 2)
    