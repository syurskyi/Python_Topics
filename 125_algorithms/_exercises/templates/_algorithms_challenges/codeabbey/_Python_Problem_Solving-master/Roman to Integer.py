c_ Solution:
    ___ romanToInt  s: s..) __ i..:
        rom_dic = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        count = 0
        #i will track the length of the string
        i = 0
        w.... i != l..(s
            __ s[i] __ 'I':
                ___
                    __ s[i+1]__'V':
                        count += 4
                        i += 2
                        _____
                    ____ s[i+1]__'X':
                        count += 9
                        i += 2
                        _____
                ______:
                    p..
            __ s[i] __ 'X':
                ___
                    __ s[i+1]__'L':
                        count += 40
                        i += 2
                        _____
                    ____ s[i+1]__'C':
                        count += 90
                        i += 2
                        _____
                ______:
                    p..
            __ s[i] __ 'C':
                ___
                    __ s[i+1]__'D':
                        count += 400
                        i += 2
                        _____
                    ____ s[i+1]__'M':
                        count += 900
                        i += 2
                        _____
                ______:
                    p..
            __ s[i] __ rom_dic:
                count += rom_dic[s[i]]
                i += 1
            
        r.. count
                