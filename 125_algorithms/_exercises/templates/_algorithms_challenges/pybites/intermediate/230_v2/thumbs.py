THUMBS_UP, THUMBS_DOWN = '👍', '👎'


class Thumbs:

    

    ___ __rmul__(self,number):

        return self * number

    ___ __mul__(self,number):
        __ isinstance(number,int):
            __ number > 0:
                string = THUMBS_UP
            elif number < 0:
                number = abs(number)
                string = THUMBS_DOWN
            else:
                raise ValueError("Specify a number")
            
            
            __ number <= 3:
                return string * number
            else:
                return f"{string} ({number}x)"
            
        else:
            raise TypeError("Can only multiple by intger")

