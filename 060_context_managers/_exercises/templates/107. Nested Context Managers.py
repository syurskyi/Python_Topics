# # Nested Context Managers
# # In the last video we saw that we could nest context managers.
# # This is actually fairly common.
# # Suppose we need to open a number of files - using a with statement for each one means we would have to nest that
# # many with statements as well.
# # For example, we want to "zip" three files. Let's look at the content of each file first:
#
# print('#' * 52 + '  ### Nested Context Managers')
#
# w___ o... file1.txt a_ f
#     ___ row i_ f
#         print r. e.._''
# print('\n----------------')
# w___ o... file2.txt a_ f
#     ___ row i_ f
#         print r.. e.._''
# print('\n----------------')
# w___ o... file3.txt a_ f
#     ___ row i_ f
#         print r.. e.._'
# # file1_line1
# # file1_line2
# # file1_line3
# # ----------------
# # file2_line1
# # file2_line2
# # file2_line3
# # ----------------
# # file3_line1
# # file3_line2
# # file3_line3
# # ######################################################################################################################
#
# # Now we want to combine the rows from each file, and print them out - like zipping together basically, except
# # we need to strip out that pesky \n!
# print(
#     '#' * 52 + '  Now we want to combine the rows from each file, and print them out - like zipping together basically,'
#                '  except we need to strip out that pesky `n`!')
#
# w___ o... file1.txt a_ f1
#     w___ o... file2.txt a_ f2
#         w___ o... file3.txt a_ f3
#             w___ T..
#                 t_
#                     f1_row _ n... f1 .st... '\n'
#                     f2_row _ n... f2 .st... '\n'
#                     f3_row _ n... f3 .st... '\n'
#                 e___ S..I..
#                     b____
#                 e___
#                     print 1_ + ',' + 2_ + ',' + 3_
# # file1_line1,file2_line1,file3_line1
# # file1_line2,file2_line2,file3_line2
# # file1_line3,file2_line3,file3_line3
# # ######################################################################################################################
#
#
# # As you can see we needed three levels of nested with statements.
# # Instead, we might try to approach the problem this way - but first let's write our own openfile context manager
# # so we can easily see when the file is being opened and closed
# print('#' * 52 + '  As you can see we needed three levels of nested `with` statements.')
#
# f___ c..m.. _______ c..m..
#
#
# 0c..m..
# ___ open_file f_name
#     print _'opening file |f_..|
#     f _ o... f_..
#     t_
#         y___ ?
#     f___
#         print _'closing file |f_..|
#         ?.cl..
#
# # First we are going to create (but not enter) the context managers, and store the enter and exit methods in some lists.
# # We'll also create a list that will contain the values returned by the enter methods:
#
#
# print('#' * 52 + '  First we are going to create (but not enter) the context managers,'
#                  '  and store the enter and exit methods in some lists.')
# print('#' * 52 + '  We will also create a list that will contain the values returned by the enter methods:')
#
# f_names = 'file1.txt', 'file2.txt', 'file3.txt'
#
# enters _
# exits _
# ___ f_name i_ f_names
#     ctx _ o... f_.
#     e____.ap.. c_.__e__
#     e____.ap.. c_.__e__
#
# # Now, we are going to enter the contexts by calling the __enter__ methods, store the return values (the file objects),
# # process the data, and then run all the __exit__ methods (in reverse order!):
#
# files _ e.. ___ enter i_ e..
# # opening file file1.txt
# # opening file file2.txt
# # opening file file3.txt
# # ######################################################################################################################
#
# print('#' * 52 + '  ')
#
# w___ T..
#     t_
#         rows _  n... f .st...('\n') ___ f i_ f..
#     e___ S..I..:
#         b____
#     e___:
#         row _ ','.jo.. r..
#         print ?
# # file1_line1,file2_line1,file3_line1
# # file1_line2,file2_line2,file3_line2
# # file1_line3,file2_line3,file3_line3
# # ######################################################################################################################
#
# # Now, we need to close all the files by calling the __exit__ methods (in reverse order, since we aded them in
# # the order in which the contexts were opened (i.e. we open from first file to last, but close from last opened file
# # to first - think of how the context managers are nested).
# # Also, keep in mind that __exit__ methods need those exception parameters - here we'll just use None for simplicity -
# # we are not doing any exception handling!
#
# print('#' * 52 + '  ')
#
# ___ fn in e.. ;;-1
#     ? N.. N.. N..
# # closing file file3.txt
# # closing file file2.txt
# # closing file file1.txt
# # ######################################################################################################################
#
# # So, let's recap by putting all this code together and simplifying a few things along the way:
#
# print('#' * 52 + '  So, lets recap by putting all this code together and simplifying a few things along the way:')
#
# f_names _ 'file1.txt', 'file2.txt', 'file3.txt'
#
# exits _
# files _
# t_
#     ___ f_name i_ f_names
#         ctx _ o.._f.. f..
#         f____.ap.. c__.__e..__
#         e____.ap.. c__.__e..__
#
#     w___ T..
#         t_
#             rows _ n... f .st..('\n') ___ f i_ fi...
#         e___ S..I..
#             b____
#         e___
#             row _ , .j.. r..
#             print r..
# f______
#     ___ fn i_ e...  ;;-1
#         f. N... N... N...
# # opening file file1.txt
# # opening file file2.txt
# # opening file file3.txt
# # file1_line1,file2_line1,file3_line1
# # file1_line2,file2_line2,file3_line2
# # file1_line3,file2_line3,file3_line3
# # closing file file3.txt
# # closing file file2.txt
# # closing file file1.txt
# # ######################################################################################################################
#
# # What was simpler, this method or simply nesting the with blocks?
# # What if we were doing this with 100 files instead of just 3?
# # Or what if we did not know in advance how many files we had to zip together (maybe we're reading all the .txt
# # files in a directory for example - there may be 1 file, 3 files, 10 files, we don't realy know,
# # and it can change over time)?
# # Maybe we can find a way to make this a little easier to use.
# # Let's try using a context manager to hold on to all these __exit__ methods we want to use:
#
# print('#' * 52 + '  Lets try using a context manager to hold on to all these `__exit__` methods we want to use:')
#
#
# c_ NestedContexts
#     ___ __i__ ____ 0contexts
#         ____._en... _ ||
#         ____._ex.. _ ||
#         ____._va.. _ ||
#
#         ___ ctx i_ c..
#             ____._en___.ap.. ctx.__e__
#             ____._ex___.ap.. ctx.__ex__
#
#     ___ __en__ ____
#         ___ enter i_ ____._enters
#             ____._va___.ap.. en..
#         r_ ____._va...
#
#     ___ __e__ ____, ..............
#         ___ e... i_ ____._e... ;;-1
#             e... (........)
#         r_ F..
#
#
# w___ NestedContexts(o...('file1.txt'),
#                    o....('file2.txt'),
#                    o....('file3.txt')) a_ files
#     print('do work here')
#
# # opening file file1.txt
# # opening file file2.txt
# # opening file file3.txt
# # do work here
# # closing file file3.txt
# # closing file file2.txt
# # closing file file1.txt
# # ######################################################################################################################
#
# # As you can see, the files were opened, our work was done, and the files were closed. Let's just add in some real work:
#
# print('#' * 52 + '  As you can see, the files were opened, our work was done, and the files were closed.')
#
# w___ NestedContexts(open_file('file1.txt'),
#                    open_file('file2.txt'),
#                    open_file('file3.txt')) a_ files:
#     w___ T...
#         t_
#             rows _  n... f .st..('\n') ___ f i_ f...
#         e___ S..I..
#             b____
#         e___:
#             row _  , .j.. r..
#             print r..
# # opening file file1.txt
# # opening file file2.txt
# # opening file file3.txt
# # file1_line1,file2_line1,file3_line1
# # file1_line2,file2_line2,file3_line2
# # file1_line3,file2_line3,file3_line3
# # closing file file3.txt
# # closing file file2.txt
# # closing file file1.txt
# # ######################################################################################################################
#
# # This is much better, but specifying the context managers is still a little painful, having to list them all
# # separately as the arguments to the NestedContexts manager.
# #
# # We could simplify things somewhat by taking this approach:
#
# print('#' * 52 + '  This is much better, but specifying the context managers is still a little painful,'
#                  '  having to list them all separately as the arguments to the `NestedContexts` manager.')
# print('#' * 52 + '  We could simplify things somewhat by taking this approach:')
#
# file_names _ 'file1.txt', 'file2.txt', 'file3.txt'
# contexts _ o.._f.. f_n.. ___ f_n.. i_ f_n..
# w___ N....... 0c.. a_ files
#     w___ T..
#         t_
#             rows _ n... f .st..('\n') ___ f i_ f....
#         e___ S..I..
#             b____
#         e___:
#             row _ , .j.. r..
#             print r...
# # opening file file1.txt
# # opening file file2.txt
# # opening file file3.txt
# # file1_line1,file2_line1,file3_line1
# # file1_line2,file2_line2,file3_line2
# # file1_line3,file2_line3,file3_line3
# # closing file file3.txt
# # closing file file2.txt
# # closing file file1.txt
# # ######################################################################################################################
#
# # So, this works, and is actually quite workable, but we have to do some setup work before we can use
# # the context manager.
# # We can try a slightly different approach where we create a method in our NestedContextManager that can be used
# # to "register" contexts - so instead of creating the NestedContextManager with an __init__ that takes in all
# # the contexts at once, we create the NextedContextManager first, and then, inside the with block we append
# # the contexts we want to work with.
# # One main advantage to that approach is that we can add contexts to NestedContextManager at any time in
# # the with block - i.e. we can delay when and how we add contexts to the overarching context manager.
# # So, we'll do this by implementing a method in NestedContexts itself that will allow us to append a context manager,
# # get the __enter__ value out of it, and store the __exit__ methods.
# # To do this we're going to take a slightly different approach - the NestedContexts manager is going to return
# # itself in it's __enter__ method, instead of returning a list of the various context values returned
# # from their respective __enter__ methods:
#
# print('#' * 52 + '  ')
# print('#' * 52 + '  ')
# print('#' * 52 + '  ')
#
#
# c_ NestedContexts:
#     ___ __i__ ____
#         ____._exits = []
#
#     ___ __e__ ____
#         r_ ____
#
#     ___ enter_context ____ ctx
#         ____._ex___.ap.. ct_.__ex__
#         value _ ct_.__en__
#         r_ v...
#
#     ___ __e__ ............
#         ___ e... i_ ____._e.. ;;-1
#             e... .............
#         r_ F.
#
# # Now let's try it again, but this time we'll "register" our contexts once the NestedContexts context has been entered:
#
#
# f_names _ 'file1.txt', 'file2.txt', 'file3.txt'
#
# w___ N...... a_ stack
#     files _ st___.en.._c.. o.._f. f_n.. ___ f_n.. i_ f_..
# # opening file file1.txt
# # opening file file2.txt
# # opening file file3.txt
# # closing file file3.txt
# # closing file file2.txt
# # closing file file1.txt
#
# print('#' * 52 + '  Nice! Now lets just do the work as well:')
#
# f_names _ 'file1.txt', 'file2.txt', 'file3.txt'
#
# w___ N..... a_ stack
#     files _ st___.en.._co..(o.._f.. f_n..  ___ f_n.. i_ f_na..
#
#     w___ T...
#         t_
#             rows _  n... f .st.. ('\n') ___ f i_ fi...
#         e___ S..I..
#             b____
#         e___
#             row _ , .j.. r..
#             print r..
# # opening file file1.txt
# # opening file file2.txt
# # opening file file3.txt
# # file1_line1,file2_line1,file3_line1
# # file1_line2,file2_line2,file3_line2
# # file1_line3,file2_line3,file3_line3
# # closing file file3.txt
# # closing file file2.txt
# # closing file file1.txt
# # ######################################################################################################################
#
# # Hopefully you can now see why I said we can decide to add contyexts to that stack at any time inside
# # the with statement - we are not restricted to adding them in the __init__ - which means we can even use
# # if statements to add contexts to the stack if we want to - this is far more flexible.
# # So, this is a common enough scenario that the standard library has something up its sleeve for us!
# # The contextlib has an ExitStack context manager that works the same way as our NestedContexts, but,
# # unlike our approach, it actually does exception handling properly too!
# # Let's see how we use it:
#
# print('#' * 52 + '  The `contextlib` has an `ExitStack` context manager that works the same way as'
#                  '  our `NestedContexts`, but, unlike our approach, it actually does exception handling properly too!')
#
# f___ c...l.. _______ E..S..
#
# f_names _ 'file1.txt', 'file2.txt', 'file3.txt'
#
# w___ E..S.. a_ stack
#     files _  st__.en.._co.. o.._f.. f_n.. ___ f_na.. i_ f_n..
# # opening file file1.txt
# # opening file file2.txt
# # opening file file3.txt
# # closing file file3.txt
# # closing file file2.txt
# # closing file file1.txt
# # ######################################################################################################################
#
# # As you can see, the files were opened and automatically closed. Now all we need to do is the work itself:
#
# print('#' * 52 + '  As you can see, the files were opened and automatically closed.'
#                  '  Now all we need to do is the work itself:')
#
# f_names = 'file1.txt', 'file2.txt', 'file3.txt'
#
# w___ E..S.. a_ stack
#     files _ s___.e.._c.. o.._f.. f_n. ___ f_n.. i_ f_n..
#     w___ T..
#         t_
#             rows _  n... f .st..('\n') ___ f i_ f..
#         e___ S..I..
#             b____
#         e___
#             row _ , .j.. r..
#             print r..
# # opening file file1.txt
# # opening file file2.txt
# # opening file file3.txt
# # file1_line1,file2_line1,file3_line1
# # file1_line2,file2_line2,file3_line2
# # file1_line3,file2_line3,file3_line3
# # closing file file3.txt
# # closing file file2.txt
# # closing file file1.txt
# # ######################################################################################################################
#
#
# # To finish up we can use the built-in open context manager:
# print('#' * 52 + '  To finish up we can use the built-in `open` context manager:')
#
#
# f_names _ 'file1.txt', 'file2.txt', 'file3.txt'
#
# w___ E..S.. a_ stack
#     files _  s___.e..._c.. o... f_n.. ___ f_n.. i_ f_n..
#     w___ T..
#         t_
#             rows _ n... f .st.. ('\n') ___ f i_ fi..
#         e___ S..I..
#             b____
#         e___:
#             row _ , .j.. r..
#             print r..
# # file1_line1,file2_line1,file3_line1
# # file1_line2,file2_line2,file3_line2
# # file1_line3,file2_line3,file3_line3
