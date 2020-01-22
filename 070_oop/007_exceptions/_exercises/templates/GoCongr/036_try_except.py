# # Basic try/e___
# ___
#     print(1 / 0)
# _____
#     print('0!!')
#
# ___
#     print(1 / 0)
# _____ E...  # it is almost the same as just `e____:`
#     print('0!!')
#
# # Catching specific exceptions
# ___
#     print(1 / 0)
# _____ X....
#     print('E...!')
#
# # Catching E... instance
# ___
#     print(1 / 0)
# _____ X.... as some_var
#     print('E...! Stop it!')
#     print ?
#
# # Mismatched E... will not be captured
# ___
#     d = {'key': 23}
#     print d|'does not exist'
# _____ X....
#     print("This won't be called")
#
# ___
#     d = {'key': 23}
#     print(d['does not exist'])
# _____ K.... a_ e
#     print("Got it", ?)
#
# # Raising E...
# ___
#     r____ V...('Custom message')
# _____ V... a_ e
#     print('Message is', ?)
#
# # Multiple e____ blocks
# ___
#     r____ V...
# _____ X....
#     print('Divided by zero!')
# _____ A...
#     print('Key is missing!')
# _____ E... __ ex
#     print("I don't know what's going on!")
#     print ?
#
# # t__/e____/else
# ___
#     print('Fine')
# _____ K...
#     print('Nope.')
# _____
#     print('Else clause')
#
# # t__/e____/finally
#
# ___
#     print(1 / 0)
# _____ X....
#     print('0!')
# f_____
#     print('I will be called in the end!')
#
# # All together
#
# ___
#     print('t__')
# _____ V...
#     pass  # You should never pass on exceptions!
# _____
#     print('else')
# f____
#     print('finally')
#
# ___
#     r____ V...()
# f____
#     print('Finally!')
