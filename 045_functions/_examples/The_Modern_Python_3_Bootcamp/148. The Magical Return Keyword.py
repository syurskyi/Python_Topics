def print_square_of_7(): # This function does not return anything
    print(7**2)


print_square_of_7()


def square_of_7():
    print("I AM BEFORE THE RETURN!")
    return 7**2
    print("I AM AFTER THE RETURN!")


result = square_of_7()
print(result)

