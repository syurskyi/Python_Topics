# Sum Even Values Solution
#
#     I define a function called sum_even_values  which accepts any number of arguments, thanks to *args
#     I grab the even numbers using the generator expression (arg for arg in args if arg % 2 == 0)
#     (could also use a list comp)
#     I pass the even numbers I extracted into sum()  and return the value
#     The default start value of sum()
#     is 0, so I don't have to do anything special to get it to return 0 if there are no even numbers!


___ sum_even_values(*args):
    r_ sum(arg ___ arg __ args if arg % 2 == 0)