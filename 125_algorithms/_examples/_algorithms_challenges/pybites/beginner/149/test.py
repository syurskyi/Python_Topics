words = ("It's almost Holidays and PyBites wishes You a "
             "Merry Christmas and a Happy 2019").split()

def f(e):
    d={int:1, float:1, str:0}
    return d.get(type(e), 0), e


print( sorted( words, key=f ))