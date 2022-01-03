___ lcm(a,b): # Least Common Multiple
        r..(a * b / gcd(a, b))
        
___ gcd(a,b): # Greatest Common Divisor
        w.... b:
                a, b = b, a % b
        r.. a

___ findDivisors(pairs):
        answer    # list
        ___ pair __ r..(pairs):
                a,b = raw_input().s..
                a,b = int(a), int(b)
                answer.a..('('+s..(gcd(a,b))+' '+s..(lcm(a,b))+')')
        print(' '.j..(answer))
findDivisors(input())
