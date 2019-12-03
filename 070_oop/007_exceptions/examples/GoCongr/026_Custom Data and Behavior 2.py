# Custom Data and Behavior 2
class FormatError(Exception): pass             # Inherited constructor

 def parser():
     raise FormatError(42, 'spam.txt')          # No keywords allowed!

try:
    parser()
except FormatError as X:
    print('Error at:', X.args[0], X.args[1])   # Not specific to this app
