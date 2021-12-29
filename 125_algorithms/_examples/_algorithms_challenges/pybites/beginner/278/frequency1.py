from collections import Counter

def major_n_minor(numbers):
    counts = Counter(numbers)
    # you code ...
    major=max(counts, key=counts.get)
    minor=min(counts, key=counts.get)
    return major, minor


print(major_n_minor([1, 3, 5, 7, 8, 8, 9, 9, 3, 5, 8, 7]))

#[1, 3, 5, 7, 8, 8, 9, 9, 3, 5, 8, 7]