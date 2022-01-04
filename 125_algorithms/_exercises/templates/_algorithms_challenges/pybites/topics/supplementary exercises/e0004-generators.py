_______ memory_profiler __ mem_profile
_______ r__
_______ time


___ function_1
    w__ open("sample_file.txt") __ infile:
        ___ line __ infile:
            print(line.strip())

___ function_2

    w__ open("sample_file.txt") __ infile:
        print(t..(infile))
        data = infile.readlines()
        ___ line __ data:
            print(line.strip())

___ function_3
    w__ open("sample_file.txt") __ infile:
        r.. (word ___ word __ infile.readline())
___ gen

    w__ open("sample_file.txt") __ infile:
        ___ line __ infile:
            y.. line

#for i in gen():
#    print(i.strip())

print _*Memory (Before): {mem_profile.memory_usage()}')

g = function_3()
___ word __ g:
    print(word)
