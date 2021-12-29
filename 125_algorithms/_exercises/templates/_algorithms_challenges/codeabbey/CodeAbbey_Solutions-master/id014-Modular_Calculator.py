___ modCalc(num):
        calc = raw_input()
        w.... calc[:1] != "%":
                __ calc[:1] __ '+':
                        num += int(calc[2:].strip())
                ____ calc[:1] __ '*':
                        num *= int(calc[2:].strip())
                calc = raw_input()
        num %= int(calc[2:].strip()) 
        print(num)
modCalc(input())
