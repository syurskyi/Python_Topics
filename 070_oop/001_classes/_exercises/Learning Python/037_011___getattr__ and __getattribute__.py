# ___ -g ____ name        # On undefined attribute fetch [obj.name]
#     p___
#
#
# ___ -g ____ name   # On all attribute fetch [obj.name]
#     p___
#
# ___ -s ____ name value # On all attribute assignment [obj.name=value]
#     p___
#
#
# ___ -d ____ name        # On all attribute deletion [del obj.name]
#     p___
#
#
# c_ Catcher
#     ___ -g ____ name
#         print 'Get:' n..
#
#     ___ -s ____ name value
#         print('Set:', n.. v..
#
#
# X = ?
# ?.job                               # Prints "Get: job"
# ?.pay                               # Prints "Get: pay"
# ?.pay = 99                          # Prints "Set: pay 99"
#
#
# c_ Wrapper
#     ___ - ____ object
#         ____.wrapped = o..                    # Save object
#
#     ___ -g ____ attrname
#         print('Trace:', a..                # Trace fetch
#         r_ g... ____.w... a..   # Delegate fetch
#
#     ___ -g ____ name
#         x = ____.other                                # LOOPS!
#
#     ___ -g  ____ name
#         x = ob___. -g ____ 'other'    # Force higher to avoid me
#
#     ___ -s ____ name value
#         ____.other _ v...                            # LOOPS!
#
#     ___ -s ____ name, value
#         ____. -d 'other' _ v...               # Use atttr dict to avoid me
#
#     ___ -s ____ name value
#         ob__. -s ____ 'other' v..      # Force higher to avoid me
#
#     ___ -g ____ name
#         x _ ____. -d 'other'                    # LOOPS!
#
