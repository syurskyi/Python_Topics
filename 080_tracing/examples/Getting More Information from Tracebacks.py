# Problem
# You want to display all of the available information when an uncaught exception is raised.
#
# Solution
# A traceback object is basically a linked list of nodes, in which each node refers to a frame object. Frame objects,
# in turn, form their own linked list opposite the linked list of traceback nodes, so we can walk back and forth
# if needed. This recipe exploits this structure and the rich amount of information held by frame objects, including
# the dictionary of local variables for the function corresponding to each frame, in particular:
#
# import sys, traceback
#
def print_exc_plus(  ):
    """
    Print the usual traceback information, followed by a listing of all the
    local variables in each frame.
    """
    tb = sys.exc_info(  )[2]
    while 1:
        if not tb.tb_next:
            break
        tb = tb.tb_next
    stack = []
    f = tb.tb_frame
    while f:
        stack.append(f)
        f = f.f_back
    stack.reverse(  )
    traceback.print_exc(  )
    print "Locals by frame, innermost last"
    for frame in stack:
        print
        print "Frame %s in %s at line %s" % (frame.f_code.co_name,
                                             frame.f_code.co_filename,
                                             frame.f_lineno)
        for key, value in frame.f_locals.items(  ):
            print "\t%20s = " % key,
            # We have to be VERY careful not to cause a new error in our error
            # printer! Calling str(  ) on an unknown object could cause an
            # error we don't want, so we must use try/except to catch it --
            # we can't stop it from happening, but we can and should
            # stop it from propagating if it does happen!
            try:
                print value
            except:
                print "<ERROR WHILE PRINTING VALUE>"
# Discussion
# The standard Python traceback module provides useful functions to produce lots of information about where and why
# an error occurred. However, traceback objects actually contain a great deal more information than the traceback module
# displays (indirectly, via the frame objects they refer to). This extra information can greatly assist in detecting
# the cause of some errors you encounter. This recipe gives an example of an extended traceback printer you might use.
#
# Here is a simplistic demonstration of the kind of problem this approach can help with. Basically, we have
# a simple function that manipulates all the strings in a list. The function doesnt do any error checking,
# so when we pass a list that contains something other than strings, we get an error. Figuring out which bad data caused
# the error is easier with our new print_exc_plus function to help us:
#

data = ["1", "2", 3, "4"]     # Typo: we 'forget' the quotes on data[2]
def pad4(seq):
    """
    Pad each string in seq with zeros up to four places. Note that there
    is no reason to actually write this function; Python already
    does this sort of thing much better. It's just an example!
    """
    return_value = []
    for thing in seq:
        return_value.append("0" * (4 - len(thing)) + thing)
    return return_value

# Here is the (limited) information we get from a normal traceback.print_exc:
#
# >>> try:
# ...     pad4(data)
# ... except:
# ...     traceback.print_exc(  )
# ...
# Traceback (most recent call last):
#   File "<stdin>", line 2, in ?
#   File "<stdin>", line 9, in pad4
# TypeError: len(  ) of unsized object

# Now here is how it looks with our new function:
#
# >>> try:
# ...     pad4(data)
# ... except:
# ...     print_exc_plus(  )
# ...
# Traceback (most recent call last):
#   File "<stdin>", line 2, in ?
#   File "<stdin>", line 9, in pad4
# TypeError: len(  ) of unsized object
# Locals by frame, innermost last
#
# Frame ? in <stdin> at line 4
#                          sys =  <module 'sys' (built-in)>
#                         pad4 =  <function pad4 at 0x007C6210>
#                 _ _builtins_ _ =  <module '_ _builtin_ _' (built-in)>
#                     _ _name_ _ =  _ _main_ _
#                    traceback =  <module 'traceback' from 'C:\Python22\lib\traceback.py'>
#                         data =  ['1', '2', 3, '4']
#                      _ _doc_ _ =  None
#               print_exc_plus =  <function print_exc_plus at 0x00802038>
#
# Frame pad4 in <stdin> at line 9
#                        thing =  3
#                 return_value =  ['0001', '0002']
#                          seq =  ['1', '2', 3, '4']
# Note how easy it is to see the bad data that caused the problem. The thing variable has a value of 3, so we know that
# the TypeError we got was because of this. A quick look at the value for data shows that we simply forgot the quotes on
# that item.
#
# So we can either fix the data or decide to make pad4 a bit more tolerant (e.g., by changing the loop to for thing in
# map(str,seq):). This kind of thing is an important design choice, but the point of this recipe is to save you time in
# understanding what is going on, so you can make your design choices with all the available information.
#
# The recipe relies on the fact that each traceback object refers to the next traceback object in the stack through
# the tb_next field, forming a linked list. Each traceback object also refers to a corresponding frame object through
# the tb_frame field, and each frame refers to the previous frame through the f_back field (a linked list going
# the other way around from that of the traceback objects).
#
# For simplicity, the recipe accumulates references to all the frame objects in a local list called stack,
# then loops over the list, emitting information about each frame. For each frame, it first emits some basic information
# (function name, filename, line number, and so on) then turns to the dictionary representing the local variables
# of the frame, to which the f_locals field refers. Just like for the dictionaries built and returned by the locals and
# globals built-in functions, each key is a variable name, and the corresponding value is the variable's value.
# The only point of note here is that while printing the name is safe (it's just a string), printing
# the value might fail, because it could invoke an arbitrary and buggy _ _str_ _ method of a user-defined object.
# So the value is printed within a try/except statement to prevent raising an uncaught exception while handling another
# exception.
#
# I use a technique very similar to this in the applications I develop. Unexpected errors are logged in
# a format like this, which makes it a lot easier to figure out what is gone wrong.