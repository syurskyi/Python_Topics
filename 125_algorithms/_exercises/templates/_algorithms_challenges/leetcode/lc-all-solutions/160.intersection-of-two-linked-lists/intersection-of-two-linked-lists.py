class Solution:
  ___ getIntersectionNode(self, headA, headB
    __ headA is None or headB is None:
      r_ None
    pa = headA
    pb = headB
    w___ pa is not pb:
      pa = headB __ pa is None else pa.next
      pb = headA __ pb is None else pb.next
    r_ pa
