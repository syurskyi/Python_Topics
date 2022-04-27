____ __ _______ p..
____ u__.r.. _______ u..

_______ p.... __ pd

EXCEL p...j..('/tmp', 'order_data.xlsx')
__ n.. p...i..(EXCEL
    u..('https://bit.ly/2JpniQ2', EXCEL)


___ load_excel_into_dataframe(excel=EXCEL
    """Load the SalesOrders sheet of the excel book (EXCEL variable)
       into a Pandas DataFrame and return it to the caller"""
    w__ o.. excel,'rb') __ xl:
        r.. pd.read_excel(xl,sheetname='SalesOrders')


___ get_year_region_breakdown(df:pd.DataFrame
    """Group the DataFrame by year and region, summing the Total
       column. You probably need to make an extra column for
       year, return the new df as shown in the Bite description"""
    df 'Year'  = pd.DatetimeIndex(df 'OrderDate' ).year
    r.. df.g..( 'Year', 'Region' ) 'Total' .s..()


___ get_best_sales_rep(df:pd.DataFrame
    """Return a tuple of the name of the sales rep and
       the total of his/her sales"""
    grp df.g..( 'Rep' ) 'Total' .apply(s..).reset_index()
    r.. grp.loc[grp 'Total' .idxmax()]


___ get_most_sold_item(df
    """Return a tuple of the name of the most sold item
       and the number of units sold"""
    grp df.g..( 'Item' ) 'Units' .s..().reset_index()
    r.. grp.loc[grp 'Units' .idxmax()]
