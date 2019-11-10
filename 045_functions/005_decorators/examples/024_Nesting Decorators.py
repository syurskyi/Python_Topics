from decorators import debug, do_twice

@debug
@do_twice
def greet(name):
    print(f"Hello {name}")

greet("Eva")
# Calling greet('Eva')
# Hello Eva
# Hello Eva
# 'greet' returned None