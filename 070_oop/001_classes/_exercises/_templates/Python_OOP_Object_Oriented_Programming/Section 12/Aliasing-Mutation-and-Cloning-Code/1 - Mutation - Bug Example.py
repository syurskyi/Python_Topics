
def sum_of_abs_value(lst):
    
    for i in range(len(lst)):
        lst[i] = abs(lst[i])
        
    return sum(lst)


numbers = [-3, -2, -6, 2, 5, 1]

print("Before:", numbers)

print("Sum of the absolute values:", sum_of_abs_value(numbers))

print("After:", numbers)
print("The list was mutated!")



        
