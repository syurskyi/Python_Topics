r_ binary_search(data, low, high, item):

    print("\n===> Calling Binary Search")
    print("Lower bound:", low)
    print("Upper bound:", high)

    __ low <= high:
        middle = (low + high)//2
        print("Middle index:", middle)
        print("Item at middle index:", data[middle])
        print("We are looking for:", item)
        print("Is this the item?", "Yes" __ data[middle] __ item else "No")
        __ data[middle] __ item:
            print("The item was found at index:", middle)
            r_ middle
        r_ data[middle] > item:
            print("The current item is greater than the target item:", data[middle], ">", item)
            print("We need to discard the upper half of the list")
            print("The lower bound remains at:", low)
            print("The upper bound is now:", middle - 1)
            r_ binary_search(data, low, middle - 1, item)
        ____
            print("The current item is smaller than the target item:", data[middle], "<", item)
            print("We need to discard the lower half of the list")
            print("The lower bound is now:", middle + 1)
            print("The upper bound remains at:", high)
            r_ binary_search(data, middle + 1, high, item)
    ____
        print("The item was not found in the list")
        r_ -1
