'''
A small but interesting Bite: given a string with leading indent spacing, calculate the amount of space characters:

'string  ' -> 0 (we only care about leading spacing)
'  string' -> 2
'    string' -> 4
etc...
This can be done in many ways so once done we encourage you to go into the Bite forum (Discussion tab that appears upon
solving the Bite) to discuss your solution with fellow Pythonistas ... Have fun!


'''


def count_indents_v1(text):
    """Takes a string and counts leading white spaces, return int count"""
    n = 0
    for c in text:
       if c is ' ':
           n += 1
       else:
           break

    return n

def count_indents_v2(string text):

v1 = count_indents_v1("   test  ")
print(f"v1: {v1}")


