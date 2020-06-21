#
# # The alternative is to send it directly to syslog. This is great for older operating systems that dont have systemd.
# # In an ideal world this should be simple, but sadly, Python requires a bit more elaborate configuration to be able
# # to send unicode log messages. Here is a sample implementation.
# #
# ______ l____
# ______ l____.ha...
# ______ o_
#
# c_ SyslogBOMFormatter(l____.F...
#     ___ format ____ record
#         result _ s__.f.. r..
#         r_ "ufeff" + ?
#
# handler _ l____.ha__.SLH_ '/dev/log'
# formatter _ S_BOMF_ l____.B..
# h__.sF__ f...
# root _ l____.gL_
# ?.sL_ __.e_.g... "LOGLEVEL", "INFO"
# ?.aH_ h__
#
# t__
#     e.. m..
# e____ E...
#     l____.e.. "Exception in main()"
#     e.. 1
