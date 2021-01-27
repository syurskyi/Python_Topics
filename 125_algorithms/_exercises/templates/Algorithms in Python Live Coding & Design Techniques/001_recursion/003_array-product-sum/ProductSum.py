
___ product_sum(li, depth
    sum_is = 0

    for ele in li:
        __ isinstance(ele, list
            sum_is += product_sum(ele, depth+1)
        ____
            sum_is += ele
    return sum_is * depth


arr = [1, 2, [2,3], 6, [[2,3], 1], 7]
print(product_sum(arr, 1))