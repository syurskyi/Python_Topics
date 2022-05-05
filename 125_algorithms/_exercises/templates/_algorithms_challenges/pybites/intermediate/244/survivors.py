# _______ __
# ____ p.. _______ P..
# ____ u__.r.. _______ u..
#
# S3 "https://bites-data.s3.us-east-2.amazonaws.com/{}"
# FILE_NAME "mutpy.out"
# TMP __.g.. ?  /tmp
# PATH P.. ? ?
#
# __ n.. ?.e..
#     u.. S_.f.. ? ?
#
#
# ___ _get_data p.._?
#     w__ o.. p.. __ f
#         r..  line.r.. ___ ? __ ?.r..
#
#
# ___ filter_killed_mutants mutpy_output l.. N.. __ l..
#     """Read in the passed in mutpy output and filter out the code snippets of
#        mutation tests that were killed. Surviving mutants should be shown in
#        full, as well the surrounding output.
#
#        For example, this is a killed mutant:
#
#          - [#  15] DDL account:
#       --------------------------------------------------------------------------------
#         23:         if not (isinstance(amount, int)):
#         24:             raise ValueError('please use int for amount')
#         25:         self._transactions.append(amount)
#         26:
#       - 27:     @property
#       - 28:     def balance(self):
#       + 27:     def balance(\
#       + 28:         self):
#         29:         return self.amount + sum(self._transactions)
#         30:
#         31:     def __len__(self):
#         32:         return len(self._transactions)
#       --------------------------------------------------------------------------------
#       [0.10240 s] killed by test_account.py::test_balance
#
#       You should reduce this to:
#
#          - [#  15] DDL account:
#       [0.10240 s] killed by test_account.py::test_balance
#
#       So you mute all that is in between the two dashed lines.
#
#       You do the same for incompetent mutants, for example:
#          - [#   3] AOR account:
#       --------------------------------------------------------------------------------
#         43:     def __add__(self, other):
#         44:         owner = '{}&{}'.format(self.owner, other.owner)
#         45:         start_amount = self.amount + other.amount
#         46:         acc = Account(owner, start_amount)
#       - 47:         for t in list(self) + list(other):
#       + 47:         for t in list(self) - list(other):
#         48:             acc.add_transaction(t)
#         49:         return acc
#       --------------------------------------------------------------------------------
#       [0.10011 s] incompetent
#
#       ... becomes:
#          - [#   3] AOR account:
#       [0.10011 s] incompetent
#
#       Return the filtered output as a list of lines.
#     """
#
#     __ mutpy_output __ N..
#         mutpy_output ?
#
#
#     previous_dashed_line N..
#
#
#     filtered    # list
#
#
#     filters ("killed",'incompetent')
#
#     i 0
#     code_block N..
#     previous_dashed_line F..
#     w.... i < l.. m..
#         line m.. ?
#         __ c..
#             c__.a.. ?
#         __ l__.s.. '---'
#             __ n.. p..
#                 p.. T..
#                 c.. ?
#             ____
#                 __ a.. fil n.. __ m.. ? +1] ___ ? __ f..
#                     f__.e.. c..
#                 c.. N..
#                 p.. N..
#         ____ n.. c..
#             f__.a.. ?
#         ? +_ 1
#
#
#     r.. ?
#
# __ _______ __ _______
#
#
#     ?
