# # Default Printing and State
# r___ I....                    # Same as IndexError(): no arguments
#
# r___ I....spam          # Constructor argument attached, printed
#
# I = I.... spam            # Available in object attribute
# I.a..
# # ('spam',)
# print(I)
#
# class E E... p..
#
# r___ E
#
# r___ E spam
#
# I = E spam
# I.a..
# print(I)
#
# t__
#   r___ E spam
# e____ E a_ X
#   print ? ?.a...                 # Displays and saves construtor arguments
#
# # spam ('spam',)
#
# t___
#   r___ E('spam', 'eggs', 'ham')
# e___ E a_ X
#   print ? ?.a...
