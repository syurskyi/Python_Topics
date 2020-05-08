# Write function to compute the value 3x+1
# Using lambda expression to create short throwaway simple one time use functions
# Commonly used to sort and filter data 
# https://www.youtube.com/watch?v=25ovCm9jKfA
# Anonymous functions == Lambda expressions

def f(x):
    return 3*x+1

lambda x: 3*x+1

g = lambda x: 3*x+1 # g(2) = 7

# Example, combine first and last name
full_name = lambda fn, ln: fn.strip().title() + " " + ln.strip().title()
full_name("leonhard", "EULER") # 'Leonhard Euler'

# Sort list of sci fi authors by last name
scifi_authors = ["isaac Asimov", "Ray Bradbury", "Robert Heinlein", "Arthurs C. Clarke", "Frank Herber", "Orson Scott Card", "Douglas Adams", "H. G. Wells", "Leigh Brackett"]
scifi_authors.sort(key=lambda name: name.split(" ")[-1].lower())
print(scifi_authors)

# Quadratic function
def build_quadratic_function(a, b, c):
    """ Returns the function f(x) = ax^2 + bx + c"""
    return lambda x: a*x**2 + b*x + c

f = build_quadratic_function(2, 3, -5)
print(f(0), f(1), f(2))

# Call build and output result in one line
print(build_quadratic_function(3, 0, 1)(2))