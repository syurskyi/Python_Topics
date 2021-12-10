______ _
 
c_ PrimeNumber(_.?):
  ___ -  number):
    _.?.- (self)
    Number = number
 
  ___ run 
    counter = 2 
    w___ counter*counter < Number: 
      __ Number @ counter == 0:
        print "%d is no prime number, because %d = %d * %d" @ ( Number, Number, counter, Number / counter)
                r_ 
            counter += 1 
        print "%d is a prime number" @ Number
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
