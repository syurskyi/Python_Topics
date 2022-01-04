___ tail(filepath, n):
    """Similate Unix' tail -n, read in filepath, parse it into a list,
       strip newlines and return a list of the last n lines"""
    with open(filepath) __ f:
        content = f.read().splitlines(keepends=F..)
        r.. content[-n:]