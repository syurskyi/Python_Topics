_______ pandas __ pd

data = "https://bites-data.s3.us-east-2.amazonaws.com/summer.csv"


___ athletes_most_medals(data: s.. = data) __ pd.Series:
    df = pd.read_csv(data)
    men = df[df["Gender"] __ "Men"]
    women = df[df["Gender"] __ "Women"]

    medal_dict    # dict
    woman_name, woman_count = women["Athlete"].value_counts().index[0], women["Athlete"].value_counts()[0]
    man_name, man_count = men["Athlete"].value_counts().index[0], men["Athlete"].value_counts()[0]
    medal_dict[woman_name] = woman_count
    medal_dict[man_name] = man_count
    r.. medal_dict


__ _______ __ _______
    print(athletes_most_medals())