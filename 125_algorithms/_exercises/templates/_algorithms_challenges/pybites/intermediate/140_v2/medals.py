_______ p.... __ pd

data "https://bites-data.s3.us-east-2.amazonaws.com/summer.csv"


___ athletes_most_medals(data=data

    medals __.r..(data)


    medal_counts medals.g..( 'Gender','Athlete' ).size()
    r.. medal_counts.g..(level=0).nlargest(1).reset_index(level=[0,1],drop=T..)








__ _______ __ _______

    athletes_most_medals()
