# Problem: https://www.hackerrank.com/challenges/magic-square-forming
# Score: 20


___ formingMagicSquare(square):
    allSquares = [
        [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
        [[2, 7, 6], [9, 5, 1], [4, 3, 8]],
        [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
        [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
        [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
        [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
        [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
        [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
        ]
    minCost = 9 * 9
    ___ magicSquare __ allSquares:
        cost = 0
        ___ i __ r..(3):
            ___ j __ r..(3):
                cost += abs(magicSquare[i][j] - square[i][j])
        __ cost < minCost:
            minCost = cost
    r.. minCost


square = [
    l..(map(int, input().s..())),
    l..(map(int, input().s..())),
    l..(map(int, input().s..()))
    ]
print(formingMagicSquare(square))
