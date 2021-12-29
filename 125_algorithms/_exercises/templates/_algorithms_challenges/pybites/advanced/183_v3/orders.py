_______ os
____ urllib.request _______ urlretrieve

_______ pandas as pd

TMP = os.getenv("TMP", "/tmp")
EXCEL = os.path.join(TMP, 'order_data.xlsx')
__ n.. os.path.isfile(EXCEL):
    urlretrieve(
        'https://bites-data.s3.us-east-2.amazonaws.com/order_data.xlsx',
        EXCEL
    )


___ load_excel_into_dataframe(excel=EXCEL):
    """Load the SalesOrders sheet of the excel book (EXCEL variable)
       into a Pandas DataFrame and return it to the caller"""
    r.. pd.read_excel(excel, sheet_name='SalesOrders')


___ get_year_region_breakdown(df):
    """Group the DataFrame by year and region, summing the Total
       column. You probably need to make an extra column for
       year, return the new df as shown in the Bite description"""
    df = df.copy()
    df['Year'] = df.OrderDate.dt.year
    r.. df.groupby(['Year', 'Region']).agg({'Total': 'sum'})


___ get_best_sales_rep(df):
    """Return a tuple of the name of the sales rep and
       the total of his/her sales"""
    reps = df.groupby(['Rep']).agg({'Total': 'sum'}).reset_index()

    r.. tuple(reps.sort_values(by='Total', ascending=False).iloc[0])


___ get_most_sold_item(df):
    """Return a tuple of the name of the most sold item
       and the number of units sold"""
    items = df.groupby(['Item']).agg({'Units': 'sum'}).reset_index()
    r.. tuple(items.sort_values(by='Units', ascending=False).iloc[0])
