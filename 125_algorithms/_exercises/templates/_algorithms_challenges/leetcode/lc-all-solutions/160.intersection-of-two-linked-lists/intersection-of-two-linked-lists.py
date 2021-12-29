class Solution:
  ___ getIntersectionNode(self, headA, headB):
    __ headA is None or headB is None:
      return None
    pa = headA
    pb = headB
    while pa is not pb:
      pa = headB __ pa is None else pa.next
      pb = headA __ pb is None else pb.next
    return pa
