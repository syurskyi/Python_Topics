# x = 'abc'
#
# ____ ____
# ____ t___
#
# _____ m__.d.. ____ m.., a..
#
#
# _____ ___ tick
#     print('Tick')
#     _____ ____.s.. 1
#     print('Tock')
#
#     loop = ____.g..
#     __ ?.i..
#         print('loop is still running')
#
#
# _____ ___ main
#     awaitable_obj = ____.g.. t.. t.. t...
#
#     ___ task __ ____.a..
#         print ? e.._'\n'
#
#     _____ ?
#
#
# __ _______ __ _______
#     loop = ____.g..
#     ___
#         ?.c...
#         ?.r..
#
#         print('coroutines have finished')
#     _______ K...
#         print('Manually closed application')
#     _______
#         ?.c..
#         print('loop is closed')
#         print(f'loop is closed = {loop.is_closed()}')
