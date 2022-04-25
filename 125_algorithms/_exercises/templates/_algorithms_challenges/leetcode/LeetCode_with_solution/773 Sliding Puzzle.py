#!/usr/bin/python3
"""
On a 2x3 board, there are 5 tiles represented by the integers 1 through 5, and
an empty square represented by 0.

A move consists of choosing 0 and a 4-directionally adjacent number and swapping
it.

The state of the board is solved if and only if the board is [[1,2,3],[4,5,0]].

Given a puzzle board, return the least number of moves required so that the
state of the board is solved. If it is impossible for the state of the board to
be solved, return -1.

Examples:

Input: board = [[1,2,3],[4,0,5]]
Output: 1
Explanation: Swap the 0 and the 5 in one move.
Input: board = [[1,2,3],[5,4,0]]
Output: -1
Explanation: No number of moves will make the board solved.
Input: board = [[4,1,2],[5,0,3]]
Output: 5
Explanation: 5 is the smallest number of moves that solves the board.
An example path:
After move 0: [[4,1,2],[5,0,3]]
After move 1: [[4,1,2],[0,5,3]]
After move 2: [[0,1,2],[4,5,3]]
After move 3: [[1,0,2],[4,5,3]]
After move 4: [[1,2,0],[4,5,3]]
After move 5: [[1,2,3],[4,5,0]]
Input: board = [[3,2,4],[1,5,0]]
Output: 14
Note:

board will be a 2 x 3 array as described above.
board[i][j] will be a permutation of [0, 1, 2, 3, 4, 5].
"""
____ t___ _______ L..
____ c.. _______ d..
____ c.. _______ d..
_______ h__


final_pos {
    1: (0, 0),
    2: (0, 1),
    3: (0, 2),
    4: (1, 0),
    5: (1, 1),
    0: (1, 2),
}

dirs (
    (0, -1),
    (0, 1),
    (-1, 0),
    (1, 0),
)


c_ Solution:
    ___ slidingPuzzle  board: L..[L..[i..]]) __ i..
        """
        BFS + visited

        => A*
        priority = current_dist + heuristic_dist

        Chain the matrix into 1d array. N = R * C
        Complexity O(N * N!)
        There are O(N!) possible board states. O(N) is the time to scan the board for the operations in the loop.

        Possible to reduce the 2D array in a 1D array and do %C and //C, where C is the size of the column
        """
        visited d..(b..)
        m, n l..(board), l..(board 0
        q [(heuristic_dist(board) + 0, 0, board)]
        target [
            [1, 2, 3],
            [4, 5, 0],
        ]
        w.... q:
            heu, cur_dist, board h__.heappop(q)
            visited[ser(board)] T..
            __ board __ target:
                r.. cur_dist

            cur_dist += 1
            i, j zero_pos(board)
            ___ di, dj __ dirs:
                I i + di
                J j + dj
                __ 0 <_ I < m a.. 0 <_ J < n:
                    B d..(board)   # need a copy in the queue
                    B[I][J], B[i][j] B[i][j], B[I][J]
                    __ n.. visited[ser(B)]:
                        h__.heappush(q, (heuristic_dist(B) + cur_dist, cur_dist, B
        r.. -1

    ___ zero_pos  board
        ___ i, row __ e..(board
            ___ j, v __ e..(row
                __ v __ 0:
                    r.. i, j
        r..

    ___ heuristic_dist  board
        """
        manhattan distance
        """
        ret 0
        ___ i, row __ e..(board
            ___ j, v __ e..(row
                __ v !_ 0:
                    I, J final_pos[v]
                    ret += a..(i - I) + a..(j - J)
        r.. ret

    ___ ser  board
        r.. t..(
            t..(row)
            ___ row __ board
        )


__ _______ __ _______
    ... Solution().slidingPuzzle([[1,2,3],[4,0,5]]) __ 1
    ... Solution().slidingPuzzle([[1,2,3],[5,4,0]]) __ -1
