def firstrepeatedeleinalistofrepeatednumbersusinghash(myarray):
    print("Given array:", myarray)
    tab = {}   # dict # hash
    # print "Created the tab:",tab
    max = 0
    for ele in myarray:
        if ele in tab and tab[ele] == 1:
            tab[ele] = -2
        elif ele in tab and tab[ele] < 0:
            tab[ele] -= 1
        elif ele != " ":
            tab[ele] = 1
        # print "newly adding ele",ele,"to tab", tab
        # print "in loop: tab",tab,"for ele'",ele,"' in array ",myarray
        else:
            tab[ele] = 0

    for ele in myarray:
        if tab[ele] < max:
            max = tab[ele]
            maxRepeatedElement = ele


    print(maxRepeatedElement, "repeated for ", abs(max), " times")

myarray = [3, 10, 1, 1, 10, 1, 10, 5, 5]
firstrepeatedeleinalistofrepeatednumbersusinghash(myarray)
