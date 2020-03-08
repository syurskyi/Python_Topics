# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
#
# """
# http://web.archive.org/web/20120309135549/http://dpip.testingperspective.com/?p_28
#
# *TL;DR80
# Encapsulates how a set of objects interact.
# """
#
# ______ ra..
# ______ ti__
#
#
# c_ TC
#
#     ___ -
#         _tm _ N...
#         _bProblem _ 0
#
#     ___ setup
#         print("Setting up the Test")
#         ti__.sl.. 0.1
#         _tm.pR..
#
#     ___ execute
#         __ no. _bP...
#             print("Executing the test")
#             ti__.sl..0.1
#         ____
#             print("Problem in setup. Test no. executed.")
#
#     ___ tearDown
#         __ no. _bP...
#             print("Tearing down")
#             ti__.sl.. 0.1
#             _t_.pR..
#         ____
#             print("Test no. executed. No tear down required.")
#
#     ___ setTM tm
#         _t_ _ tm
#
#     ___ setProblem value
#         _bP... _ ?
#
#
# c_ Reporter
#
#     ___ -
#         _tm _ N...
#
#     ___ prepare
#         print("Reporter Class is preparing to report the results")
#         ti__.sl.. 0.1
#
#     ___ report
#         print("Reporting the results of Test")
#         ti__.sl.. 0.1
#     ___ setTM  tm
#         _t_ _ ?
#
#
# c_ DB
#
#     ___ -
#         _tm _ N...
#
#     ___ insert
#         print("Inserting the execution begin status in the Database")
#         ti__.sl.. 0.1
#         # Following code is to simulate a communication from DB to TC
#         __ ra___.r_r.. 1 4 __ 3
#             r_ -1
#
#     ___ update
#         print("Updating the test results in Database")
#         ti__.sl.. 0.1
#
#     ___ setTM tm
#         _t_ _ tm
#
#
# c_ TestManager
#
#     ___ -
#         _reporter _ N...
#         _db _ N...
#         _tc _ N...
#
#     ___ prepareReporting
#         rvalue _ _d_.in..
#         __ ? __ -1
#             _t_.sP.. 1
#             _r___.pr..
#
#     ___ setReporter reporter
#         _?  ?
#
#     ___ setDB db
#         _?  ?
#
#     ___ publishReport
#         _d_.up..
#         _r____.re..
#
#     ___ setTC tc
#         _?  ?
#
#
# __ _______ __ ______
#     reporter _ R...
#     db _ ?
#     tm _ ?
#     ?.sR.. r..
#     ?.sD. d_
#     r___.sT_ t_
#     d_.sT_ t_
#     # For simplification we are looping on the same test.
#     # Practically, it could be about various unique test classes and their
#     # objects
#     ___ i __ ra.. 3
#         tc _ T..
#         ?.sT. t_
#         t_.sT_ t_
#         ?.s..
#         ?.e..
#         ?.tD..
#
# ### OUTPUT ###
# # Setting up the Test
# # Inserting the execution begin status in the Database
# # Executing the test
# # Tearing down
# # Updating the test results in Database
# # Reporting the results of Test
# # Setting up the Test
# # Inserting the execution begin status in the Database
# # Reporter Class is preparing to report the results
# # Problem in setup. Test no. executed.
# # Test no. executed. No tear down required.
# # Setting up the Test
# # Inserting the execution begin status in the Database
# # Executing the test
# # Tearing down
# # Updating the test results in Database
# # Reporting the results of Test
