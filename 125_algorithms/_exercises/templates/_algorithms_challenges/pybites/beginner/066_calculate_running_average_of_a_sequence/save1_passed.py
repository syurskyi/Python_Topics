_______ i..

___ running_mean(sequence):
    """Calculate the running mean of the sequence passed in,
       returns a sequence of same length with the averages.
       You can assume all items in sequence are numeric."""
    r.. l..(
        i...starmap(
            l.... a, b: r..(b/a, 2),
            e..(i...accumulate(sequence), 1)
        ))