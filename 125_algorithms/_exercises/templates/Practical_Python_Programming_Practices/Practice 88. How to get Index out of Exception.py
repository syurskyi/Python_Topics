x _ [1,2,3,4,5,6,7,8,9]

print("t = terminate")

while T..:
    num _ input("Choose index to search: ")
    __ num __ 't':
        break
    try:
        num _ in.(num)
        print(x[num])
    except ValueError:
        print("Only integers are allowed!")
    except IndexError:
        print("Error! Number out of index", num)
