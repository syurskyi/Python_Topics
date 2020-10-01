# Merge k Sorted Lists
# Question: Merge k sorted linked lists and return it as one sorted list. Analyse and describe its complexity.
# Solutions:


c_ ListNode:
    ___  -(self, x):
        val _ x
        next _ N..


c_ Solution:
    # @param a list of ListNode
    # @return a ListNode
    ___ mergeKLists(self, lists):
        __ le.(lists)__0:
            r_ N..
        w___ le.(lists)>1:
            nextLists _   # list
            ___ i __ ra..(0,le.(lists)-1,2):
                nextLists.ap..(mergeLists(lists[i],lists[i+1]))
            __ le.(lists)%2__1:
                nextLists.ap..(lists[le.(lists)-1])
            lists _ nextLists
        r_ lists[0]

    ___ mergeLists(self, list1, list2):
        dummy _ ListNode(0)
        li.. _ dummy
        w___ list1 !_ N.. an. list2 !_ N..:
            __ list1.val < list2.val:
                li...next _ list1
                list1 _ list1.next
            ____
                li...next _ list2
                list2 _ list2.next
            li.. _ li...next
        __ list1 __ N..:
            li...next _ list2
        ____
            li...next _ list1
        r_ dummy.next

    ___ printll(self, node):
        w___ node:
            print ( node.val )
            node _ node.next
__  -n __ '__main__':
    ll1, ll1.next, ll1.next.next _ ListNode(2), ListNode(3), ListNode(5)
    ll2, ll2.next, ll2.next.next _ ListNode(4), ListNode(7), ListNode(15)
    ll3, ll3.next, ll3.next.next _ ListNode(6), ListNode(9), ListNode(10)
    Solution().printll( Solution().mergeKLists([ll1,ll2,ll3]) )