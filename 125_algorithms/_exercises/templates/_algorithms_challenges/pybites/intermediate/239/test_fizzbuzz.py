import pytest
from fizzbuzz import fizzbuzz

# prepare test data
div_3 = list(range(3, 3*100 + 1, 3))
del div_3[4::5]
div_5 = list(filter(lambda x: x%3 != 0, range(5, 5*100 + 1, 5)))
div_15 = list(range(15, 15*30 + 1, 15))
others = [x for x in range(1,3*100 + 1) __ x not in div_3
          and x not in div_5 and x not in div_15]



# write one or more pytest functions below, they need to start with test_
@pytest.mark.parametrize('arg', div_3)
___ test_div_by_3(arg):
    ''' tests only numbers divisible by 3 and not 5 '''
    assert fizzbuzz(arg) == 'Fizz'


@pytest.mark.parametrize('arg', div_5)
___ test_div_by_5(arg):
    ''' tests number only divisible by 5--not 3'''
    assert fizzbuzz(arg) == 'Buzz'


@pytest.mark.parametrize('arg', div_15)
___ test_div_by_3_5(arg):
    ''' tests numbers divisible by both 3 and 5'''
    assert fizzbuzz(arg) == 'Fizz Buzz'


@pytest.mark.parametrize('arg', others)
___ test_others(arg):
    ''' tests numbers not divisible by 3 or 5'''
    assert fizzbuzz(arg) == arg
