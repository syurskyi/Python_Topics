____ __ _______ p..
____ u__.r.. _______ u..
_______ p.... __ pd
____ i.. _______ c__

data "https://bites-data.s3.us-east-2.amazonaws.com/summer.csv"


___ load_data(data
    dt_file p...j..('/tmp', data.s..('/')[-1])
    __ n.. p...i..(dt_file
        u.. ? dt_file)
    w__ o.. dt_file, _ __ f:
        r.. __.r..(f)


___ athletes_most_medals(data=data
    c__ load_data(data)
    df c__.groupby( 'Gender', 'Athlete' ) 'Medal' .c.. )
    male df.loc 'Men' .nlargest(1)
    female df.loc 'Women' .nlargest(1)
    r.. {r[0]: r[1] ___ r __ c__(male.i..,female.i..}
