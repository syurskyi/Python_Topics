# values = ["a", "b", "c"]
#
# ___ value __ ?
#     print ?
#
# # a
# # b
# # c
#
# index = 0
#
# ___ value __ ?
#     print ? ?
#     ? +_ 1
#
# # 0 a
# # 1 b
# # 2 c
#
# index = 0
#
# ___ value __ ?
#     print ? ?
#
# # 0 a
# # 0 b
# # 0 c
#
# ___ index __ ra_ le_ ?
#     value = ? ?
#     print ? ?
#
# # 0 a
# # 1 b
# # 2 c
#
# ___ count, value __ ? ?
#     print ? ?
#
# # 0 a
# # 1 b
# # 2 c
#
# print v.. 0
# # a
#
#
# ___ count value __ ? ? s.._1
#     print ? ?
#
# # 1 a
# # 2 b
# # 3 c
#
# ___ check_whitespace lines
#     """Check ___ whitespace and line length issues."""
#     ___ lno, line __ ? ?
#         __ "\r" __ ?
#             y___ ?+1, "\\r __ line"
#         __ "\t" __ ?
#             y___ ?+1, "OMG TABS!!!1"
#         __ ?|;-1 .r__(" \t") !_ ?|; -1
#             y___ ?+1, "trailing whitespace"

users = ["Test User", "Real User 1", "Real User 2"]
for index, user in enumerate(users):
    if index == 0:
        print("Extra verbose output for:", user)
    print(user)
#
# # Extra verbose output ___: Test User
# # Real User 1
# # Real User 2
#

def even_items(iterable):
    """Return items from ``iterable`` when their index is even."""
    values = []  # list
    for index, value in enumerate(iterable, start=1):
        if not index % 2:
            values.append(value)
    return values


def even_items(iterable):
    return [v for i, v in enumerate(iterable, start=1) if not i % 2]

# seq = l__ ra_ 1, 11
#
# print ?
# # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# even_items ?
# # [2, 4, 6, 8, 10]
#
# alphabet = "abcdefghijklmnopqrstuvwxyz"
#
# even_items a..
# # ['b', 'd', 'f', 'h', 'j', 'l', 'n', 'p', 'r', 't', 'v', 'x', 'z']
#
# l__ a.. 1;;2
# # ['b', 'd', 'f', 'h', 'j', 'l', 'n', 'p', 'r', 't', 'v', 'x', 'z']
#
# ___ a..
#     alpha = "abcdefghijklmnopqrstuvwxyz"
#     ___ a __ ?
#         y___ ?
#
# # alphabet[1::2]
# # Traceback (most recent call last):
# #   File "<stdin>", line 1, __ <module>
# # TypeError: 'function' object is no. subscriptable
#
# even_items a..
# # ['b', 'd', 'f', 'h', 'j', 'l', 'n', 'p', 'r', 't', 'v', 'x', 'z']
#
# ___ my_enumerate sequence s.._0
#     n = start
#     ___ elem __ ?
#         y___  ? ?
#         ? +_ 1
#
#
# seasons = ["Spring", "Summer", "Fall", "Winter"]
#
# ? ?
# # <generator object my_enumerate at 0x7f48d7a9ca50>
#
# l__ ? ?
# # [(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
#
# l__ ? ? s.._1
# # [(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]
#
# ####################### Unpacking Arguments With ?()
#
# tuple_2 = (10, "a")
# first_elem, second_elem = ?
# ?
# # 10
# ?
# # 'a'
#
# values = ["a", "b"]
# enum_instance = ? ?
# ?
# # <? at 0x7fe75d728180>
# n__ ?
# # (0, 'a')
# n__ ?
# # (1, 'b')
# # next(enum_instance)
# # Traceback (most recent call last):
# #   File "<stdin>", line 1, __ <module>
# # StopIteration
#
first = ["a", "b", "c"]
second = ["d", "e", "f"]
third = ["g", "h", "i"]
for one, two, three in zip(first, second, third):
    print(one, two, three)

# a d g
# b e h
# c f i

# ___ count |one two three __ ? z__ ? ? ?
#     print ? ? ? ?
#
# # 0 a d g
# # 1 b e h
# # 2 c f i
#
# ___ count |one two three __ ? z__ ? ? ?
#     print ? ? ? ?
#
# # 0 a d g
# # 1 b e h
# # 2 c f i
