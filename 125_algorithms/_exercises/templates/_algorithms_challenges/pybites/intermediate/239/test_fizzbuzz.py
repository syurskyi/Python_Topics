_______ p__
____ fizzbuzz _______ fizzbuzz

# prepare test data
div_3 = l..(r..(3, 3*100 + 1, 3))
del div_3[4::5]
div_5 = l..(filter(l.... x: x%3 != 0, r..(5, 5*100 + 1, 5)))
div_15 = l..(r..(15, 15*30 + 1, 15))
others = [x ___ x __ r..(1,3*100 + 1) __ x n.. __ div_3
          a.. x n.. __ div_5 a.. x n.. __ div_15]



# write one or more pytest functions below, they need to start with test_
?p__.m__.p.('arg', div_3)
___ test_div_by_3(arg):
    ''' tests only numbers divisible by 3 and not 5 '''
    ... fizzbuzz(arg) __ 'Fizz'


?p__.m__.p.('arg', div_5)
___ test_div_by_5(arg):
    ''' tests number only divisible by 5--not 3'''
    ... fizzbuzz(arg) __ 'Buzz'


?p__.m__.p.('arg', div_15)
___ test_div_by_3_5(arg):
    ''' tests numbers divisible by both 3 and 5'''
    ... fizzbuzz(arg) __ 'Fizz Buzz'


?p__.m__.p.('arg', others)
___ test_others(arg):
    ''' tests numbers not divisible by 3 or 5'''
    ... fizzbuzz(arg) __ arg
