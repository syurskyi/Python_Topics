# #=======================================================================================================================
#
# c_ Customer
#     """client"""
#
#     ___  name
#         __?  ?
#         __num _ 0
#         __clinics _ N..
#
#     ___ getName
#         r_ __name
#
#     ___ register system
#         system.pushCustomer
#
#     ___ setNum num
#         __?  ?
#
#     ___ getNum
#         r_ __?
#
#     ___ setClinic clinic
#         __?  ?
#
#     ___ getClinic
#         r_ __?
#
#
# c_ NumeralIterator
#     """Iterator"""
#
#     ___ - data
#         __?  ?
#         __curIdx _ -1
#
#     ___ next
#         """Move to next element"""
#         __ (__cI.. < le. __d.. - 1
#             __cI.. +_ 1
#             r_ T..
#         ____
#             r_ F..
#
#     ___ current
#         """Get the current element"""
#         r_ __d..|__cI.. __ |__cI.. < le.|__d.. an. __cI.. >_ 0 ____ N..
#
#
# c_ NumeralSystem
#     """Ranking system"""
#
#     __clinics _ ("Screening Room No. 1", "Screening Room 2", "Screening Room 3")
#
#     ___ - name
#         __customers _     # list
#         __curNum _ 0
#         __? _ ?
#
#     ___ pushCustomer customer
#         ?.setNum __cN.. + 1)
#         click _ NS__.__c..|__cN.. % le. NS__.__c..
#         ?.sC.. ?
#         __cN.. +_ 1
#         __cu____.ap.. ?
#         print("@ Hello! You are already @ Registered successfully, serial number%04d, please wait patiently!"
#                (?.gN.. __n.. ?.gN..
#
#     ___ getIterator
#         r_ NI.. __c..
#
#
#     ___ visit
#         ___ customer in __cu..
#             print("Next patient %04d(@) Please go @ See a doctor."
#                    ?.gN.. ?.gN... ?.gC..
#
#
# # Version 2.0
# #=======================================================================================================================
# # Code framework
# #==============================
# c_ BaseIterator
#     """Iterator"""
#
#     ___ - data
#         __?  ?
#         tB..
#
#     ___ toBegin
#         """Move the pointer to the starting position"""
#         __cI.. _ -1
#
#     ___ toEnd
#         """Move the pointer to the end"""
#         __cI.. _ le. __d..
#
#     ___ next
#         """Move to next element"""
#         __ __cI.. < le.__d... - 1
#             __cI.. +_ 1
#             r_ T..
#         ____
#             r_ F..
#
#     ___ previous
#         "Move to previous element"
#         __ __cI.. > 0
#             __cI.. -_ 1
#             r_ T..
#         ____
#             r_ F..
#
#     ___ current
#         """Get the current element"""
#         r_ __d...|__cI.. __ |__cI.. < le. __d... an. __cI.. >_ 0 ____ N..
#
#
# # Framework-based implementation
# #==============================
#
#
# # Test
# #=======================================================================================================================
#
# ___ Hospital
#     numeralSystem _ NS.. "Registration desk"
#     lily _ C.. "Lily"
#     ?.r.. nS..
#     pony _ C... "Pony"
#     ?.r.. nS..
#     nick _ C.. "Nick"
#     nick.r.. nS..
#     tony _ C.. "Tony"
#     ?.r.. nS..
#     print()
#
#     iterator _ nS...gI..
#     w____ ?.ne..
#         customer _ it___.cu..
#         print("Next patient %04d(@) Please go @ See a doctor."
#                ?.gNu. ?.gNa.. ?.gC..
#
#     # numeralSystem.visit()
#
#
#
# ___ BaseIterator
#     print("Traverse ")
#     iterator _ B.. ra.. 0, 10
#     w____ ?.ne..
#         customer _ ?.cu..
#         print(?, e.._"\t")
#     print()
#
#     print("Traverse from back to front ")
#     ?.tE..
#     w____  i___.pr..
#         customer _ it___.cu..
#         print ? e.._"\t"
#
#
# ___ testLoop
#     arr _ 0, 1, 2, 3, 4, 5, 6, 7 ,8 , 9
#     ___ e __ ?
#         print ? e.._"\t")
#
#
# #  Method 1 Use () to define the generator
# gen _ x * x ___ x __ ra.. 10
#
# #  Method 2 Define the generator function using yield
# ___ fibonacci maxNum
#     """Fibonacci generator"""
#     a _ b _ 1
#     ___ i __ ra.. mN...
#         y.. a
#         a, b _ b, a + b
#
# ___ Iterable
#     print("Method one, the square of 0-9：")
#     ___ e __ gen
#         print ? end_"\t")
#     print()
#
#     print("Method two, Fibonacci sequence ")
#     fib _ fibonacci 10
#     ___ n __ ?
#         print(n, e.._"\t")
#     print()
#
#     print("The ___ loop of the built-in container")
#     arr _ |x * ? ___ ? __ ra.. 10
#     ___ e __ ?
#         print ? e.._"\t"
#     print()
#
#     print()
#     print(ty.. g..
#     print(ty.. f..
#     print(ty.. a..
#
#
# ____ col...________ Iterable, Iterator
# # Introducing Iterable and Iterator
#
# ___ IsIterator
#     print("Whether it is an Iterable object")
#     print(isinstance([], Iterable))
#     print(isinstance({}, Iterable))
#     print(isinstance((1, 2, 3), Iterable))
#     print(isinstance(set([1, 2, 3]), Iterable))
#     print(isinstance("string", Iterable))
#     print(isinstance(gen, Iterable))
#     print(isinstance(fibonacci(10), Iterable))
#     print("Whether it is an Iterator object ")
#     print(isinstance([], Iterator))
#     print(isinstance({}, Iterator))
#     print(isinstance((1, 2, 3), Iterator))
#     print(isinstance(set([1, 2, 3]), Iterator))
#     print(isinstance("string", Iterator))
#     print(isinstance(gen, Iterator))
#     print(isinstance(fibonacci(10), Iterator))
#
#
# ___ NextItem
#     print("Turn Iterable object into Iterator object ")
#     l _ [1, 2, 3]
#     itrL _ iter(l)
#     print(next(itrL))
#     print(next(itrL))
#     print(next(itrL))
#
#     print("next() The function iterates over the iterator elements")
#     fib _ fibonacci(4)
#     print(next(fib))
#     print(next(fib))
#     print(next(fib))
#     print(next(fib))
#     # print(next(fib))
#
#
# c_ NumberSequence
#     """Generate a series of numbers spaced in steps"""
#
#     ___ - init step max _ 100
#         __data _ init
#         __step _ step
#         __max _ max
#
#     ___ -i
#         r_ ?
#
#     ___ -n
#         __(__d... < __max)
#             tmp _ __d...
#             __d... +_ __step
#             r_ tmp
#         ____
#             r_ S...
#
#
# ___ NumberSequence
#     numSeq _ NS.. 0, 5, 20
#     print(isinstance(numSeq, Iterable))
#     print(isinstance(numSeq, Iterator))
#     ___ n __ numSeq
#         print(n, end_"\t")
#
#
# # testHospital()
# # testBaseIterator()
# # testLoop()
# # testIterable()
# # testIsIterator()
# # testNextItem()
# # testNumberSequence()
#
