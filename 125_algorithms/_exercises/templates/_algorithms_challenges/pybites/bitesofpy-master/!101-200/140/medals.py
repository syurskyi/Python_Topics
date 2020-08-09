from os ______ path
from urllib.request ______ urlretrieve
______ pandas as pd
from itertools ______ chain

data = "https://bites-data.s3.us-east-2.amazonaws.com/summer.csv"


___ load_data(data
    dt_file = path.join('/tmp', data.split('/')[-1])
    __ not path.isfile(dt_file
        urlretrieve(data, dt_file)
    with open(dt_file, 'r') as f:
        r_ pd.read_csv(f)


___ athletes_most_medals(data=data
    csv = load_data(data)
    df = csv.groupby(['Gender', 'Athlete'])['Medal'].count()
    male = df.loc['Men'].nlargest(1)
    female = df.loc['Women'].nlargest(1)
    r_ {r[0]: r[1] ___ r in chain(male.items(),female.items())}
