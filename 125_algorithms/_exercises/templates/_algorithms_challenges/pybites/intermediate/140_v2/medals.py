import pandas as pd

data = "https://bites-data.s3.us-east-2.amazonaws.com/summer.csv"


___ athletes_most_medals(data=data):

    medals = pd.read_csv(data)


    medal_counts = medals.groupby(['Gender','Athlete']).size()
    return medal_counts.groupby(level=0).nlargest(1).reset_index(level=[0,1],drop=True)








__ __name__ == "__main__":

    athletes_most_medals()
