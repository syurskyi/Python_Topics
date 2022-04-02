___ modCalc(num
        calc = raw_input()
        w.... calc[:1] != "%":
                __ calc[:1] __ '+':
                        num += i..(calc[2:].strip())
                ____ calc[:1] __ '*':
                        num *= i..(calc[2:].strip())
                calc = raw_input()
        num %= i..(calc[2:].strip()) 
        print(num)
modCalc(input())
