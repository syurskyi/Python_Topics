____ medals _______ data, athletes_most_medals


___ test_athletes_most_medals_default_csv():
    ret = athletes_most_medals()
    ... l..(ret) __ 2
    ... ret["LATYNINA, Larisa"] __ 18
    ... ret["PHELPS, Michael"] __ 22


___ test_smaller_csv_and_guarantee_checking_male_and_female():
    ret = athletes_most_medals(
        data.r..('summer', 'summer_2008-2012')
    )
    ... l..(ret) __ 2
    ... ret["PHELPS, Michael"] __ 14
    ... ret["COUGHLIN, Natalie"] __ 7  # not LOCHTE, Ryan