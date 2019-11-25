# Choose Generators for Large Datasets
# A list comprehension in Python works by loading the entire output list into memory. For small or
# even medium-sized lists, this is generally fine. If you want to sum the squares of the first one-thousand integers,
# then a list comprehension will solve this problem admirably:

sum([i * i for i in range(1000)])
# 332833500

# But what if you wanted to sum the squares of the first billion integers? If you tried then on your machine,
# then you may notice that your computer becomes non-responsive. That’s because Python is trying to create a list
# with one billion integers, which consumes more memory than your computer would like. Your computer may not have
# the resources it needs to generate an enormous list and store it in memory. If you try to do it anyway,
# then your machine could slow down or even crash.
# When the size of a list becomes problematic, it’s often helpful to use a generator instead of a list comprehension
# in Python. A generator doesn’t create a single, large data structure in memory, but instead returns an iterable.
# Your code can ask for the next value from the iterable as many times as necessary or until you’ve reached
# the end of your sequence, while only storing a single value at a time.
# If you were to sum the first billion squares with a generator, then your program will likely run for a while,
# but it shouldn’t cause your computer to freeze. The example below uses a generator:

sum(i * i for i in range(1000000000))
# 333333332833333333500000000

# You can tell this is a generator because the expression isn’t surrounded by brackets or curly braces.
# Optionally, generators can be surrounded by parentheses.
# The example above still requires a lot of work, but it performs the operations lazily. Because of lazy evaluation,
# values are only calculated when they’re explicitly requested. After the generator yields a value
# (for example, 567 * 567), it can add that value to the running sum, then discard that value and generate
# the next value (568 * 568). When the sum function requests the next value, the cycle starts over.
# This process keeps the memory footprint small.
# map() also operates lazily, meaning memory won’t be an issue if you choose to use it in this case:

sum(map(lambda i: i*i, range(1000000000)))
# 333333332833333333500000000

# It’s up to you whether you prefer the generator expression or map().
