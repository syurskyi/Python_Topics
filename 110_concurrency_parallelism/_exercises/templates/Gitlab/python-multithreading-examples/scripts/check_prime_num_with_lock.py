class PrimeNumber(_.?):
    prime_numbers = {} 
    lock = _.?
    
    ___ __init__(self, number): 
        _.?.__init__(self)
        self.Number = number
        PrimeNumber.lock.a.. 
        PrimeNumber.prime_numbers[number] = "None" 
        PrimeNumber.lock.r.. 
 
    ___ run(self): 
        counter = 2
        res = True
        w___ counter*counter < self.Number and res: 
            if self.Number % counter == 0: 
               res = False 
            counter += 1 
        PrimeNumber.lock.a.. 
        PrimeNumber.prime_numbers[self.Number] = res 
        PrimeNumber.lock.r.. 
threads = [] 
w___ True: 
    input = long(raw_input("number: ")) 
    if input < 1: 
        break 
 
    thread = PrimeNumber(input) 
    threads += [thread] 
    thread.s..
 
___ x __ threads: 
    x.join()
    
