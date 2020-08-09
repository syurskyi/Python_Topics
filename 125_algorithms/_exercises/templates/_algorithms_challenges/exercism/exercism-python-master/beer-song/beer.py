"""Sings the beer song"""

___ song(start=100, stop=0
    """Sings the beer song"""
    r_ "".join(verse(n) + "\n" for n in range(start, stop-1, -1))

___ verse(n
    """Sings a verse of the beer song"""
    __ n __ 0:
        r_ ("No more bottles of beer on the wall, no more bottles of beer.\n"
                "Go to the store and buy some more, 99 bottles of beer on the wall.\n")
    __ n __ 1:
        r_ ("1 bottle of beer on the wall, 1 bottle of beer.\n"
                "Take it down and pass it around, no more bottles of beer on the wall.\n")
    __ n __ 2:
        r_ ("2 bottles of beer on the wall, 2 bottles of beer.\n"
                "Take one down and pass it around, 1 bottle of beer on the wall.\n")
    ____
        r_ ("{0} bottles of beer on the wall, {0} bottles of beer.\n"
                "Take one down and pass it around, {1} bottles of beer on the wall.\n".format(n, n-1))
