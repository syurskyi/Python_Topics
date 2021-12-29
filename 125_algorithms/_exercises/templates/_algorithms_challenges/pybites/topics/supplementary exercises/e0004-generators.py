import memory_profiler as mem_profile
import random
import time


___ function_1():
    with open("sample_file.txt") as infile:
        for line in infile:
            print(line.strip())

___ function_2():

    with open("sample_file.txt") as infile:
        print(type(infile))
        data = infile.readlines()
        for line in data:
            print(line.strip())

___ function_3():
    with open("sample_file.txt") as infile:
        return (word for word in infile.readline())
___ gen():

    with open("sample_file.txt") as infile:
        for line in infile:
            yield line

#for i in gen():
#    print(i.strip())

print(f'Memory (Before): {mem_profile.memory_usage()}')

g = function_3()
for word in g:
    print(word)
