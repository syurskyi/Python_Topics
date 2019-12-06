# # Control-Flow Nesting
# ___ action2
#     print(1 + [])            # Generate TypeError
#
# ___ action1
#     t__:
#         _2
#     e____ T..        # Most recent matching try
#         print('inner tty')
#
# t__
#     _1
# e____ T...           # Here, only if action1 re-raises
#     print('outer try')
