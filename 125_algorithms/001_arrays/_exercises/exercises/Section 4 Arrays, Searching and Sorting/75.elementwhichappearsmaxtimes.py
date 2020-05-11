def elementwhichappearsmaxtimes(myarray):
    myarray.sort()
    print("sorted array:", myarray)
    j = 0
    count = max = 1
    element = myarray[0]
    for i in range(1, len(myarray)):
        if (myarray[i] == element):
            count += 1
            if count > max:
                max = count
                maxRepeatedElement = element
        else:
            count = 1
            element = myarray[i]
    print(myarray, "repeated for ", myarray)

myarray = [4, 3, 1, 4, 3, 4, 3, 4, 4]
elementwhichappearsmaxtimes(myarray)
