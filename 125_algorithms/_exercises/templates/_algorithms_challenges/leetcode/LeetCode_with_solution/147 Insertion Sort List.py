__author__ = 'Danyang'
# Definition for singly-linked list.
c_ ListNode:
    ___ - , x):
        val = x
        next = N..

c_ Solution:
    # ascending
    ___ insertionSortList_TLE(self, head):
        """
        Time Limit Exceded
        """
        comparator = l.... x, y: cmp(x.val, y.val)
        # open set & closed set
        dummy_head = ListNode(0)
        dummy_head.next = head


        closed_tail = dummy_head.next
        w....(closed_tail a.. closed_tail.next):
            open_head = closed_tail.next
            # open_head_next = closed_tail.next.next

            # find position
            ptr_before = dummy_head
            ptr = dummy_head.next # error using ptr = head

            # WHILE OUTSIDE IF THUS INCREASING TIME COMPLEXITY
            w....(ptr_before):
                __ comparator(ptr, open_head)>0:
                    ptr_before.next = open_head
                    closed_tail.next = open_head.next
                    open_head.next = ptr

                    # closed_tail.next = open_head_next
                    break

                __ ptr__open_head:
                    closed_tail = closed_tail.next
                    break

                ptr_before = ptr_before.next
                ptr = ptr.next


        r.. dummy_head.next


    ___ insertionSortList(self, head):
        """
        O(n^2), but with better performance since while loop inside a if

        [ [closed_lst], [open_lst] ], insert the first item of open_lst into the closed_lst:
        1. compare the first item the last item of the closed_lst
        2. if in order, continue to next
        3. if not, find the insertion point and insert

        :param head: ListNode
        :return: ListNode
        """
        comparator = l.... x, y: cmp(x.val, y.val)
        # open set & closed set
        # iterate through all the nodes
        dummy = ListNode(0)  # Singly-linked list, thus need dummy_head
        dummy.next = head

        closed_tail = head
        w.... (closed_tail a.. closed_tail.next):
            open_head = closed_tail.next
            open_head_next = closed_tail.next.next
            __ n.. comparator(closed_tail, open_head)<=0:  # Step 1: only compare the closed set tail and open set head

                pre = dummy
                w.... comparator(pre.next, open_head)<0:  # Step 2: find position
                    pre = pre.next

                # swap nodes
                open_head.next = pre.next
                pre.next = open_head

                closed_tail.next = open_head_next

            ____:
                closed_tail = closed_tail.next


        r.. dummy.next

__ __name____"__main__":
    _______ r__
    lst = [ListNode(i) ___ i __ r__.sample(xrange(-1000, 1000), 1000)]
    # lst = [ListNode(1), ListNode(3), ListNode(2)]
    # lst = [ListNode(i) for i in range(10, -1, -1)]
    ___ i __ r..(l..(lst)):
        try:
            lst[i].next = lst[i+1]
        except IndexError: # last
            lst[i].next = N..



    head = Solution().insertionSortList(lst[0])
    current = head
    ___ i __ r..(l..(lst)):
        print current.val
        current = current.next



