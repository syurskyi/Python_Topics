print('%(qty)d more %(food)s' % {'qty': 1, 'food': 'spam'})


# Template with substitution targets
reply = """
Greetings...
Hello %(name)s!
Your age is %(age)s
"""
values = {'name': 'Bob', 'age': 40} # Build up values to substitute
print(reply % values) # Perform substitutions


food = 'spam'
qty = 10
vars()

print('%(qty)d more %(food)s' % vars())  # Variables are keys in vars()
