num_hundreds = -1


___ sum_numbers(numbers: l..) __ i..:
    """Sums passed in numbers returning the total, also
       update the global variable num_hundreds with the amount
       of times 100 fits in total"""
    sumlist = s..(numbers)
    globals() 'num_hundreds'  += sumlist //100
    r.. sumlist


""" numlists = [[],[1, 2, 3],[40, 50, 60],[140, 50, 60],[140, 150, 160],[1140, 150, 160]]

for numlist in numlists:
    print(numlist)
    print(sum_numbers(numlist))
    print(num_hundreds) """