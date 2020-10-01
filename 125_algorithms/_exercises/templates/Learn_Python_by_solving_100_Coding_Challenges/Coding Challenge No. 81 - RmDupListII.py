# Remove Duplicates from Sorted List II
# Question: Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.
# For example:
# Given 1->2->3->3->4->4->5, return 1->2->5.
# Given 1->1->1->2->3, return 2->3.
# Solutions:

c_ ListNode:
    ___  -(self, x):
        val _ x
        next _ N..


c_ Solution:
    # @param head, a ListNode
    # @return a ListNode
    ___ deleteDuplicates(self, head):
        __ head __ N..:
            r_ N..
        dummy _ ListNode(10**10)
        dummy.next, head _ head, dummy # add a dummy node
        pprev, prev, curr, dupFlag _ head, head.next, head.next.next, F..
        w___ T..:
            __ dupFlag __ T..:
                __ curr __ N..:
                    pprev.next _ N..
                    b..
                __ prev.val !_ curr.val:
                    pprev.next, prev, dupFlag _ curr, curr, F..
            ____
                __ curr __ N..:
                    b..
                __ prev.val __ curr.val:
                    dupFlag _ T..
                ____
                    pprev, prev _ pprev.next, prev.next
            curr _ curr.next
        r_ head.next

    ___ printll(self, node):
        w___ node:
            print ( node.val )
            node _ node.next


__  -n __ '__main__':
    ll1, ll1.next, ll1.next.next _ ListNode(2), ListNode(2), ListNode(5)
    Solution().printll( Solution().deleteDuplicates(ll1) )