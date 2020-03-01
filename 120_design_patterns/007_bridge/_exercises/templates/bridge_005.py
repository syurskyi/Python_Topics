# """Bridge pattern
#
# Bridge is a structural design pattern. It separates responsibilities into two
# orthogonal class hierarchies: implementation and interface. Bridge decouples an
# abstraction from its implementation so that the two can vary independently.
#
# The interface class encapsulates an instance of a concrete implementation class.
# The client interacts with the interface class, and the interface class in turn
# "delegates" all requests to the implementation class.
#
# Adapter makes things work after they're designed; Bridge makes them work before
# they are.
# """
# ____ a.. ______ A.. a..
#
#
# # Abstract Interface (aka Handle) used by the client
#
#
# c_ Website A..
#
#     ___ - implementation)
#         # encapsulate an instance of a concrete implementation class
#         _?  ?
#
#     ___ -s
#         r_ "Interface: @; Implementation: @".f..(
#             . -c . -n _i___. -c . -n
#         )
#
#     ??
#     ___ show_page
#         p..
#
#
# # Concrete Interface 1
#
#
# c_ FreeWebsite W...
#
#     ___ show_page
#         ads _ _i__.g_a.
#         text _ self._i___.g_e..
#         call_to_action _ _i___.g_t_a
#         print a..
#         print t..
#         print c..
#         print("")
#
#
# # Concrete Interface 2
#
#
# c_ PaidWebsite W..
#
#     ___ show_page
#         text _ _i___.g_a..
#         print ?
#         print("")
#
#
# # Abstract Implementation (aka Body) decoupled from the client
#
#
# c_ Implementation A..
#
#     ___ get_excerpt
#         r_ "excerpt from the article"
#
#     ___ get_article
#         r_ "full article"
#
#     ___ get_ads
#         r_ "some ads"
#
#     ??
#     ___ get_call_to_action
#         p..
#
#
# # Concrete Implementation 1
#
#
# c_ ImplementationA I..
#
#     ___ get_call_to_action
#         r_ "Pay 10 $ a month to remove ads"
#
#
# # Concrete Implementation 2
#
#
# c_ ImplementationB I..
#
#     ___ get_call_to_action
#         r_ "Remove ads with just 10 $ a month"
#
#
# # Client
#
#
# ___ main
#     a_free _ F.. I_A
#     print ?
#     ?.s_p..
#
#     b_free _ F.. I_B
#     print ?
#     ?.s_p..
#
#     a_paid _ P... I_A
#     print ?
#     ?.s_p..
#
#     b_paid _ P.. I_B
#     print ?
#     ?.s_p..
#
#     # in a real world scenario, we could perform A/B testing of our website by
#     # choosing a random implementation
#     ______ ra..
#
#     impl _ ra__.ch.. I_A I_B
#     print FW.. ?
#
#
# __ _______ __ ______
#     ?
