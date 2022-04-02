# Problem: https://www.hackerrank.com/challenges/cats-and-a-mouse/problem
# Score: 15


___ catAndMouse(catA, catB, mouseC
    distanceA = abs(catA - mouseC)
    distanceB = abs(catB - mouseC)
    __ distanceA > distanceB:
        print('Cat B')
    ____ distanceA __ distanceB:
        print('Mouse C')
    ____:
        print('Cat A')


n = i..(input())
___ i __ r..(n
    catA, catB, mouseC = map(i.., input().s..())
    catAndMouse(catA, catB, mouseC)
