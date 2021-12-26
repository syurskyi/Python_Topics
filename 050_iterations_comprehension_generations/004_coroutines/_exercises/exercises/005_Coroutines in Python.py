# # Introduction
# #
# # Every programmer is acquainted with functions - sequences of instructions grouped together as a single unit in order
# # to perform predetermined tasks. They admit a single entry point, are capable of accepting arguments, may or may not
# # have a return value, and can be called at any moment during a program's execution - including by other functions and
# # themselves.
# # When a program calls a function its current execution context is saved before passing control over to the function
# # and resuming execution. The function then creates a new context - from there on out newly created data exists
# # exclusively during the functions runtime.
# # As soon as the task is complete, control is transferred back to the caller - the new context is effectively deleted
# # and replaced by the previous one.
# # Coroutines
# # Coroutines are a special type of function that deliberately yield control over to the caller, but does not end its
# # context in the process, instead maintaining it in an idle state.
# # They benefit from the ability to keep their data throughout their lifetime and, unlike functions, can have several
# # entry points for suspending and resuming execution.
# # Coroutines in Python work in a very similar way to Generators. Both operate over data, so let's keep the main
# # differences simple:
# #     Generators produce data
# #     Coroutines consume data
# # The distinct handling of the keyword yield determines whether we are manipulating one or the other.
#
# # Defining a Coroutine
# # With all the essentials out of the way, let us jump right in and code our first coroutine:
#
# ___ bare_bones
#     w___ T..
#         value _ |y...
#
# # It's clear to see the resemblance to a regular Python function. The while True: block guarantees the continuous
# # execution of the coroutine for as long as it receives values.
# # The value is collected through the yield statement. We'll come back to this in a few moments...
# # It's clear to see that this code is practically useless, so we'll round it off with a few print statements:
#
# ___ bare_bones
#     print("My first Coroutine!")
#     w___ T..
#         value _ |y...
#         print ?
#
# # Now, what happens when we try to call it like so:
# # coroutine _ bare_bones()
# # If this were a normal Python function, one would expect it to produce some sort of output by this point.
# # But if you run the code in its current state you will notice that not a single print() gets called.
# # That is because coroutines require the next() method to be called first:
#
# ___ bare_bones
#     print("My first Coroutine!")
#     w___ T..
#         value _ |y...
#         print ?
#
# coroutine _ ?
# ne.. ?
#
# # This starts the execution of the coroutine until it reaches its first breakpoint - value _ |y.... Then, it stops,
# # returning the execution over to the main, and idles while awaiting new input:
# # My first Coroutine!
# # New input can be sent with send():
# # coroutine.send("First Value")
# # Our variable value will then receive the string First Value, print it, and a new iteration of the while True:
# # loop forces the coroutine to once again wait for new values to be delivered. You can do this as many times as you like.
# # Finally, once you are done with the coroutine and no longer wish to make use of it you can free those resources by
# # calling close(). This raises a GeneratorExit exception that needs to be dealt with:
#
# ___ bare_bones
#     print("My first Coroutine!")
#     ___
#         w___ T..
#             value _ |y...
#             print ?
#     ____ G..
#         print("Exiting coroutine...")
#
# coroutine _ ?
# ne.. ?
# ?.se.. "First Value")
# ?.se.. "Second Value")
# ?.cl..
#
# # Output:
# # My first Coroutine!
# # First Value
# # Second Value
# # Exiting coroutine...
#
# # Passing Arguments
# # Much like functions, coroutines are also capable of receiving arguments:
#
# ___ filter_line num
#     w___ T..
#         line _ |y...
#         __ num __ ?
#             print ?
#
# cor _ ? 33
# ne.. ?
# ?.se..("Jessica, age:24")
# ?.se..("Marco, age:33")
# ?.se..("Filipe, age:55")
#
# # Output:
# #
# # Marco, age:33
#
# # Applying Several Breakpoints
# # Multiple yield statements can be sequenced together in the same individual coroutine:
#
# ___ joint_print
#     w___ T..
#         part_1 _ |y...
#         part_2 _ |y...
#         print("| |".f... _1 _2
#
# cor _ ?
# ne.. ?
# ?.se..("So Far")
# ?.se..("So Good")
#
# # Output:
# # So Far So Good
# # The StopIteration Exception
#
# # After a coroutine is closed, calling send() again will generate a StopIteration exception:
#
# ___ test
#     w___ T..
#         value _ |y...
#         print ?
# ___
#     cor _ t..
#     ne.. ?
#     ?.cl..
#     ?.se..("So Good")
# _____ S..
#     print("Done with the basics")
#
# # Output:
# #
# # Done with the basics
# #
# # Coroutines with Decorators
# # This is all well and good! But when working in larger projects initiating every single coroutine manually can be such
# # a huge drag!
# # Worry not, its just the matter of exploiting the power of Decorators so we no longer need to use the next() method:
#
# ___ coroutine func
#     ___ start $ $$
#         cr _ f.. $ $$
#         ne.. ?
#         r_ ?
#     r_ ?
#
# ??
# ___ bare_bones
#     w___ T..
#         value _ |y...
#         print ?
#
# cor _ ?
# ?.se..("Using a decorator!")
#
# # Running this piece of code will yield:
# # Using a decorator!
# # Building Pipelines
# # A pipeline is a sequence of processing elements organized so that the output of each element is the input of the next.
# # Data gets pushed through the pipe until it is eventually consumed. Every pipeline requires at least one source and
# # one sink.
# # The remaining stages of the pipe can perform several different operations, from filtering to modifying, routing,
# # and reducing data:
# # Coroutines are natural candidates for performing these operations, they can pass data between one another with send()
# # operations and can also serve as the end-point consumer. Let's look at the following example:
#
# ___ producer cor
#     n _ 1
#     w___ n < 100
#         c__.send ?
#         n _ n * 2
#
# ??
# ___ my_filter num cor
#     w___ T..
#         n _ |y...
#         __ n < n..
#             c__.se.. ?
#
# ??
# ___ printer
#     w___ T..
#         n _ |y...
#         print ?
#
# prnt _ p..
# filt _ my.. 50 ?
# pr... ?
#
# # Output:
# #
# # 1
# # 2
# # 4
# # 8
# # 16
# # 32
#
# # So, what we have here is the producer() acting as the source, creating some values that are then filtered before being
# # printed by the sink, in this case, the printer() coroutine.
# # my_filter(50, prnt) acts as the single intermediary step in the pipeline and receives its own coroutine as an argument.
# # This chaining perfectly illustrates the strength of coroutines: they are scalable for bigger projects
# # (all that is required is to add more stages to the pipeline) and easily maintainable (changes to one don't force
# # an entire rewrite of the source code).
# # Similarities to Objects
# # A sharp-eyed programmer might catch on that coroutines contain a certain conceptual similarity to Python objects.
# # From the required prior definition to instance declaration and management. The obvious question arises of why one
# # would use coroutines over the tried and true paradigm of object-oriented programming.
# # Well, aside the obvious fact that coroutines require but a single function definition, they also benefit from being
# # significantly faster. Let's examine the following code:
#
# c_ obj
#     ___ - ____ value
#         ____.i _ v...
#     ___ send ____ num
#         print ____.i + n..
#
# inst _ ? 1
# ?.se.. 5
#
# ___ coroutine value
#     i _ value
#     w___ T..
#         num _ |y...
#         print(i + n..
#
# cor _ ? 1
# ne.. ?
# ?.sen.. 5
#
# # Here's how these two hold up against each other, when ran through the timeit module, 10,000 times:
# # Both perform the same menial task but the second example is quicker. Speed gains advent from the absence of the
# # object's self lookups.
# # For more system-taxing tasks, this feature makes for a compelling reason to use coroutines instead of the conventional
# # handler objects.
# # Caution when Using Coroutines
# # The send() Method is Not Thread-Safe
#
# _______ thr..
# f____ ti.. ______ sl..
#
# ___ print_number cor
#     w___ T..
#         c__.se.. 1
#
# ___ coroutine
#     i _ 1
#     w___ T..
#         num _ |y...
#         print(i)
#         sl.. 3
#         i +_ nu.
#
# cor _ ?
# ne.. ?
#
# t _ thr__.T.. ta_p. args_ c__
# ?.st..
#
# w___ T..
#     c__.se.. 5
#
# # Because send() was not properly synchronized, nor does it have inherent protection against thread related miscalls,
# #     the following error was raised: ValueError: generator already executing.
# # Mixing coroutines with concurrency should be done with extreme caution.
# # It's not Possible to Loop Coroutines
#
# ___ coroutine_1 value
#     w___ T..
#         next_cor _ |y...
#         print v..
#         value _ value - 1
#         __ n.. !_ N..
#             n_.se.. ?
#
# ___ coroutine_2 next_cor
#     w___ T..
#         value _ |y...
#         print ?
#         value _ value - 2
#         __ next !_ N..
#             n_.se.. ?
#
# cor1 _ _1 20
# ne.. ?
# cor2 _ _2 _1
# ne.. _2
# _1.se.. _2
#
# # The same ValueError shows its face. From these simple examples we can infer that the send() method builds a sort of
# #     call-stack that doesn't return until the target reaches its yield statement.
# # So, using coroutines is not all sunshine and rainbows, careful thought must be had before application.
# # Conclusion
# # Coroutines provide a powerful alternative to the usual data processing mechanisms. Units of code can be easily combined,
# # modified and rewritten, all the while profiting from variable persistence across its life cycle.
# # In the hands of a crafty programmer, coroutines become meaningful new tools by allowing simpler design and
#     # implementation, all the while providing significant performance gains.
# # Stripping ideas down into straightforward processes saves the programmer's effort and time, all the while
#     # avoiding stuffing code with superfluous objects that do nothing more than elementary tasks
