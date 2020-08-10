______ ___
sum _ 0
w__ True:
    ___
        line _ input()                     # or call sys.stdin.readlines()
    ______ EOFError:                       # or for line in sys.stdin:
        break                              # input strips \n at end
    ____
        sum +_ int(line)                   # was sting.atoi() in 2nd ed
print(sum)
