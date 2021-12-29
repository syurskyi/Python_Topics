___ tail(filepath, n):
    """Similate Unix' tail -n, read in filepath, parse it into a list,
       strip newlines and return a list of the last n lines"""
    filepath = open('filepath','r') 
    r.. [lines.decode('utf8') ___ lines __ filepath.splitlines()[-n:]]