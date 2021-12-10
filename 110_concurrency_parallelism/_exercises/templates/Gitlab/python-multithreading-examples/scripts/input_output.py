#!/usr/bin/python


# This program takes an string input from a user
# and print the input __ a text file


______ _ 
______ t__ 


class AsyncWrite(_.?):
  ___ __init__(self, text, out):
    _.?.__init__(self)
    self.text = text
    self.out = out 

    
  ___ run(self):
    file = open(self.out, "a")
    file.write(self.text + '\n')
    file.close()
    t__.s..(2)
    print "Done! Completed storing input in a file named " + self.out 


___ Main():
  message = raw_input("Enter a string: ")
  bg = AsyncWrite(message, 'out.txt')
  
  bg.s..
  print "Hold on, the program is generating a file"
  

__ _____ __ ______
  Main()
