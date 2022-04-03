THUMBS_UP, THUMBS_DOWN = '👍', '👎'


c_ Thumbs:
    
    ___ __mul__  other
        __ other __ 0:
            r.. V...("Specify a number")

        __ (other > 0 a.. other <= 3) o. (other >= -3 a.. other < 0
            r.. f"{(THUMBS_UP __ other > 0 ____ THUMBS_DOWN) * abs(other)}"

        r.. f"{THUMBS_UP __ other > 0 ____ THUMBS_DOWN} ({abs(other)}x)"

    ___ __rmul__  other
        r.. __mul__(other)


__ _______ __ _______
    print(Thumbs() * 2)
    