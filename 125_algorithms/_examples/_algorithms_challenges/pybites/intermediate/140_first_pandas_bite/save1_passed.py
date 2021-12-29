import pandas as pd

data = "https://bites-data.s3.us-east-2.amazonaws.com/summer.csv"


def athletes_most_medals(data=data):
    df = pd.read_csv(data)

    df_grouped = df.groupby(['Athlete', 'Gender']).count()
    df_grouped = df_grouped['Medal'].reset_index()

    mens = df_grouped[df_grouped['Gender'] == 'Men'].\
        sort_values(by='Medal', ascending=False).head(1)
    womens = df_grouped[df_grouped['Gender'] == 'Women'].\
        sort_values(by='Medal', ascending=False).head(1)

    output = pd.merge(mens, womens, how='outer')[['Athlete', 'Medal']].\
        set_index('Athlete')
    output = output['Medal']
    output.index.name = None

    return output.to_dict()