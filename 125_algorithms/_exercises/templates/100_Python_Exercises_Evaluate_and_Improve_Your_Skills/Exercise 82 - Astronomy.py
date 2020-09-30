#Use Python to calculate the distance (in AU units) between Jupiter and Sun on January 1, 1230.
#A: I didn't know this so I did some internet research and reveal that ephem is used for astronomical clculations.
#The ephem library was installed with pip, and for Windows a precompiled library from http://www.lfd.uci.edu/~gohlke/pythonlibs/#pyephem was installed with pip
#Try to find your own version from that page

______ ephem
jupiter _ ephem.Jupiter()
jupiter.compute('1230/1/1')
distance_au_units _ jupiter.sun_distance
distance_km _ distance_au_units * 149597870.691
print(distance_km)
