_______ pandas as pd
XYZ = "https://bites-data.s3.us-east-2.amazonaws.com/xyz.csv"
THRESHOLDS = (5000, 0.05)


___ calculate_flux(XYZ: s..) -> l..:
    """Read the data in from xyz.csv
    add two new columns, one to calculate dollar flux,
    and the other to calculate percentage flux
    return as a list of tuples
    """


    data = pd.read_csv(XYZ,dtype={'12/31/2020': int,'12/31/2019': int})

    data['dollar_flux'] = data.iloc[:,1].sub(data.iloc[:,2])
    data['pct_flux'] = data.iloc[:,[-2,1]].pct_change(axis=1).dropna(axis=1)


    r.. l..(data.to_records(index=False))









___ identify_flux(xyz: l..) -> l..:
    """Load the list of tuples, iterate through
    each item and determine if it is above both
    thresholds. if so, add to the list
    """
    flagged_lines    # list

    ___ line __ xyz:
        *orig,dollar_amount,pct_amount = line
        __ abs(dollar_amount) > THRESHOLDS[0] a.. abs(pct_amount) > THRESHOLDS[1]:
            flagged_lines.a..(line)




    r.. flagged_lines
