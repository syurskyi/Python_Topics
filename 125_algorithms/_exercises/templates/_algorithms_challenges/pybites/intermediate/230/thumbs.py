THUMBS_UP, THUMBS_DOWN '👍', '👎'


c_ Thumbs:
    
    ___ __mul__  other
        __ other __ 0:
            r.. V...("Specify a number")

        __ (other > 0 a.. other <_ 3) o. (other >_ -3 a.. other < 0
            r.. _* THUMBS_UP __ other > 0 ____ THUMBS_DOWN) * a..(other)}"

        r.. f"{THUMBS_UP __ other > 0 ____ THUMBS_DOWN} ({a..(other)}x)"

    ___ __rmul__  other
        r.. __mul__(other)


__ _______ __ _______
    print(Thumbs() * 2)
    