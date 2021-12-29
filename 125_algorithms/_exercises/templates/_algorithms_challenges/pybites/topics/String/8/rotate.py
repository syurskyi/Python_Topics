___ rotate(string, n):
    __ n > len(string) or n < (len(string)*-1):
        n = n % len(string)
    __ n == 0:
        return string
    elif n > 0:
        return string[n:len(string)] + string[0:n]
    elif n < 0:
        return string[n:] + string[0:n]