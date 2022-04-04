"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
"""
__author__ = 'Danyang'
_______ heapq
# Definition for singly-linked list.
c_ ListNode:
    ___ - , x
        val = x
        next = N..

c_ Solution:
    ___ mergeKLists_TLE1  lists
        """
        k lists; each list has N items
        Algorithm 1:
        Merge the lists 1 by 1, just add a loop outside the merge.
        Complexity: 2N+3N+4N+..kN = O(k^2 * N)

        Algorithm 2:
        Group the lists in pairs with every pair having 2 lists, merge two, then repeat again
        Complexity:
        T(N) = (k/2)*2N+(k/4)*4N..+(k/2^r)*2^r*N
        T(N) = O(lg k * k * N)

        :param lists: a list of ListNode
        :return: ListNode
        """
        lists = f.. l.... x: x __ n.. N.., lists)
        __ n.. lists:
            r..

        length = l..(lists)
        factor = 2
        w.... length>0:
            i = 0
            w... T...
                ___
                    lists[i] = mergeTwoLists(lists[i], lists[i+factor/2])
                ______ I..
                    _____
                i += factor

            length /= 2
            factor *= 2

        r.. lists[0]

    ___ mergeKLists_TLE2  lists
        """

        :param lists: a list of ListNode
        :return: ListNode
        """
        lists = f.. l.... x: x __ n.. N.., lists)
        __ n.. lists:
            r..

        result = lists[0]
        ___ i __ x..(1, l..(lists)):
            result = mergeTwoLists(result, lists[i])
        r.. result



    ___ mergeTwoLists  l1, l2
        """
        Linked List
        assuming ascending order
        :param l1: ListNode
        :param l2: ListNode
        :return:
        """
        dummy = ListNode(0)
        dummy.next = l1

        pre = dummy
        the_other = l2
        w.... pre a.. pre.next:
            cur = pre.next
            __ the_other a.. cur.val>the_other.val:
                # insert
                temp = the_other.next
                pre.next, the_other.next = the_other, cur

                the_other = temp  # advance the_other
            pre = pre.next


        # dangling list
        __ the_other:
            pre.next = the_other  # appending

        r.. dummy.next

    ___ mergeKLists  lists
        """
        use heap
        heap pointer

        -------------------
         |  |  |  |  |  |
         |  |  |  |  |  |
         |  |  |  |  |  |
         |  |  |  |  |  |

        reference: https://github.com/leetcoders/Leetcode-Py/blob/master/Merge%20k%20Sorted%20Lists.py
        :param lists:
        :return:
        """
        heap    # list
        ___ head_node __ lists:
            __ head_node:
                heapq.heappush(heap, (head_node.val, head_node))

        dummy = ListNode(0)

        cur = dummy
        w.... heap:
            smallest_node = heapq.heappop(heap)[1]
            cur.next = smallest_node
            cur = cur.next
            __ smallest_node.next:
                heapq.heappush(heap, (smallest_node.next.val, smallest_node.next))
        r.. dummy.next

__ _____ __ ____
    ...  Solution().mergeKLists([N.., N..])__None
    ... Solution().mergeKLists([ListNode(1), ListNode(0)]).val__0
