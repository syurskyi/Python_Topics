___ tail(filepath, n):
    """Similate Unix' tail -n, read in filepath, parse it into a list,
       strip newlines and return a list of the last n lines"""
    file = open(filepath, "r")
    data = file.read()
    return [lines for lines in data.splitlines()[-n:]]