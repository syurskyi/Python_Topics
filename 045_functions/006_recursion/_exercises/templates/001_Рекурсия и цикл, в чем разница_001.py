# for
def getTotal(n):
    total = 0
    for number in list(range(n+1)):
        print(number)
        total = total + number
    return total

print(getTotal(5))

# recursion

def getTotal(n, total):
    print(n)
    if n == 0:  # base condition
        return total
    else:
        return getTotal(n-1, (total+(n)))

print(getTotal(5, 0))
