# # Counter
# # The Counter dictionary is one that specializes ___ helping with, you guessed it, counters!
# # Actually we used a defaultdict earlier to do something similar:
#
# f_ c.. _____ d__d__ C...
#
# # Let's say we want to count the frequency of each character i_ a string:
#
# sentence _ 'the quick brown fox jumps over the lazy dog'
# counter _ d__d__ i_.
#
# ___ c i_ se..
#     c... c  +_ 1
#
# c...
#
# # defaultdict(int,
# #             {'t': 2,
# #              'h': 2,
# #              'e': 3,
# #              ' ': 8,
# #              'q': 1,
# #              'u': 2,
# #              'i': 1,
# #              'c': 1,
# #              'k': 1,
# #              'b': 1,
# #              'r': 2,
# #              'o': 4,
# #              'w': 1,
# #              'n': 1,
# #              'f': 1,
# #              'x': 1,
# #              'j': 1,
# #              'm': 1,
# #              'p': 1,
# #              's': 1,
# #              'v': 1,
# #              'l': 1,
# #              'a': 1,
# #              'z': 1,
# #              'y': 1,
# #              'd': 1,
# #              'g': 1})
#
# # We can do the same thing using a Counter - unlike the defaultdict we don't specify a default factory -
# # it's always zero (it's a counter after all):
#
# counter _ C..
# ___ c i_ se..
#     c... c +_ 1
#
# c...
#
# # Counter({'t': 2,
# #          'h': 2,
# #          'e': 3,
# #          ' ': 8,
# #          'q': 1,
# #          'u': 2,
# #          'i': 1,
# #          'c': 1,
# #          'k': 1,
# #          'b': 1,
# #          'r': 2,
# #          'o': 4,
# #          'w': 1,
# #          'n': 1,
# #          'f': 1,
# #          'x': 1,
# #          'j': 1,
# #          'm': 1,
# #          'p': 1,
# #          's': 1,
# #          'v': 1,
# #          'l': 1,
# #          'a': 1,
# #          'z': 1,
# #          'y': 1,
# #          'd': 1,
# #          'g': 1})
#
# # OK, so if that's all there was to Counter it would be pretty odd to have a data structure different than OrderedDict.
# # But Counter has a slew of additional methods which make sense i_ the context of counters:
# #     Iterate through all the elements of counters, but repeat the elements as many times as their frequency
# #     Find the n most common (by frequency) elements
# #     Decrement the counters based on another Counter (or iterable)
# #     Increment the counters based on another Counter (or iterable)
# #     Specialized constructor ___ additional flexibility
# # If you are familiar with multisets, then this is essentially a data structure that can be used ___ multisets.
