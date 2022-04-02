# Problem: https://www.hackerrank.com/challenges/text-alignment/problem
# Score: 10


# Replace all ______ with rjust, ljust or center.

thickness = i..(input()) # This must be an odd number
c = 'H'

# Top Cone
___ i __ r..(thickness
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

# Top Pillars
___ i __ r..(thickness+1
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

# Middle Belt
___ i __ r..((thickness+1)//2
    print((c*thickness*5).center(thickness*6))

# Bottom Pillars
___ i __ r..(thickness+1
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

# Bottom Cone
___ i __ r..(thickness
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))
