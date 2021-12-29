___ lcm(a,b): # Least Common Multiple
        r..(a * b / gcd(a, b))
        
___ gcd(a,b): # Greatest Common Divisor
        while b:      
                a, b = b, a % b
        r.. a

___ findDivisors(pairs):
        answer    # list
        ___ pair __ r..(pairs):
                a,b = raw_input().s..
                a,b = int(a), int(b)
                answer.a..('('+str(gcd(a,b))+' '+str(lcm(a,b))+')')
        print(' '.join(answer))
findDivisors(input())
