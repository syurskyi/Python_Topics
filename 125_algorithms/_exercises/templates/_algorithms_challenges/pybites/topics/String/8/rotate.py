___ rotate(string, n):
    __ n > l..(string) o. n < (l..(string)*-1):
        n = n % l..(string)
    __ n __ 0:
        r.. string
    ____ n > 0:
        r.. string[n:l..(string)] + string[0:n]
    ____ n < 0:
        r.. string[n:] + string[0:n]