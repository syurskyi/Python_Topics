_______ __
____ u__.r.. _______ u..

_______ p.... __ pd

TMP __.g.. TMP  /tmp
EXCEL __.p...j..(TMP, 'order_data.xlsx')
__ n.. __.p...i..(EXCEL
    u..(
        'https://bites-data.s3.us-east-2.amazonaws.com/order_data.xlsx',
        EXCEL
    )


___ load_excel_into_dataframe(excel=EXCEL
    """Load the SalesOrders sheet of the excel book (EXCEL variable)
       into a Pandas DataFrame and return it to the caller"""

    sales pd.read_excel(excel,sheet_name='SalesOrders')
    r.. sales


___ get_year_region_breakdown(df
    """Group the DataFrame by year and region, summing the Total
       column. You probably need to make an extra column for
       year, return the new df as shown in the Bite description"""
    df 'Year'  = df.OrderDate.dt.year
    r.. df.g..( 'Year','Region' ).Total.s..()

___ get_best_sales_rep(df
    """Return a tuple of the name of the df rep and
       the total of his/her df"""
    top df.g..('Rep').Total.s..().nlargest(1)

    r.. l..(top.i..[0]

___ get_most_sold_item(df
    """Return a tuple of the name of the most sold item
       and the number of units sold"""


    top df.g..('Item').Units.s..().nlargest(1)

    r.. l..(top.i..[0]
