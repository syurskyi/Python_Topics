THUMBS_UP, THUMBS_DOWN = '👍', '👎'


class Thumbs:

    

    def __rmul__(self,number):

        return self * number

    def __mul__(self,number):
        if isinstance(number,int):
            if number > 0:
                string = THUMBS_UP
            elif number < 0:
                number = abs(number)
                string = THUMBS_DOWN
            else:
                raise ValueError("Specify a number")
            
            
            if number <= 3:
                return string * number
            else:
                return f"{string} ({number}x)"
            
        else:
            raise TypeError("Can only multiple by intger")

