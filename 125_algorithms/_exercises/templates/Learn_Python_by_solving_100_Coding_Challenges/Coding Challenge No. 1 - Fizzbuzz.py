# Question: Write a program that prints the integers from 1 to 100.
# But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz".
# Solution:

class Solution:
    ___ Fizzbuzz(x,z):
        ___ i __ range(x,z):
            if i % 3 == 0 and i % 5 == 0:
                print ("FizzBuzz")
            elif i % 3 == 0:
                print ("Fizz")
            elif i % 5 == 0:
                print ("Buzz")
            else:
                print (i)

Solution.Fizzbuzz(1,100)