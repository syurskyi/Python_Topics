from collections import OrderedDict
"""
You are given a list of integers. Write code to find the majority and minorty numbers in that list.
Definition: a majority number is the one appearing most frequently, a minority number appears least frequently.
Here is a simple example how it should work:

>>> numbers = [1, 2, 2, 3, 2, 3]
>>> major_n_minor(numbers)
(2, 1)
Note - you can assume that there will be only one of each.
Hint: any built-in library that supports convenient and rapid tallies?
"""

def major_n_minor(numbers):
    """
    Input: an array with integer numbers
    Output: the majority and minority number
    """
    # https://stackoverflow.com/questions/55125342/usage-of-dict-value-and-dict-key-in-python3
    # https://stackoverflow.com/questions/52135345/is-some-dict-items-an-iterator-in-python
    # https://stackoverflow.com/questions/21062781/shortest-way-to-get-first-item-of-ordereddict-in-python-3
    # https://stackoverflow.com/questions/49159238/why-does-the-kwargs-mapping-compare-equal-with-a-differently-ordered-ordereddi
    # https://stackoverflow.com/questions/39980323/are-dictionaries-ordered-in-python-3-6
    # https://stackoverflow.com/questions/50872498/will-ordereddict-become-redundant-in-python-3-7/
    test = {'oranges': 5,
            'apples': 3,
            'peach': 1}
    #print(type((test.items())))
    #print(type(test.values()))
    #print(type(test.keys()))
    # Q: Co to tak naprawde znaczy OrderedDict? Ordered wg klucza czy wartosci?
    # A: Zadne z powyzszego. Ordered znaczy, ze zachowana jest kolejnosc podczas wstawiania.

    d = OrderedDict()
    for num in numbers:
        try:
            d[num] += 1
        except:
            d[num] = 1
    #print(d)
    dict = {}
    for num in numbers:
        try:
            dict[num] += 1
        except:
            dict[num] = 1
    sort = sorted(dict.items(), key=lambda x: x[1] )
    return sort[-1][0], sort[0][0]
    # difference between for i in d:
    # for i in d.items(): ?
    # return (next((iter(reversed(sor.items()))))[0], next(iter(sor.items()))[0] )
print(major_n_minor([0,0,0,1,2,2]))