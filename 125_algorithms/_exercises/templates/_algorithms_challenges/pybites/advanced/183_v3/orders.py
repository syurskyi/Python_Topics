# _______ __
# ____ u__.r.. _______ u..
#
# _______ p.... __ pd
#
# TMP __.g.. TMP  /tmp
# EXCEL __.p...j.. ? 'order_data.xlsx'
# __ n.. __.p...i.. ?
#     u..
#         'https://bites-data.s3.us-east-2.amazonaws.com/order_data.xlsx',
#         ?
#
#
#
# ___ load_excel_into_dataframe excel_?
#     """Load the SalesOrders sheet of the excel book (EXCEL variable)
#        into a Pandas DataFrame and return it to the caller"""
#     r.. _.r.. ? sheet_name_ SalesOrders
#
#
# ___ get_year_region_breakdown df
#     """Group the DataFrame by year and region, summing the Total
#        column. You probably need to make an extra column for
#        year, return the new df as shown in the Bite description"""
#     df ?.c..
#     df Year  _ __.O...d_.y..
#     r.. ?.g.. Year Region .a.. Total : sum
#
#
# ___ get_best_sales_rep df
#     """Return a tuple of the name of the sales rep and
#        the total of his/her sales"""
#     reps __.g.. Rep .a.. Total : sum .r..
#
#     r.. t.. >.s.. b._ Total  a.._F.. i.. 0
#
#
# ___ get_most_sold_item df
#     """Return a tuple of the name of the most sold item
#        and the number of units sold"""
#     items ?.g.. Item .a.. Units : sum .r..
#     r.. t.. ?.s.. b._ Units a.._ F.. i.. 0
