#!/usr/bin/python3
"""
Alice has a hand of cards, given as an array of integers.

Now she wants to rearrange the cards into groups so that each group is size W,
and consists of W consecutive cards.

Return true if and only if she can.



Example 1:

Input: hand = [1,2,3,6,2,3,4,7,8], W = 3
Output: true
Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8].
Example 2:

Input: hand = [1,2,3,4,5], W = 4
Output: false
Explanation: Alice's hand can't be rearranged into groups of 4.


Note:

1 <= hand.length <= 10000
0 <= hand[i] <= 10^9
1 <= W <= hand.length
"""
____ typing _______ List
____ c.. _______ Counter, d..
_______ heapq


c_ Solution:
    ___ isNStraightHand  A: List[i..], W: i..) __ b..:
        """
        sort + queue

        prev = previous value
        prev_cnt = previous value count
        """
        q = d..()
        counter = Counter(A)
        prev = 0
        prev_cnt = 0
        ___ k __ s..(counter  # sorted by key
            __ prev_cnt > counter[k] o. prev_cnt > 0 a.. k > prev + 1:
                r.. F..
                
            q.a..(counter[k] - prev_cnt)
            prev, prev_cnt = k, counter[k]
            __ l..(q) __ W:
                c = q.popleft()
                prev_cnt -= c

        r.. prev_cnt __ 0

    ___ isNStraightHand_heap  A: List[i..], W: i..) __ b..:
        """
        sort + heap
        O(N log N + N log N)
        """
        A.s..()
        __ l..(A) % W != 0:
            r.. F..
        __ W __ 1:
            r.. T..


        h    # list  # tuple of (-3, [1, 2, 3])
        ___ a __ A:
            __ n.. h:
                h = [(a, [a])]
                _____

            __ a __ h[0][1][-1]:
                heapq.heappush(h, (a, [a]))
            ____ a __ h[0][1][-1] + 1:
                _, lst = heapq.heappop(h)
                lst.a..(a)
                __ l..(lst) < W:
                    heapq.heappush(h, (a, lst))
            ____:
                r.. F..

        __ h:
            r.. F..

        r.. T..


__ _______ __ _______
    ... Solution().isNStraightHand([1,2,3,6,2,3,4,7,8], 3) __ T..
    ... Solution().isNStraightHand([1,1,2,2,3,3], 3) __ T..
