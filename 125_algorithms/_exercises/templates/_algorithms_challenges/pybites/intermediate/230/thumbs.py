THUMBS_UP, THUMBS_DOWN = '👍', '👎'


c_ Thumbs:
    
    ___ __mul__(self, other):
        __ other __ 0:
            r.. ValueError("Specify a number")

        __ (other > 0 a.. other <= 3) o. (other >= -3 a.. other < 0):
            r.. f"{(THUMBS_UP __ other > 0 ____ THUMBS_DOWN) * abs(other)}"

        r.. f"{THUMBS_UP __ other > 0 ____ THUMBS_DOWN} ({abs(other)}x)"

    ___ __rmul__(self, other):
        r.. __mul__(other)


__ __name__ __ "__main__":
    print(Thumbs() * 2)
    