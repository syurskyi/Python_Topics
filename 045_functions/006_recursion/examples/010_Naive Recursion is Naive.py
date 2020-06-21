def fibonacci_recursive(n):
    print("Calculating F", "(", n, ")", sep="", end=", ")

    # Base case
    if n == 0:
        return 0
    elif n == 1:
        return 1

    # Recursive case
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

print(fibonacci_recursive(5))
# Calculating F(5), Calculating F(4), Calculating F(3), Calculating F(2), Calculating F(1),
# Calculating F(0), Calculating F(1), Calculating F(2), Calculating F(1), Calculating F(0),
# Calculating F(3), Calculating F(2), Calculating F(1), Calculating F(0), Calculating F(1),

# 5