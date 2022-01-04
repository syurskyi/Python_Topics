_______ memory_profiler __ mem_profile
_______ random
_______ time


___ function_1
    with open("sample_file.txt") __ infile:
        ___ line __ infile:
            print(line.strip())

___ function_2

    with open("sample_file.txt") __ infile:
        print(t..(infile))
        data = infile.readlines()
        ___ line __ data:
            print(line.strip())

___ function_3
    with open("sample_file.txt") __ infile:
        r.. (word ___ word __ infile.readline())
___ gen

    with open("sample_file.txt") __ infile:
        ___ line __ infile:
            y.. line

#for i in gen():
#    print(i.strip())

print(f'Memory (Before): {mem_profile.memory_usage()}')

g = function_3()
___ word __ g:
    print(word)
