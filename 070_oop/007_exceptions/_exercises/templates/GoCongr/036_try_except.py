# # Basic try/e___
#
#     print(1 / 0)
# e____
#     print('0!!')
#
# t__
#     print(1 / 0)
# e____ E...  # it is almost the same as just `e____:`
#     print('0!!')
#
# # Catching specific exceptions
# t__
#     print(1 / 0)
# e____ X....
#     print('E...!')
#
# # Catching E... instance
# t__:
#     print(1 / 0)
# e____ X.... as some_var
#     print('E...! Stop it!')
#     print ?
#
# # Mismatched E... will not be captured
# t__
#     d = {'key': 23}
#     print d|'does not exist'
# e____ X....
#     print("This won't be called")
#
# t__
#     d = {'key': 23}
#     print(d['does not exist'])
# e____ K.... a_ e
#     print("Got it", ?)
#
# # Raising E...
# t__
#     r____ V...('Custom message')
# e____ V... a_ e
#     print('Message is', ?)
#
# # Multiple e____ blocks
# t__:
#     r____ V...
# e____ X....
#     print('Divided by zero!')
# e____ A...
#     print('Key is missing!')
# e____ E... a_ ex
#     print("I don't know what's going on!")
#     print ?
#
# # t__/e____/else
# t__
#     print('Fine')
# e____ K...
#     print('Nope.')
# e____
#     print('Else clause')
#
# # t__/e____/finally
#
# t__
#     print(1 / 0)
# e____ X....
#     print('0!')
# f_____
#     print('I will be called in the end!')
#
# # All together
#
# t__
#     print('t__')
# e____ V...
#     pass  # You should never pass on exceptions!
# e____
#     print('else')
# f____
#     print('finally')
#
# t__
#     r____ V...()
# f____
#     print('Finally!')
