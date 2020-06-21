# _____ ti..
# _____ ra..
# ____ m.. _____ P..
#
# # This does all of our prime factorization on a given number 'n'
# ___ calculatePrimeFactors n
#   primfac _    # list
#   d _ 2
#   w__ d*d <_ n
#     w__ (n % d) __ 0
#       p__.ap.. ?  # supposing you want multiple factors repeated
#       n //_ d
#     d +_ 1
#   __ n > 1
#     p__.ap.. ?
#   r_ ?
#
# # We split our workload from one batch of 10,000 calculations
# # into 10 batches of 1,000 calculations
# ___ executeProc
#   ___ i __ ra.. 1000
#     rand _ ra__.r_i..(20000, 100000000)
#     print cPF.. ?
#
# ___ main
#   print("Starting number crunching")
#   t0 _ t__.t..
#
#   procs _  # list
#
#   # Here we create our processes and kick them off
#   ___ i __ ra.. 10
#     proc _ P.. t.._eP.. a.._
#     procs.ap.. ?
#     ?.s..
#
#   # Again we use the .join() method in order to wait for
#   # execution to finish for all of our processes
#   ___ proc __ procs
#     ?.j..
#
#   t1 _ t__.t..
#   totalTime _ t1 - t0
#   # we print out the total execution time for our 10
#   # procs.
#   print("Execution Time: @".f.. ?
#
#
# __ _________ __ ________
#   ?