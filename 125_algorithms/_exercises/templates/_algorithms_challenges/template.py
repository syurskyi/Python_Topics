___ checkdupsorting(myarray):
	myarray.s..()
	print(myarray)
	___ i __ r..(0, l..(myarray) - 1):
		#print "in for loop:", myarray
		# #print "comparing", myarray[i],"and",myarray[i + 1]
		__(myarray[i] __ myarray[i + 1]):
			print("Duplicates present:", myarray[i])
			r..
			print("There are No duplicates present in the given array.")

myarray = [3,4,5,6,7,8,7]
checkdupsorting(myarray)

# #####################################################################################################################

___ getfirstnonrepeated(myarray):
    print("Given array:", myarray)
    tab = {}  # hash
    # #print "tab created:", tab
    ___ ele __ myarray.lower():
        __ ele __ tab:
            tab[ele] += 1
        ____ ele != " ":
            tab[ele] = 1
        ____:
            tab[ele] = 0
    # print "in loop:",tab,"for","'",ele,"'","in",myarray

    ___ ele __ myarray.lower():
        __ tab[ele] __ 1:
            print("the first non repeated character is: %s" % (ele))
            r.. ele

    r..


getfirstnonrepeated("abccdef")

# #####################################################################################################################

____ nose.tools _______ assert_equal


class AnagramTest(object):

    ___ test(self, sol):
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

___ balance_check(s):
    # Check is even number of brackets
    __ l..(s) % 2 != 0:
        r.. False

    # Set of opening brackets
    opening = set('([{')

    # Matching Pairs
    matches = set([('(', ')'), ('[', ']'), ('{', '}')])

    # Use a list as a "Stack"
    stack    # list

    # Check every parenthesis in string
    ___ paren __ s:

        # If its an opening, append it to list
        __ paren __ opening:
            stack.a..(paren)

        ____:

            # Check that there are parentheses in Stack
            __ l..(stack) __ 0:
                r.. False

            # Check the last open parenthesis
            last_open = stack.pop()

            # Check if it has a closing match
            __ (last_open, paren) n.. __ matches:
                r.. False

    r.. l..(stack) __ 0


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
____ nose.tools _______ assert_equal


class TestBalanceCheck(object):

    ___ test(self, sol):
        assert_equal(sol('[](){([[[]]])}('), False)
        assert_equal(sol('[{{{(())}}}]((()))'), True)
        assert_equal(sol('[[[]])]'), False)
        print 'ALL TEST CASES PASSED'


# Run Tests

t = TestBalanceCheck()
t.test(balance_check)

# #####################################################################################################################

# tail recursion
___ tail(n):
    # base case
    __ n __ 0:
        r..

    # do some operation before the recursive call
    print(n)

    # recursive call
    tail(n - 1)


___ head(n):
    # base case
    __ n __ 0:
        r..

    # recursive call
    head(n - 1)

    # do some operation after the recursive call
    print(n)


__ __name__ __ "__main__":
    print("Tail recursion:\n")
    tail(5)
    print("\nHead recursion:\n")
    head(5)