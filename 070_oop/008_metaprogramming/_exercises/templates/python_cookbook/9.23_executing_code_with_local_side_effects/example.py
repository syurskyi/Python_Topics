def test():
    a = 13
    loc = locals()
    exec('b = a + 1')
    b = loc['b']
    print(b)      # --> 14

def test1():
    x = 0
    exec('x += 1')
    print(x)      # --> 0

def test2():
    x = 0
    loc = locals()
    print('before:', loc)
    exec('x += 1')
    print('after:', loc)
    print('x =', x)

def test3():
    x = 0
    loc = locals()
    print(loc)
    exec('x += 1')
    print(loc)
    locals()
    print(loc)
 
def test4():
    a = 13
    loc = { 'a' : a }
    glb = { }
    exec('b = a + 1', glb, loc)
    b = loc['b']
    print(b)

if __name__ == '__main__':
    print(':::: Running test()')
    test()

    print(':::: Running test1()')
    test1()

    print(':::: Running test2()')
    test2()

    print(':::: Running test3()')
    test3()

    print(':::: Running test4()')
    test4()

# # Problem
#     # You are using exec() to execute a fragment of code in the scope of the caller, but after
#     # execution, none of its results seem to be visible.
#     # Solution
#     # To better understand the problem, try a little experiment. First, execute a fragment of
#     # code in the global namespace:

# Discussion
# Correct use of exec() is actually quite tricky in practice. In fact, in most situations where
# you might be considering the use of exec(), a more elegant solution probably exists
# (e.g., decorators, closures, metaclasses, etc.).
# However, if you still must use exec(), this recipe outlines some subtle aspects of using
# it correctly. By default, exec() executes code in the local and global scope of the caller.
# However, inside functions, the local scope passed to exec() is a dictionary that is a copy
# of the actual local variables. Thus, if the code in exec() makes any kind of modification,
# that modification is never reflected in the actual local variables. Here is another example
# that shows this effect:

# When you call locals() to obtain the local variables, as shown in the solution, you get
# the copy of the locals that is passed to exec(). By inspecting the value of the dictionary
# after execution, you can obtain the modified values. Here is an experiment that shows
# this:

# Carefully observe the output of the last step. Unless you copy the modified value from
# loc back to x, the variable remains unchanged.
# With any use of locals(), you need to be careful about the order of operations. Each
# time it is invoked, locals() will take the current value of local variables and overwrite
# the corresponding entries in the dictionary. Observe the outcome of this experiment:

# Notice how the last call to locals() caused x to be overwritten.
# As an alternative to using locals(), you might make your own dictionary and pass it
# to exec(). For example:

# For most uses of exec(), this is probably good practice. You just need to make sure that
# the global and local dictionaries are properly initialized with names that the executed
# code will access.
# Last, but not least, before using exec(), you might ask yourself if other alternatives are
# available. Many problems where you might consider the use of exec() can be replaced
# by closures, decorators, metaclasses, or other metaprogramming features.

 

 

