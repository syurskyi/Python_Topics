# ____ __ _______ p..
# ____ u__.r.. _______ u..
#
# _______ p.... __ pd
#
# EXCEL p...j.. '/tmp', 'order_data.xlsx'
# __ n.. p...i.. ?
#     u.. 'https://bit.ly/2JpniQ2' ?
#
#
# ___ load_excel_into_dataframe excel_?
#     """Load the SalesOrders sheet of the excel book (EXCEL variable)
#        into a Pandas DataFrame and return it to the caller"""
#     w__ o.. ? __ __ xl
#         r.. __.r.. ? sheetname+ SalesOrders
#
#
# ___ get_year_region_breakdown df __.D..
#     """Group the DataFrame by year and region, summing the Total
#        column. You probably need to make an extra column for
#        year, return the new df as shown in the Bite description"""
#     df 'Year'  = __.D.. ? OrderDate .y..
#     r.. __.g.. Year Region Total .s..
#
#
# ___ get_best_sales_rep df __.D..
#     """Return a tuple of the name of the sales rep and
#        the total of his/her sales"""
#     grp __.g.. Rep Total .a..s.. .r..
#     r.. ?.l.. ?Total .i..
#
#
# ___ get_most_sold_item df
#     """Return a tuple of the name of the most sold item
#        and the number of units sold"""
#     grp __.g.. Item  Units .s.. .r..
#     r.. ?.l.. ? Units .i..
