_______ itertools

___ running_mean(sequence):
    """Calculate the running mean of the sequence passed in,
       returns a sequence of same length with the averages.
       You can assume all items in sequence are numeric."""
    r.. l..(
        itertools.starmap(
            l.... a, b: round(b/a, 2),
            enumerate(itertools.accumulate(sequence), 1)
        ))