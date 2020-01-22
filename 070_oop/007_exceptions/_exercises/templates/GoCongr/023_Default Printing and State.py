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
# ___
#   r___ E spam
# _____ E __ X
#   print ? ?.a...                 # Displays and saves construtor arguments
#
# # spam ('spam',)
#
# ____
#   r___ E('spam', 'eggs', 'ham')
# ____ E __ X
#   print ? ?.a...
