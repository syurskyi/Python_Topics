c_ PrimeNumber(_.?):
    prime_numbers = {} 
    lock = _.?
    
    ___ - (self, number): 
        _.?.- (self)
        Number = number
        PrimeNumber.lock.a.. 
        PrimeNumber.prime_numbers[number] = "None" 
        PrimeNumber.lock.r.. 
 
    ___ run 
        counter = 2
        res = True
        w___ counter*counter < Number a.. res:
            __ Number @ counter == 0:
               res = False 
            counter += 1 
        PrimeNumber.lock.a.. 
        PrimeNumber.prime_numbers[Number] = res 
        PrimeNumber.lock.r.. 
threads   # list
w___ True: 
    input = long(raw_input("number: ")) 
    __ input < 1:
        break 
 
    thread = PrimeNumber(input) 
    threads += [thread] 
    thread.s..
 
___ x __ threads: 
    x.j..
    
