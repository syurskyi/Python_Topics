# c_ Subscriber o..
#     """It's the Observer object. It receives messages from the Observable."""
#
#     ___ - name
#         ?  ?
#
#     ___ receive  message
#         """Method assigned in, and called by, the Publisher.
#
#         This method is assigned when the Publisher registers a Subscriber to a
#         newsletter, and it's called when the Publisher dispatches a message.
#
#         Parameters
#         ----------
#         message : str
#         """
#         print("@ received: @".f.. ?n.. m.
#
#
# c_ Publisher o..
#     """It's the Observable object. It dispatches messages to the Observers."""
#
#     ___ - newsletters
#         ?subscriptions _ di..
#         ___ newsletter __ ?
#             ?ad.. ?
#
#     ___ get_subscriptions newsletter
#         r_ ?subscriptions ?
#
#     ___ register  newsletter who callback_N..
#         """Register a Subscriber to this newsletter.
#
#         Parameters
#         ----------
#         newsletter : str
#         who : Subscriber
#         callback : method
#             callback function bound to the Subscriber object
#         """
#         __ ? __ N..
#             ? _ ge.. who "receive"
#         ?g_su.. n.. |w.. _ c..
#
#     ___ unregister  newsletter who
#         """Remove a Subscriber object from a subscription to a newsletter.
#
#         Parameters
#         ----------
#         newsletter : str
#         who : Subscriber
#         """
#         ___
#             del ?g_s.. n.. |w..
#         _______ K...
#             print(
#                 "@ is not subscribed to the @ newsletter!".f..(
#                     w__.n.. n...
#                 )
#             )
#
#     ___ dispatch newsletter message
#         """Send a message to all subscribers registered to this newsletter.
#
#         Parameters
#         ----------
#         newsletter : str
#         message : str
#         """
#         __ le. ?ge.. n___.it.. __ 0
#             print(
#                 "No subscribers for the @ newsletter. Nothing to send!".f..(
#                     n...
#                 )
#             )
#             r_
#
#         ___ subscriber, callback __ ?g.. |n___.it..
#             c.. m..
#
#     ___ add_newsletter  newsletter
#         """Add a subscription key-value pair for a new newsletter.
#
#         The key is the name of the new subscription, namely the name of the
#         newsletter (e.g. 'Tech'). The value is an empty dictionary which will be
#         populated by subscriber objects willing to register to this newsletter.
#
#         Parameters
#         ----------
#         newsletter : str
#         """
#         ?su.. |n... _ di..
#
#
# ___ m..
#
#     pub = P.. n.._["Tech", "Travel"])
#
#     tom = S..("Tom")
#     sara = S..("Sara")
#     john = S..("John")
#
#     p__.r.. n.._"Tech" w.._tom
#     p__.r.. n.._"Travel" w.._tom
#     p__.r.. n.._"Travel" w.._sara
#     p__.r.. n.._"Tech" w.._john
#
#     p__.d.. n.._"Tech" m.._"Tech Newsletter num 1"
#     p__.d.. n.._"Travel" m.._"Travel Newsletter num 1"
#
#     p__.un.. n.._"Tech" w.._john
#
#     p__.d.. n.._"Tech" m.._"Tech Newsletter num 2"
#     p__.d.. n.._"Travel" m.._"Travel Newsletter num 2"
#
#     p__.a_n..("Fashion")
#     p__.r.. n.._"Fashion" w.._tom
#     p__.r.. n.._"Fashion" w.._sara
#     p__.r.. n.._"Fashion" w.._john
#     p__.d.. n.._"Fashion" m.._"Fashion Newsletter num 1"
#     p__.un.. n.._"Fashion" w.._tom
#     p__.un.. n.._"Fashion" w.._sara
#     p__.d.. n.._"Fashion" m.._"Fashion Newsletter num 2")
#
#
# __ _______ __ ______
#     ?
