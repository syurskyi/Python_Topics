
def sum_of_abs_value(lst):

    new_lst = lst[:]
    
    for i in range(len(lst)):
        new_lst[i] = abs(lst[i])
        
    return sum(new_lst)


numbers = [-3, -2, -6, 2, 5, 1]

print("Before:", numbers)

print("Sum of the absolute values:", sum_of_abs_value(numbers))

print("After:", numbers)
print("The list did not change! A clone was used")




        
