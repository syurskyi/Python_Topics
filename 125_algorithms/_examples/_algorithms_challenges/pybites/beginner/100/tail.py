def tail(filepath, n):
    """Similate Unix' tail -n, read in filepath, parse it into a list,
       strip newlines and return a list of the last n lines"""
    with open(filepath) as f:
        lines = f.read().splitlines()
    return lines[-n:]


print(tail("test.txt", 1))