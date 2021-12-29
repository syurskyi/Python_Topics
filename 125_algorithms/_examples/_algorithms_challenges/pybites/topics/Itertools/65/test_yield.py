
def some_list(x):
    for i in range(x):
        for j in range(i):
            yield (i+1)*(j+1)

print(list(some_list(5)))