def tail(filepath, n):
    """Similate Unix' tail -n, read in filepath, parse it into a list,
       strip newlines and return a list of the last n lines"""
    return [lines.decode('utf8') for lines in filepath.splitlines()[-n:]]