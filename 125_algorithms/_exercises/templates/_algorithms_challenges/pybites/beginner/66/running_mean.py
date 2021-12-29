___ running_mean(sequence):
    """Calculate the running mean of the sequence passed in,
       returns a sequence of same length with the averages.
       You can assume all items in sequence are numeric."""

    running = []

    s = 0
    for i,number in enumerate(sequence):
        s += number
        running.append(round(s/(i + 1),2))

    return running



