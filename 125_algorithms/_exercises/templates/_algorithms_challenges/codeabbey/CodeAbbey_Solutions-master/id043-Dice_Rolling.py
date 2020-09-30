___ findRoll(rolls
        output =   # list
        ___ roll __ range(rolls
                rawRoll = input()
                calculatedRoll = int(rawRoll * 6) + 1
                output.append(str(calculatedRoll))
        print(' '.join(output))
findRoll(input())
