def checkdupsorting(myarray):
	myarray.sort()
	print(myarray)
	for i in range(0, len(myarray) - 1):
		#print "in for loop:", myarray
		# #print "comparing", myarray[i],"and",myarray[i + 1]
		if(myarray[i] == myarray[i + 1]):
			print("Duplicates present:", myarray[i])
			return
			print("There are No duplicates present in the given array.")

myarray = [3,4,5,6,7,8,7]
checkdupsorting(myarray)

# #####################################################################################################################

def getfirstnonrepeated(myarray):
    print("Given array:", myarray)
    tab = {}  # hash
    # #print "tab created:", tab
    for ele in myarray.lower():
        if ele in tab:
            tab[ele] += 1
        elif ele != " ":
            tab[ele] = 1
        else:
            tab[ele] = 0
    # print "in loop:",tab,"for","'",ele,"'","in",myarray

    for ele in myarray.lower():
        if tab[ele] == 1:
            print("the first non repeated character is: %s" % (ele))
            return ele

    return


getfirstnonrepeated("abccdef")

# #####################################################################################################################

from nose.tools import assert_equal


class AnagramTest(object):

    def test(self, sol):
        assert_equal(sol('go go go', 'gggooo'), True)
        assert_equal(sol('abc', 'cba'), True)
        assert_equal(sol('hi man', 'hi     man'), True)
        assert_equal(sol('aabbcc', 'aabbc'), False)
        assert_equal(sol('123', '1 2'), False)
        print("ALL TEST CASES PASSED")


# Run Tests
t = AnagramTest()
t.test(anagram)

# %%
t.test(anagram2)

# %%
'''
# Good Job!
'''

# #####################################################################################################################

def balance_check(s):
    # Check is even number of brackets
    if len(s) % 2 != 0:
        return False

    # Set of opening brackets
    opening = set('([{')

    # Matching Pairs
    matches = set([('(', ')'), ('[', ']'), ('{', '}')])

    # Use a list as a "Stack"
    stack = []

    # Check every parenthesis in string
    for paren in s:

        # If its an opening, append it to list
        if paren in opening:
            stack.append(paren)

        else:

            # Check that there are parentheses in Stack
            if len(stack) == 0:
                return False

            # Check the last open parenthesis
            last_open = stack.pop()

            # Check if it has a closing match
            if (last_open, paren) not in matches:
                return False

    return len(stack) == 0


balance_check('[]')
# True

balance_check('[](){([[[]]])}')
# True

balance_check('()(){]}')
# False

# Test Your Solution
"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""
from nose.tools import assert_equal


class TestBalanceCheck(object):

    def test(self, sol):
        assert_equal(sol('[](){([[[]]])}('), False)
        assert_equal(sol('[{{{(())}}}]((()))'), True)
        assert_equal(sol('[[[]])]'), False)
        print 'ALL TEST CASES PASSED'


# Run Tests

t = TestBalanceCheck()
t.test(balance_check)

# #####################################################################################################################

# tail recursion
def tail(n):
    # base case
    if n == 0:
        return

    # do some operation before the recursive call
    print(n)

    # recursive call
    tail(n - 1)


def head(n):
    # base case
    if n == 0:
        return

    # recursive call
    head(n - 1)

    # do some operation after the recursive call
    print(n)


if __name__ == "__main__":
    print("Tail recursion:\n")
    tail(5)
    print("\nHead recursion:\n")
    head(5)