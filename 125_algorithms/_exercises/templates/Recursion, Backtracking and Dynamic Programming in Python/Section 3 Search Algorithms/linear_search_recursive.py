___ linear_search_recursive(container, item, index=0
    # base case for search miss (when item is not present in the container)
    __ index >= le_(container
        r_ -1

    # base case when we find the item
    __ container[index] == item:
        r_ index

    r_ linear_search_recursive(container, item, index + 1)


nums = [1, 4, 6, -4, 0, 100]
print(linear_search_recursive(nums, 0))