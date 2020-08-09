___ sumDigits(sumCount
        answer = []
        ___ eachLine in range(sumCount
                [a,b,c] = raw_input().split(' ')
                value = (int(a) * int(b)) + int(c)
                value = list(str(value))
                su. = 0
                ___ digit in value:
                        su. += int(digit)
                answer.append(str(su.))
        print(' '.join(answer))
sumDigits(input())
