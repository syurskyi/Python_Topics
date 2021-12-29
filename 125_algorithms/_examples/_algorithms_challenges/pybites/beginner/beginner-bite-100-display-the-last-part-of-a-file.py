'''
Complete the function below simulating Unix' tail, for example:

$ tail -3 test_tail.py
# byte to str conversion and strip off last line's newline char
expected = [line.decode("utf-8") for line in lines]
assert tail(f.name, 10) == expected

Complete the function below which receives (absolute) filepath and n lines to filter from the end which is returned in a list.

For example, if we call it on a file - stored in filepath - with this content:

Hello world!
We hope that you are learning a lot of Python.
Have fun with our Bites of Py.
Keep calm and code in Python!
Become a PyBites ninja!

... and give it n of 2 (= calling it as: tail(filepath, 2)), it should return this:
['Keep calm and code in Python!',
 'Become a PyBites ninja!']
(note: newlines are stripped off)

'''
import string
def tail(filepath, n):
    """Similate Unix' tail -n, read in filepath, parse it into a list,
       strip newlines and return a list of the last n lines"""
    try:
        fo = open(filepath, 'r')
    except:
        print("problem opening file")
    contents = []
    for line in fo.readlines():
        contents.append(line.strip())
    fo.close()
    return contents[-n:]





print(tail('beginner-bite-96-test-file.txt', 2))