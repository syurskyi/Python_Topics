from itertools import  accumulate

def running_mean(sequence):
    """Calculate the running mean of the sequence passed in,
       returns a sequence of same length with the averages.
       You can assume all items in sequence are numeric."""
    return [ round(num/(index+1),2) for index, num in enumerate(accumulate(sequence))]