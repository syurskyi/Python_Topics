# c_ Event l..
#   ___ -c  $ $$
#     ___ item __ ?
#       ? $ $$
#
#
# c_ PropertyObservable
#   ___ -
#     ?property_changed _ E..
#
#
# c_ Person(PO..
#   ___ -  age_0
#     s__ . -
#     _? ?
#
#   ??
#   ___ can_vote
#     r_ _a.. >_ 18
#
#   ??
#   ___ age
#     r_ _a..
#
#   # @age.setter
#   # ___ age(self, value):
#   #   if self._age == value:
#   #     return
#   #   self._age = value
#   #   self.property_changed('age', value)
#
#   ??.?
#   ___ age  value
#     __ _a.. __ ?
#       r_
#
#     old_can_vote _ ?c..
#
#     ?_a.. _ ?
#     ?pr.. 'age' ?
#
#     __ o_c_v.. !+ ?c..
#       ?pr.. 'can_vote' ?c..
#
#
# __ _______ __ ______
#   ___ person_changed name, value
#     __ n.. __ 'can_vote'
#       print _*Voting status changed to |v.. ')
#
#   p = ?
#   ?.p___.ap.. (
#     p...
#   )
#
#   ___ age __ ra.. 16 21
#     print _*Changing age to |a.. ')
#     ?.a.. _ ?