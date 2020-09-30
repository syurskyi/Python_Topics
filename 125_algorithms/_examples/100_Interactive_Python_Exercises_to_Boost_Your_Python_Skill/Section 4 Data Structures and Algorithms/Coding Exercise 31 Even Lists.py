def foo(mylist):
    if len(mylist) > 0 and len(mylist) % 2 != 0:
        middle_index = int(len(mylist)/2)
        return mylist[middle_index]
    else:
        return "Bad List"