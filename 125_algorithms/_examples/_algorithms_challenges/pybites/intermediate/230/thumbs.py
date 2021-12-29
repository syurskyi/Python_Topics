THUMBS_UP, THUMBS_DOWN = '👍', '👎'


class Thumbs:
    
    def __mul__(self, other):
        if other == 0:
            raise ValueError("Specify a number")

        if (other > 0 and other <= 3) or (other >= -3 and other < 0):
            return f"{(THUMBS_UP if other > 0 else THUMBS_DOWN) * abs(other)}"

        return f"{THUMBS_UP if other > 0 else THUMBS_DOWN} ({abs(other)}x)"

    def __rmul__(self, other):
        return self.__mul__(other)


if __name__ == "__main__":
    print(Thumbs() * 2)
    