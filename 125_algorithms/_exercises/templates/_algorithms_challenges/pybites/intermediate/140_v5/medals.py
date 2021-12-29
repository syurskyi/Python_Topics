____ os _______ path
____ urllib.request _______ urlretrieve
_______ pandas as pd
____ itertools _______ chain

data = "https://bites-data.s3.us-east-2.amazonaws.com/summer.csv"


___ load_data(data):
    dt_file = path.join('/tmp', data.split('/')[-1])
    __ n.. path.isfile(dt_file):
        urlretrieve(data, dt_file)
    with open(dt_file, 'r') as f:
        r.. pd.read_csv(f)


___ athletes_most_medals(data=data):
    csv = load_data(data)
    df = csv.groupby(['Gender', 'Athlete'])['Medal'].c.. )
    male = df.loc['Men'].nlargest(1)
    female = df.loc['Women'].nlargest(1)
    r.. {r[0]: r[1] ___ r __ chain(male.items(),female.items())}
