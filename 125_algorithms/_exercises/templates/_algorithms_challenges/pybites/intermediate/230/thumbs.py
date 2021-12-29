THUMBS_UP, THUMBS_DOWN = '👍', '👎'


class Thumbs:
    
    ___ __mul__(self, other):
        __ other == 0:
            raise ValueError("Specify a number")

        __ (other > 0 and other <= 3) or (other >= -3 and other < 0):
            return f"{(THUMBS_UP __ other > 0 else THUMBS_DOWN) * abs(other)}"

        return f"{THUMBS_UP __ other > 0 else THUMBS_DOWN} ({abs(other)}x)"

    ___ __rmul__(self, other):
        return self.__mul__(other)


__ __name__ == "__main__":
    print(Thumbs() * 2)
    