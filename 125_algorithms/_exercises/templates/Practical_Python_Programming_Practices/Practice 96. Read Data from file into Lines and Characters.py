from math ______ pi

r _ float(input("Insert radius of the orbit(million km): "))
v _ float(input("Insert orbital speed(km/s): "))

r _ r*1000000

yr _ 2*pi*r/v

yr _ yr/(60*60*24)

print(round(yr))