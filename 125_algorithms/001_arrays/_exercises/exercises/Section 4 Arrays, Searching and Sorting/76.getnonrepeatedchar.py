def getrepeatedelement(A):
    print("given array:", A)
    tab = {}

    for element in A.lower():
        if element in tab:
            tab[element] += 1
            print("the first repeated element is: %s" % element)
            return element
        elif element != " ":
            tab[element] = 1
        else:
            tab[element] = 0
    return

getrepeatedelement("abcdefd")