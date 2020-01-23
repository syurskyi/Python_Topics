# Function in the 'trace' module in Python library generates trace of program execution, and annotated statement
# coverage. It also has functions to list functions called during run by generating caller relationships.
#
# Following two Python scripts are used as an example to demonstrate features of trace module.

#myfunctions.py
import math
def area(x):
   a = math.pi*math.pow(x,2)
   return a

def factorial(x):
   if x==1:
      return 1
   else:
       return x*factorial(x-1)

#mymain.py
import myfunctions
def main():
   x = 5
   print ('area=',myfunctions.area(x))
   print ('factorial=',myfunctions.factorial(x))

if __name__=='__main__':
   main()

# The 'trace' module has a command line interface. All the functions in the module can be called using command line
# switches. The most important option is --trace which displays program lines as they are executed. In following
# example another option --ignore-dir is used. It ignores specified directories while generating the trace.
#
# E:\python37>python -m trace --ignore-dir=../lib --trace mymain.py

# Output
# mymain.py(2): def main():
# mymain.py(7): if __name__=='__main__':
# mymain.py(8): main()
# --- modulename: mymain, funcname: main
# mymain.py(3): x=5
# mymain.py(4): print ('area=',myfunctions.area(x))
# --- modulename: myfunctions, funcname: area
# myfunctions.py(3): a=math.pi*math.pow(x,2)
# myfunctions.py(4): return a
# area= 78.53981633974483
# mymain.py(5): print ('factorial=',myfunctions.factorial(x))
# --- modulename: myfunctions, funcname: factorial
# myfunctions.py(6): if x==1:
# myfunctions.py(9): return x*factorial(x-1)
# --- modulename: myfunctions, funcname: factorial
# myfunctions.py(6): if x==1:
# myfunctions.py(9): return x*factorial(x-1)
# --- modulename: myfunctions, funcname: factorial
# myfunctions.py(6): if x==1:
# myfunctions.py(9): return x*factorial(x-1)
# --- modulename: myfunctions, funcname: factorial
# myfunctions.py(6): if x==1:
# myfunctions.py(9): return x*factorial(x-1)
# --- modulename: myfunctions, funcname: factorial
# myfunctions.py(6): if x==1:
# myfunctions.py(7): return 1
# factorial= 120
# The --count option generates a file for each module in use with, cover extension.
#
# E:\python37>python -m trace --count mymain.py
# area= 78.53981633974483
# factorial = 120
# myfunctions.cover
#
# 1: import math
# 1: def area(x):
# 1:    a = math.pi*math.pow(x,2)
# 1:    return a
# 1: def factorial(x):
# 5:    if x==1:
# 1:       return 1
#    else:
# 4:    return x*factorial(x-1)
# mymain.cover
#
# 1: import myfunctions
# 1: def main():
# 1:    x = 5
# 1:    print ('area=',myfunctions.area(x))
# 1:    print ('factorial=',myfunctions.factorial(x))
#
# 1: if __name__=='__main__':
# 1:    main()
# --summary option displays a brief summary if –count option is also used.
#
# E:\python37>python -m trace --count --summary mymain.py
# area = 78.53981633974483
# factorial = 120
# lines cov% module (path)
#    8 100% myfunctions (E:\python37\myfunctions.py)
#    7 100% mymain (mymain.py)
# The --file option specifies name of file in which accumulates count over several tracing runs.
#
# E:\python37>python -m trace --count --file report.txt mymain.py
# area = 78.53981633974483
# factorial = 120
# Skipping counts file 'report.txt': [Errno 2] No such file or directory: 'report.txt'
#
# E:\python37>python -m trace --count --file report.txt mymain.py
# area= 78.53981633974483
# factorial= 120
# --listfuncs option displays functions called during execution of program.
#
# E:\python37>python -m trace --listfunc mymain.py | findstr -v importlib
# area= 78.53981633974483
# factorial= 120
#
# functions called:
# filename: E:\python37\lib\encodings\cp1252.py, modulename: cp1252, funcname: IncrementalEncoder.encode
# filename: E:\python37\myfunctions.py, modulename: myfunctions, funcname: <module>
# filename: E:\python37\myfunctions.py, modulename: myfunctions, funcname: area
# filename: E:\python37\myfunctions.py, modulename: myfunctions, funcname: factorial
# filename: mymain.py, modulename: mymain, funcname: <module>
# filename: mymain.py, modulename: mymain, funcname: main
# --trackcalls option is used along with –list funcs option. It generates calling relationships.
#
# E:\python37>python -m trace --listfunc --trackcalls mymain.py | findstr -v importlib
# area= 78.53981633974483
# factorial= 120
#
# calling relationships:
#
# --> E:\python37\myfunctions.py
#
#
# *** E:\python37\lib\trace.py ***
# --> mymain.py
# trace.Trace.runctx -> mymain.<module>
#
# *** E:\python37\myfunctions.py ***
# myfunctions.factorial -> myfunctions.factorial
#
# *** mymain.py ***
# mymain.<module> -> mymain.main
# --> E:\python37\lib\encodings\cp1252.py
# mymain.main -> cp1252.IncrementalEncoder.encode
# --> E:\python37\myfunctions.py
# mymain.main -> myfunctions.area
# mymain.main -> myfunctions.factorial

