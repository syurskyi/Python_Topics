# """Prototype pattern
# """
# ____ c____ ______ de..
#
#
# c_ InstanceNotAvailable E..
#     p..
#
#
# ___ prototype hash_function_id auto_register_F.. debug_F..
#     """Implement the Prototype pattern on a class.
#
#     The decorated class gains the following methods:
#       - register
#       - unregister
#       - clone (@classmethod)
#       - identifier (@property)
#       - available_identifiers (@staticmethod)
#
#     Parameters
#     ----------
#     hash_function : function
#         a function
#     auto_register : bool
#         if True, automatically add objects to instance pool at instantiation
#     debug : bool
#         if True, show some documentation while using this decorator
#
#     Returns
#     -------
#     inner : function
#     """
#
#     ___ inner klass
#         instance_pool _ di..
#
#         c_ Decorated kl..
#
#             ___ - $  $$
#                 """Call __init__ of original class and assign an identifier.
#
#                 Parameters
#                 ----------
#                 args : tuple
#                     args to pass to the __init__ of the original class
#                 kwargs : dict
#                     kwarg to pass to the __init__ of the original class
#                 """
#                 ?. -  $  $$
#                 _identifier _ h.. ____
#
#             ___ -r $  $
#                 klass_repr _ k___. -r ____ $  $$
#                 r_ "@ (id: @)".f... ? .i..
#
#             ___ register
#                 """Add this instance to the instance pool."""
#                 i_p__.up.. .i.. ____
#                 __ debug
#                     print("@ registered".f... self.i..
#
#             ___ unregister
#                 """Remove this instance from the instance pool."""
#                 __ debug
#                     print("@ unregistered".f... .i..
#                 de. i_p_|.i..
#
#             ?p..
#             ___ identifier
#                 """Return the identifier of this instance."""
#                 r_ _i..
#
#             ??.?
#             ___ identifier value
#                 _i.. _ ?
#
#         D___. -n _ k__. -n
#
#         c_ ClassObject
#
#             ___ -r
#                 r_ k___. -n
#
#             __str__ _ __repr__
#
#             ___ -c $  $$
#                 __ debug
#                     print("@.__call__ (prototype)".f... st. ____
#                 decorated_instance _ D.. $ $$
#                 __ auto_register
#                     ?.r..
#                 r_ ?
#
#             ?c..
#             ___ clone ___ identifier
#                 """Get an instance from the pool and return it to the caller.
#
#                 Parameters
#                 ----------
#                 identifier : int
#                     identifier for an instance
#
#                 Raises
#                 ------
#                 InstanceNotAvailable
#                     if the instance is not available in the instance pool
#
#                 Returns
#                 -------
#                 cloned_obj : decorated class
#                     instance of the decorated class
#                 """
#                 ___
#                     original_object _ i_p..|i..
#                     cloned_obj _ de... o_o..
#                     r_ ?
#
#                 ______ K...
#                     r_ I.. (
#                         "Instance with identifier @ not found.\nWas it "
#                         "registered?\nThe available identifiers are: @".f...(
#                             i.., ___.a_i..
#                         )
#                     )
#
#             ?s..
#             ___ available_identifiers
#                 """Return the identifiers stored in the instance pool.
#
#                 Returns
#                 -------
#                 list
#                     identifiers of all instances available in instance pool.
#                 """
#                 r_ li.. i_p...ke..
#
#         r_ CO..
#
#     r_ i..
#
#
# ?p.. ha..
# c_ Point o...
#
#     ___ - x y
#         print("@__init__ (original class)".f...  . -c. -n
#         ?  ?
#         ?  ?
#
#     ___ -r
#         r_ "@(@, @)".f... ? -c. -n .x .y
#
#     ___ move x y
#         .x +_ x
#         .y +_ y
#
#
# # TODO: how can we inherit from Point?
#
# # we will decorate this class later
#
#
# c_ Stuff o..
#     p..
#
#
# c_ MoreStuff S..
#     p..
#
#
# ___ main(
#     print("\nCreate 2 points")
#     print("p1")
#     p1 _ P.. (x_3, y_5)
#     print(p1)
#     print("p2")
#     p2 _ P.. (x_100, y_150)
#     print(p2)
#     print("p1.identifier !_ p2.identifier")
#     assert p1.i.. !_ p2.i..
#
#     print("\nIdentifiers in the instance pool")
#     print(P___.a_i..
#
#     print(
#         "\nThe instance pool is empty because we didn't register any "
#         "instance. Let's fix this"
#     )
#     p1.r..
#     p2.r..
#     print P__.a_i..
#
#     print("\nCreate a point by cloning p1 (__init__ is not called)")
#     p3 _ P___.cl.. p1.i..
#     print(p3)
#     print("Create a point by cloning p3 (which is a clone of p1)")
#     p4 _ P__.cl.. p3.i..
#     print(p4)
#     print("p1.identifier == p3.identifier == p4.identifier")
#     assert p1.i.. __ p3.i.. __ p4.i..
#
#     print("\nIdentifiers in the instance pool")
#     print(P___.a_i..
#
#     print("\nmove p1")
#     p1.m.. 5, 7
#     print(p1)
#     # p3 and p4 are not weak references of p1, they are deep copies
#     print("if p1 moves, p3 and p4 are unaffected")
#     print(p3)
#     print(p4)
#
#     print("\nunregister p1")
#     p1.u..
#     print("p1 cannot be cloned because it was unregistered")
#     try:
#         Point.clone(p1.i..)
#     ______ InstanceNotAvailable __ e
#         print ?
#     print("but p1 still exists")
#     print(p1)
#
#     # TODO: this behavior might be undesirable
#     print(
#         "\nEven if we destroy p2, it's not removed from the instance pool, "
#         "so if we know the identifier we can still clone it"
#     )
#     identifier _ de... p2.i..
#     del p2
#     print(P__.a_i..
#     P___.cl.. i..
#
#     print("\nwith a wrong identifier we get a ValueError exception")
#     wrong_identifier _ 123456789
#     ___
#         P___.cl.. ?
#     ______ INA.. __ e
#         print ?
#
#     print("\nDecorate a new class")
#     proto _ p... auto_register_T.. debug_T..
#     StuffDecorated _ ? S..
#
#     s1 _ SD___
#     SD___.cl.. s1.i..
#     print("\nInstance pools are different for each class")
#     print("StuffDecorated.available_identifiers")
#     print(SD__.a_i..
#     print("Point.available_identifiers")
#     print(P__.a_i..
#
#     proto _ pr... auto_register_T..
#     MoreStuffDecorated _ pr... MS..
#     ?
#     print("MoreStuffDecorated.available_identifiers")
#     print ?.a_i..
#
#
# __ _______ __ ________
#     ?
