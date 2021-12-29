'''
Write a function that takes a sequence of items and returns the running average, so for example this:

running_mean([1, 2, 3])
returns:
[1, 1.5, 2]
You can assume all items are numeric so no type casting is needed.

Round the mean values to 2 decimals (4.33333 -> 4.33). See the tests for more info.

Bonus: use a function of itertools + make it a generator, but this is not required to get this working.
'''

list = [2, 6, 10, 8, 11, 10]
result = []

def running_mean(sequence):

    """
    Calculate the running mean of the sequence passed in,
    returns a sequence of same length with the averages.
    You can assume all items in sequence are numeric.
    """
    sum = 0
    for item in enumerate(list, start=1):
        sum += item[1]
        mean = sum / item[0]
        result.append(round(mean,2))

    for i in result:
        print(i)

running_mean(list)


