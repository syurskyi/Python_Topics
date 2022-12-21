# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

c_ Solution o..
    # def copyRandomList(self, head):
    #     """
    #     :type head: RandomListNode
    #     :rtype: RandomListNode
    #     """
    #     # hash O(n) and O(n)
    #     dic = collections.defaultdict(lambda: RandomListNode(0))
    #     dic[None] = None
    #     n = head
    #     while n:
    #         dic[n].label = n.label
    #         dic[n].next = dic[n.next]
    #         dic[n].random = dic[n.random]
    #         n = n.next
    #     return dic[head]

    # def copyRandomList(self, head):
    #     # hash O(n) and O(n)
    #     dic = {}
    #     dic[None] = None
    #     dummyHead = RandomListNode(0)
    #     p, q = head, dummyHead
    #     while p is not None:
    #         q.next = RandomListNode(p.label)
    #         dic[p] = q.next
    #         p = p.next
    #         q = q.next
    #     p, q = head, dummyHead
    #     while p is not None:
    #         q.next.random = dic[p.random]
    #         p = p.next
    #         q = q.next
    #     return dummyHead.next

    ___ copyRandomList  head
        # Modify original structure: Original->Copy->Original->Copy
        # node.next.random = node.random.next
        # O(n) and O(1)
        p = head
        w.. p is n.. N..:
            next = p.next
            copy = RandomListNode(p.label)
            p.next = copy
            copy.next =  next
            p = next
        p = head
        w.. p is n.. N..:
            __ p.random is n.. N..:
                p.next.random = p.random.next
            p = p.next.next
        p = head
        __ p is n.. N..:
            headCopy = p.next
        ____
            headCopy = N..
        w.. p is n.. N..:
            copy = p.next
            p.next = copy.next
            p = p.next
            __ p is n.. N..:
                copy.next = p.next
        r_ headCopy