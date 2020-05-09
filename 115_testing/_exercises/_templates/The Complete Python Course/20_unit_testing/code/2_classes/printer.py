# c_ PrinterError R..
#     p..
#
#
# c_ Printer
#     ___ -  pages_per_s in. capacity in.
#         p.. _ p..
#         _c... _ c..
#
#     ___ print  pages
#         __ ? > _c...
#             r____ P... Printer does not have enough capacity for all these pages.
#
#         _capacity -= pages
#
#         r_ _ Printed |pages| pages in |pages/____.pages_per_s:.2f| seconds.'