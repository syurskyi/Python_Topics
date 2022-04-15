# ____ c.. _______ n..
# ____ o.. _______ a..
#
# Tweet n..('Tweet', 'text polarity')
#
# # polarity < 0 = negative, > 0 = positive
# # long strings and pep8: you can wrap strings in () to reduce line length
# tweets
#     ? t.._ "It's shocking that the vast majority of online banking "
#                 "systems have critical vulnerabilities leaving customer "
#                 "accounts unprotected."),
#           polarity=-0.3333333333333333),
#     ? t.._ "The most unbelievable aspect of the Star Trek universe "
#                 "is that every ship they meet has compatible video "
#                 "conferencing facilities."),
#           polarity=0.125),
#     ? t.._ "Excellent set of tips for managing a PostgreSQL cluster "
#                 "in production."),
#           polarity=1.0),
#     ? t.._ "This tutorial has a great line-by-line breakdown of how "
#                 "to train a pong RL agent in PyTorch."),
#           polarity=0.8),
#     Tweet(text="This is some masterful reporting by ... It's also an "
#                "infuriating story. ... is trying to erase debt by preying "
#                "on the city’s residents. The poorest get hit the worst. "
#                "It’s shameful.",
#           polarity=-0.19999999999999998),
#
#
#
# ___ filter_tweets_on_polarity tweets keep_positive=T..
#     """Filter the tweets by polarity score, receives keep_positive bool which
#        determines what to keep. Returns a list of filtered tweets."""
#     positive    # list
#     negative    # list
#     ___ tweet __ ?
#         __ ?.p.. > 0
#             p__.a.. ?
#         ____
#             n__.a.. ?
#     r.. p.. __ ? __ T.. ____ n..
#
# ___ order_tweets_by_polarity tweets positive_highest_T..
#     """Sort the tweets by polarity, receives positive_highest which determines
#        the order. Returns a list of ordered tweets."""
#     __ ? __ T..
#         r.. s.. ? k.._a.. 'polarity' r.._T..
#     ____
#         r.. s.. ? k.._a.. 'polarity' r.._F..