
"""
TASK DESCRIPTION:

Write a function that can sum up numbers:

It should receive a list of n numbers.
If no argument is provided, return sum of numbers 1..100.
Look closely to the type of the function's default argument ...
"""
# ??? Co powinno sie wydarzyc, jesli przekazemy pusta liste ???

input = []

############################### KEY TAKEAWAYS #################################
###  1. Sum of empty list is 0.
###  2. None is a type of NoneType
###  3. "is" keyword is used to test if two variables refer to the same object.
###     It returns True if the two variable are referring to same object otherwise it returns False.
###     https://stackoverflow.com/questions/60975441/behaviour-of-is-keyword-in-python
###  4. Some objects in Python are cached for efficieny reasons
###     https://medium.com/@bdov_/https-medium-com-bdov-python-objects-part-ii-demystifying-cpython-shared-objects-fce1ec86dd63
###  5. Every object has value, type and memory location (id)

### https://realpython.com/null-in-python/

################################################################################




### ----------- My solution ---------------------------

def my_sum_numbers(numbers=None):
    result = 0
    # Dlaczego samo "if numbers:" nie dziala? Tzn. wtedy jak podamy pusta liste to nie spelnia warunku?
    # albo inaczej, przy przekazywaniu argumentu "if arg" dla pelnej tablicy dziala, dla pustej nie
    # "false" values include False, None, 0 and [] (an empty list), also empty sets, strings, dicts.
    # Bo if testuje wartosc boolowska danej zmiennej. Dlatego jak podamy pusta liste,
    # to bedzie traktowane jako bool false i
    # zostanie policzona suma 1-100.

    # None ma wartosc boolowska false, czyli albo moge sprawdzic wartosc albo moge sprawdzic typ obiektu
    # is None
    # == False
    #
    if numbers != None:
        for item in numbers:
            result += item
        return result
    for i in range(101):
        result += i
    return result

### ---------- PyBites original solution ---------------

def pyb_sum_numbers(numbers=None):
    if numbers is None:
        numbers = range(1, 101)
    return sum(numbers)

### Tutaj nie wiem, co chcialem osiagnac. Chyba chcialem sprawdzic alternatywny sposob, jak moznaby
### cos takiego napisac. Zamiast sprawdzac, co zostalo przekazane jako argument, mozna
### probowac obsluzyc wyjatek 'NoneType' object is not iterable

def sum_numbers_1(numbers=None):
    try:
        return sum(numbers)
    except TypeError:
        return sum(range(1,101))


print(pyb_sum_numbers("hello"))
