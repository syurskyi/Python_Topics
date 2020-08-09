___ pythagorean(triangles
    answer = []
    ___ triangle in range(triangles
        sides = input().split()
        a,b,c = sides
        a,b,c = int(a),int(b),int(c)

        __ a**2 + b**2 __ c**2:
            answer.append('R')
        ____ a**2 + b**2 > c**2:
            answer.append('A')
        ____ a**2 + b**2 < c**2:
            answer.append('O')
    print(' '.join(answer))
pythagorean(int(input()))
