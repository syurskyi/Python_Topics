___ lcm(a,b # Least Common Multiple
        r_(a * b / gcd(a, b))
        
___ gcd(a,b # Greatest Common Divisor
        w___ b:
                a, b = b, a % b
        r_ a

___ findDivisors(pairs
        answer = []
        for pair in range(pairs
                a,b = raw_input().split()
                a,b = int(a), int(b)
                answer.append('('+str(gcd(a,b))+' '+str(lcm(a,b))+')')
        print(' '.join(answer))
findDivisors(input())
