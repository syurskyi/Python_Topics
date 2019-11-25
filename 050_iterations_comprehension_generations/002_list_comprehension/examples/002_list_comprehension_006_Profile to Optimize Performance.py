# Profile to Optimize Performance
# So, which approach is faster? Should you use list comprehensions or one of their alternatives?
# Rather than adhere to a single rule that’s true in all cases, it’s more useful to ask yourself whether or not
# performance matters in your specific circumstance. If not, then it’s usually best to choose whatever approach
# leads to the cleanest code!
# If you’re in a scenario where performance is important, then it’s typically best to profile different approaches
# and listen to the data. timeit is a useful library for timing how long it takes chunks of code to run.
# You can use timeit to compare the runtime of map(), for loops, and list comprehensions:

import random
import timeit
TAX_RATE = .08
txns = [random.randrange(100) for _ in range(100000)]


def get_price(txn):
    return txn * (1 + TAX_RATE)


def get_prices_with_map():
    return list(map(get_price, txns))


def get_prices_with_comprehension():
    return [get_price(txn) for txn in txns]


def get_prices_with_loop():
    prices = []
    for txn in txns:
        prices.append(get_price(txn))
    return prices


timeit.timeit(get_prices_with_map, number=100)
# 2.0554370979998566

timeit.timeit(get_prices_with_comprehension, number=100)
# 2.3982384680002724

timeit.timeit(get_prices_with_loop, number=100)
# 3.0531821520007725

# Here, you define three methods that each use a different approach for creating a list. Then, you tell timeit to run
# each of those functions 100 times each. timeit returns the total time it took to run those 100 executions.
# As the code demonstrates, the biggest difference is between the loop-based approach and map(), with the loop taking
# 50% longer to execute. Whether or not this matters depends on the needs of your application.
# Conclusion
# In this tutorial, you learned how to use a list comprehension in Python to accomplish complex tasks without making
# your code overly complicated.
# Now you can:
#     Simplify loops and map() calls with declarative list comprehensions
#     Supercharge your comprehensions with conditional logic
#     Create set and dictionary comprehensions
#     Determine when code clarity or performance dictates an alternative approach
# Whenever you have to choose a list creation method, try multiple implementations and consider what’s easiest
# to read and understand in your specific scenario. If performance is important, then you can use profiling tools
# to give you actionable data instead of relying on hunches or guesses about what works the best.
# Remember that while Python list comprehensions get a lot of attention, your intuition and ability to use data
# when it counts will help you write clean code that serves the task at hand. This, ultimately, is the key to making
# your code Pythonic!
