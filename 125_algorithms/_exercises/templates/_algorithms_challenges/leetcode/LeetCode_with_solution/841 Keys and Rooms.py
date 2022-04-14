#!/usr/bin/python3
"""
There are N rooms and you start in room 0.  Each room has a distinct number in
0, 1, 2, ..., N-1, and each room may have some keys to access the next room.

Formally, each room i has a list of keys rooms[i], and each key rooms[i][j] is
an integer in [0, 1, ..., N-1] where N = rooms.length.  A key rooms[i][j] = v
opens the room with number v.

Initially, all the rooms start locked (except for room 0).

You can walk back and forth between rooms freely.

Return true if and only if you can enter every room.

Example 1:

Input: [[1],[2],[3],[]]
Output: true
Explanation:
We start in room 0, and pick up key 1.
We then go to room 1, and pick up key 2.
We then go to room 2, and pick up key 3.
We then go to room 3.  Since we were able to go to every room, we return true.
Example 2:

Input: [[1,3],[3,0,1],[2],[0]]
Output: false
Explanation: We can't enter the room with number 2.
Note:

1 <= rooms.length <= 1000
0 <= rooms[i].length <= 1000
The number of keys in all rooms combined is at most 3000.
"""
____ t___ _______ L..


c_ Solution:
    ___ canVisitAllRooms  G: L..[L..[i..]]) __ b..
        """
        starting from 0

        need a queue to keep track of processing nodes? Implicitly handle by dfs
        stacks
        """
        n l..(G)
        visited [0 ___ _ __ r..(n)]  # 0 locked, 1 visited
        dfs(G, 0, visited)
        r.. a..(e __ 1 ___ e __ visited)

    ___ dfs  G, u, visited
        visited[u] 1
        ___ nbr __ G[u]:
            __ n.. visited[nbr]:
                dfs(G, nbr, visited)


__ _______ __ _______
    ... Solution().canVisitAllRooms([[1],[2],[3],[]]) __ T..
    ... Solution().canVisitAllRooms([[1,3],[3,0,1],[2],[0]]) __ F..
