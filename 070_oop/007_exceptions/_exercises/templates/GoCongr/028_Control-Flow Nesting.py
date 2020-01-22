# # Control-Flow Nesting
# ___ action2
#     print(1 + [])            # Generate TypeError
#
# ___ action1
#     ___
#         _2
#     _____ T..        # Most recent matching try
#         print('inner tty')
#
# ___
#     _1
# _____ T...           # Here, only if action1 re-raises
#     print('outer try')
