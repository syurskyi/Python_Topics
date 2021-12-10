#!/usr/bin/python


# This program takes an string input from a user
# and print the input __ a text file


______ _ 
______ t__ 


c_ AsyncWrite(_.?):
  ___ - (self, text, out):
    _.?.- (self)
    text = text
    out = out 

    
  ___ run
    file = open(out, "a")
    file.write(text + '\n')
    file.close()
    t__.s..(2)
    print "Done! Completed storing input in a file named " + out 


___ Main():
  message = raw_input("Enter a string: ")
  bg = AsyncWrite(message, 'out.txt')
  
  bg.s..
  print "Hold on, the program is generating a file"
  

__ _____ __ ______
  Main()
