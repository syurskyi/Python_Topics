# ____ a.. ______ A.. a..
# ______ ra..
#
# c_ AbstractSubject o..
#     """A common interface for the real and proxy objects."""
#
#     m...
#
#     ??
#     ___ sort reverse_F..
#         p..
#
# c_ RealSubject A..
#     """A class for a heavy object which takes a lot of memory space
#     and takes some time to instantiate."""
#
#     ___ -
#         digits _    # list
#
#         ___ i __ xr..  10000000
#             ?.ap.. ra___.ra..
#
#     ___ sort reverse_F..
#         d___.so..
#
#         __ r..
#             d___.re..
#
# c_ Proxy A..
#     """A proxy which has the same interface as RealSubject."""
#
#     reference_count _ 0
#
#     ___ -
#         """A constructor which creates an object if it is not exist and caches it otherwise."""
#
#         __ no. ge.. -c 'cached_object', N..
#             -c .c_o.. _ R..
#             print 'Created new object'
#         ____
#             print 'Using cached object'
#
#         -c .r_c.. +_ 1
#
#         print 'Count of references _ ', -c .r_c..
#
#     ___ sort  reverse_F..
#         """The args are logged by the Proxy."""
#
#         print 'Called sort method with args:'
#         print lo__.it..
#
#         -c .c_o_.so.. re.._re..
#
#     ___ -d
#         """Decreases a reference to an object, if the number of references is 0, delete the object."""
#         -c .r_c.. -_ 1
#
#         __ -c .r_c.. __ 0
#             print 'Number of reference_count is 0. Deleting cached object...'
#             de. -c .c_o..
#
#         print 'Deleted object. Count of objects _ ', -c .r_c..
#
# __ _______ __ ______
#     proxy1 _ P..
#     print
#
#     proxy2 _ P..
#     print
#
#     proxy3 _ P..
#     print
#
#     p_1.s.. re.._T..
#     print
#
#     print 'Deleting proxy2...'
#     del proxy2
#     print
#
#     print 'The other objects are deleted upon program termination...'
