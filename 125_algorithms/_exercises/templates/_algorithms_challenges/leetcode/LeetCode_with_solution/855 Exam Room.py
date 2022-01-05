#!/usr/bin/python3
"""
In an exam room, there are N seats in a single row, numbered 0, 1, 2, ..., N-1.

When a student enters the room, they must sit in the seat that maximizes the
distance to the closest person.  If there are multiple such seats, they sit in
the seat with the lowest number.  (Also, if no one is in the room, then the
student sits at seat number 0.)

Return a class ExamRoom(int N) that exposes two functions: ExamRoom.seat()
returning an int representing what seat the student sat in, and
ExamRoom.leave(int p) representing that the student in seat number p now leaves
the room.  It is guaranteed that any calls to ExamRoom.leave(p) have a student
sitting in seat p.

Example 1:

Input: ["ExamRoom","seat","seat","seat","seat","leave","seat"],
[[10],[],[],[],[],[4],[]]
Output: [null,0,9,4,2,null,5]
Explanation:
ExamRoom(10) -> null
seat() -> 0, no one is in the room, then the student sits at seat number 0.
seat() -> 9, the student sits at the last seat number 9.
seat() -> 4, the student sits at the last seat number 4.
seat() -> 2, the student sits at the last seat number 2.
leave(4) -> null
seat() -> 5, the student sits at the last seat number 5.
​​​​​​​
Note:

1 <= N <= 10^9
ExamRoom.seat() and ExamRoom.leave() will be called at most 10^4 times across
all test cases.
Calls to ExamRoom.leave(p) are guaranteed to have a student currently sitting in
seat number p.
"""
_______ bisect


c_ ExamRoom:
    ___ - , N: i..):
        """
        Maintain a sorted array of index. BST
        BST -> bisect sort
        O(N) per query
        """
        N = N
        idxes    # list  # sorted arry of taken idx

    ___ seat(self) __ i..:
        """
        similar to 849
        """
        __ n.. idxes:
            ret_idx = 0
        ____:
            max_dist, ret_idx = 0, 0
            # begin
            dist = idxes[0] - 0
            __ dist > max_dist:
                max_dist = dist
                ret_idx = 0
            # middle
            ___ j __ r..(l..(idxes)-1):
                i = (idxes[j] + idxes[j+1]) // 2
                dist = m..(abs(idxes[j] - i), abs(idxes[j+1] - i))
                __ dist > max_dist:
                    max_dist = dist
                    ret_idx = i
            # end
            dist = N-1 - idxes[-1]
            __ dist > max_dist:
                max_dist = dist
                ret_idx = N-1

        bisect.insort(idxes, ret_idx)
        r.. ret_idx

    ___ leave  p: i..) __ N..
        idxes.remove(p)


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(N)
# param_1 = obj.seat()
# obj.leave(p)
