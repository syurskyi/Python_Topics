"""
Main Concept:

1. group the mans with same height and record origin index
2. record all heights
3. sort heights and iterate from end to start
4. get the corresponding mans and insert to `k` index

input: [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]

heights: [4, 5, 6, 7]

process:

7 [(0, 0), (1, 2)]  # input[0], input[2]
[[7, 0]]
[[7, 0], [7, 1]]

6 [(1, 4)]
[[7, 0], [6, 1], [7, 1]]

5 [(0, 3), (2, 5)]
[[5, 0], [7, 0], [6, 1], [7, 1]]
[[5, 0], [7, 0], [5, 2], [6, 1], [7, 1]]

4 [(4, 1)]
[[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]
"""


c_ Solution:
    ___ reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        ans    # list

        __ n.. people:
            r.. ans

        people.s..(key=l.... p: (p[0], -p[1]))

        ___ i __ r..(l..(people) - 1, -1, -1):
            ans.insert(people[i][1], people[i])

        r.. ans


c_ Solution:
    ___ reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        ans    # list

        __ n.. people:
            r.. ans

        h2mans    # dict
        heights    # list

        ___ i __ r..(l..(people)):
            h, k = people[i]

            __ h __ h2mans:
                h2mans[h].a..((k, i))
            ____:
                h2mans[h] = [(k, i)]
                heights.a..(h)

        heights.s..()

        ___ height __ heights[::-1]:
            ___ k, i __ s..(h2mans[height]):
                ans.insert(k, people[i])

        r.. ans
