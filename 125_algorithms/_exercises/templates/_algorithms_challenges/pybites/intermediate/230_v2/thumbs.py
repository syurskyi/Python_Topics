THUMBS_UP, THUMBS_DOWN  '👍', '👎'


c_ Thumbs:

    

    ___ __rmul__ number

        r.. self * number

    ___ __mul__ number
        __ isi..(number,i..
            __ number > 0:
                s__  THUMBS_UP
            ____ number < 0:
                number  abs(number)
                s__  THUMBS_DOWN
            ____:
                r.. V...("Specify a number")
            
            
            __ number < 3:
                r.. s__ * number
            ____:
                r.. f"{s__} ({number}x)"
            
        ____:
            r.. T..("Can only multiple by intger")

