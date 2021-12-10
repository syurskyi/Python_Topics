______ _
 
class PrimeNumber(_.?):
  ___ __init__(self, number): 
    _.?.__init__(self)
    self.Number = number
 
  ___ run(self): 
    counter = 2 
    w___ counter*counter < self.Number: 
      if self.Number % counter == 0: 
        print "%d is no prime number, because %d = %d * %d" % ( self.Number, self.Number, counter, self.Number / counter) 
                return 
            counter += 1 
        print "%d is a prime number" % self.Number
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
