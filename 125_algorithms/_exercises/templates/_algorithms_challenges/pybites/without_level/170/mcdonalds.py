_______ pandas __ pd

data = "https://s3.us-east-2.amazonaws.com/bites-data/menu.csv"
# load the data in once, functions will use this module object
df = pd.read_csv(data)

pd.options.mode.chained_assignment = N..  # ignore warnings


___ get_food_most_calories(df=df
    """Return the food "Item" string with most calories"""
    r.. df[df.Calories __ df.Calories.m..()].iloc[0].Item


___ get_bodybuilder_friendly_foods(df=df, excl_drinks=F..
    """Calulate the Protein/Calories ratio of foods and return the
       5 foods with the best ratio.

       This function has a excl_drinks switch which, when turned on,
       should exclude 'Coffee & Tea' and 'Beverages' from this top 5.

       You will probably need to filter out foods with 0 calories to get the
       right results.

       Return a list of the top 5 foot Item stings."""
    df.drop(df[df.Calories __ 0].index, inplace=T..)

    df 'PC_Ratio'  = df.Protein / df.Calories

    __ excl_drinks:
        df = df[(df.Category != 'Coffee & Tea') & (df.Category != 'Beverages')]

    top_5 = l..(df.sort_values(by= 'PC_Ratio' , ascending=F..).iloc[0:5].Item)

    r.. top_5
