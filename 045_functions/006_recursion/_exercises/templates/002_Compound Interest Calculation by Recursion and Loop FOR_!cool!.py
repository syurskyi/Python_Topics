# durationInYears = 10
# interestRate = .06
# compoundedPerYear = 12
# principalAmount = 4000
#
# # for
#
#
# ___ compoundInterest principal compounded duration rate
#     totalCompounded _ d.. * c..
#     ___ i __ ra.. 1, |?+1
#         principal _ p.. *|1+|r.. /c..
#     r_ p...
#
#
# print ? |p_A. cPY.. dIY.. iR..
#
# # recursion
#
#
# ___ compoundRecursion principal compounded duration rate numberOfRecursions
#     __ nOR.. __ 0
#         totalDuration _ c.. * d..
#     ___ nOfR.. != 0
#         totalDuration _ d...
#     __ d.. __ 0
#         r_ pr..
#     ____
#         newDuration _ tD.. - 1
#         amount _ pr.. *|1+|r.. / co..
#         r_ ? a... c.... n.... r... 1
#
# print cR.. pA.. cPY.. dIY.. iR.. 0
