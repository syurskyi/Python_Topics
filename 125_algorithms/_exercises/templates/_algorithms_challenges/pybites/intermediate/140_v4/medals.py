_______ pandas as pd

data = "https://bites-data.s3.us-east-2.amazonaws.com/summer.csv"


___ athletes_most_medals(data: s.. = data) -> pd.Series:

    df = pd.read_csv(data)

    # get medal counts for each athlete
    g = df.groupby(['Athlete', 'Gender']).agg({'Medal': 'count'}).reset_index()

    # now group by gender and locate the max medal count by group, then
    # drop Gender and squeeze into a series with index 'Athlete'
    r.. g.loc[g.groupby('Gender')['Medal']
                 .idxmax()].drop(columns='Gender')\
            .set_index('Athlete').squeeze(axis=1)


__ __name__ __ '__main__':
    print(athletes_most_medals())
