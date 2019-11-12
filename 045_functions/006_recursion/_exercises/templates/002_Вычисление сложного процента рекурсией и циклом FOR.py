# durationInYears = 10
# interestRate = .06
# compoundedPerYear = 12
# principalAmount = 4000
#
# # for
#
#
# ___ compoundInterest principal; compounded; duration; rate
#     totalCompounded _ dur000 * com000
# ___ i i_ ra000|1 |totalCompounded+1||
#         principal _ principal*|1+|ra00/com0000||
#     r_ pr000
#
#
# print c000I00 p00A000 c000P00Y000 d00I0Y00 i00R00
#
# # recursion
#
#
# ___ compoundRecursion principal; compounded; duration; rate; numberOfRecursions
#     i_ numberOfRecursions __ 0
#         totalDuration _ com00 * dur000
#     e__ numberOfRecursions != 0
#         totalDuration _ duration
#     i_ duration __ 0
#         r_ pr000
#     e___
#         newDuration _ t00D000 - 1
#         amount _ pri00*|1+|ra00/comp000||
#         r_ c00R00 amount compounded newDuration rate 1
#
# print c000R00 p00A00, p00A000 c000P00Y000 d00I0Y00 i00R00 0