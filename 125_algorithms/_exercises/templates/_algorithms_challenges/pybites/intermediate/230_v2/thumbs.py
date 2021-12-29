THUMBS_UP, THUMBS_DOWN = '👍', '👎'


class Thumbs:

    

    ___ __rmul__(self,number):

        r.. self * number

    ___ __mul__(self,number):
        __ isi..(number,int):
            __ number > 0:
                string = THUMBS_UP
            ____ number < 0:
                number = abs(number)
                string = THUMBS_DOWN
            ____:
                raise ValueError("Specify a number")
            
            
            __ number <= 3:
                r.. string * number
            ____:
                r.. f"{string} ({number}x)"
            
        ____:
            raise TypeError("Can only multiple by intger")

