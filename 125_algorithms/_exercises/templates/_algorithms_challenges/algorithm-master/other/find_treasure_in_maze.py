"""
http://acm.nyist.edu.cn/JudgeOnline/problem.php?pid=82


Description:
一个叫ACM的寻宝者找到了一个藏宝图，它根据藏宝图找到了一个迷宫，
这是一个很特别的迷宫，迷宫里有N个编过号的门（N<=5)，
它们分别被编号为A,B,C,D,E.为了找到宝藏，ACM必须打开门，
但是，开门之前必须在迷宫里找到这个打开这个门所需的所有钥匙（每个门都至少有一把钥匙），
例如：现在A门有三把钥匙，ACM就必须找全三把钥匙才能打开A门。
现在请你编写一个程序来告诉ACM，他能不能顺利的得到宝藏。

每组测试数据的第一行包含了两个整数M,N(1<N,M<20)，分别代表了迷宫的行和列。接下来的M每行有N个字符，描述了迷宫的布局。其中每个字符的含义如下：
.表示可以走的路
S:表示ACM的出发点
G:表示宝藏的位置
X:表示这里有墙，ACM无法进入或者穿过。
A,B,C,D,E表示这里是门，a,b,c,d,e表示对应大写字母的门上的钥匙。
注意ACM只能在迷宫里向上下左右四个方向移动。


Testing:
>>> s = Solution()
>>> gotcha = []
>>> for _in, _out in (
...     (['S.X.', 'a.X.', '..XG', '....'], True),
...     (['S.Xa', '.aXB', 'b.AG'], False),
...     (['aX.S', 'bXAB', 'cXCD', 'dXGX'], False),
...     (['SbAdX.', 'a.BD.G', 'cBCdaX'], True),
...     (['S.Aa.X.', 'a.Xc.C.', 'b.X..DG', '.cB..Xd'], True),
...
...     res = s.find_treasure_in_maze(_in)
...     if res != _out: print(_in, res)
...     gotcha.append(res == _out)
>>> bool(gotcha) and all(gotcha)
True
"""


class Solution:
    START = 'S'
    GOLD = 'G'
    OBSTACLE = 'X'
    EMPTY = '.'
    DOORS = 'ABCDE'
    KEYS = 'abcde'

    ___ find_treasure_in_maze(self, maze
        """
        :type maze: list[str]
        :rtype: bool
        """
        __ not maze or not maze[0]:
            r_ False

        m, n = le.(maze), le.(maze[0])
        k = le.(self.DOORS)
        keys = [0] * k  # all keys count
        has_gold = False

        queue = []
        doors = [None] * k  # doors meet when bfs
        holds = [0] * k  # keys meet when bfs
        visited = set()  # visited cell when bfs

        ___ x in range(m
            ___ y in range(n
                __ maze[x][y] __ self.START:
                    queue.append((x, y))
                ____ maze[x][y] __ self.GOLD:
                    has_gold = True
                ____ maze[x][y] in self.KEYS:
                    i = ord(maze[x][y]) - ord('a')
                    keys[i] += 1

        __ not has_gold or not queue:
            r_ False

        w___ queue or self.is_possible(maze, keys, holds, doors
            __ self.bfs(maze, queue, keys, holds, doors, visited
                r_ True

        r_ False

    ___ bfs(self, maze, queue, keys, holds, doors, visited
        """
        return True if got gold, otherwise False

        :type maze: list[str]
        :type queue: list[tuple[int]]
        :type keys: list[int]
        :type holds: list[int]
        :type doors: list[tuple[int]]
        :type visited: set[tuple[int]]
        :rtype: bool
        """
        m, n = le.(maze), le.(maze[0])

        ___ x, y in queue:
            ___ dx, dy in (
                (0, -1), (0, 1),
                (-1, 0), (1, 0),

                _x = x + dx
                _y = y + dy

                __ not (0 <= _x < m and 0 <= _y < n
                    continue
                __ (_x, _y) in visited or maze[_x][_y] __ self.OBSTACLE:
                    continue
                __ maze[_x][_y] __ self.GOLD:
                    r_ True

                __ maze[_x][_y] in self.DOORS:
                    i = ord(maze[_x][_y]) - ord('A')
                    __ holds[i] < keys[i]:
                        doors[i] = (_x, _y)
                        continue
                    doors[i] = None

                __ maze[_x][_y] in self.KEYS:
                    i = ord(maze[_x][_y]) - ord('a')
                    holds[i] += 1

                visited.add((_x, _y))
                queue.append((_x, _y))

        queue.clear()
        r_ False

    ___ is_possible(self, maze, keys, holds, doors
        """
        :type maze: list[str]
        :type keys: list[int]
        :type holds: list[int]
        :type doors: list[tuple[int]]
        :rtype: bool
        """
        ___ door in doors:
            __ not door:
                continue

            x, y = door
            i = ord(maze[x][y]) - ord('A')
            __ holds[i] >= keys[i]:
                r_ True

        r_ False
