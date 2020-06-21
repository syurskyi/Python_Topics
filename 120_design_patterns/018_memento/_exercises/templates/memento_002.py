# # TODO finish it
# ______ co..
#
#
# ___ Memento obj deep_F..
#     state _ co__.co__ co__.d_c_||bo.. de..|||?. -d
#     ___ R..
#         ?. -d.c..
#         ?. -d.up.. ?
#     r_ R...
#
# c_ Transaction
#     """A transaction guard. This is realy just syntactic suggar arount a memento
#     closure."""
#     deep _ F..
#     ___ - $targets
#         ?  ?
#         C...
#     ___ C...
#         states _ |M.. t.. de.. ___ target __ t..
#     ___ R...
#         ___ state __ ?
#             ?
#
# c_ transactional o..
#     """Adds transactional semantics to methods. Methods decorated with
#     @transactional will rollback to entry state upon exceptions."""
#     ___ - method
#         ?  ?
#     ___ -g obj T
#         ___ transaction $  $$
#             state _ M.. ?
#             ___
#                 r_ m.. ? $ $$
#             ______
#                 s..
#                 r_
#         r_ ?
#
# __ _______ __ ______
#
#    c_ NumObj o..
#       ___ - value
#          ?  ?
#       ___ -r
#          r_ '<%s: %r>'  -c . -n ?
#       ___ I...
#          ? +_ 1
#       ?t..
#       ___ DoStuff
#          value _ '1111' # <- invalid value
#          I...    # <- will fail and rollback
#
#    print
#    n _ N.. -1
#    print ?
#    t _ T.. ?
#    ___
#       ___ i __ ra.. 3
#          n.I..
#          print ?
#       t.C..
#       print '-- commited'
#       ___ i __ ra.. 3
#          n.I..
#          print ?
#       ?.v.. +_ 'x' # will fail
#       print ?
#    ________
#       t.R..
#       print '-- rolled back'
#    print ?
#    print '-- now doing stuff ...'
#    ___
#       n.DS..
#    _______
#       print '-> doing stuff failed!'
#       ______ tr...
#       tr____.p_e... 0
#       pass
#    print ?
