from medals import data, athletes_most_medals


def test_athletes_most_medals_default_csv():
    ret = athletes_most_medals()
    a__ len(ret) == 2
    a__ ret["LATYNINA, Larisa"] == 18
    a__ ret["PHELPS, Michael"] == 22


def test_smaller_csv_and_guarantee_checking_male_and_female():
    ret = athletes_most_medals(
        data.replace('summer', 'summer_2008-2012')
    )
    a__ len(ret) == 2
    a__ ret["PHELPS, Michael"] == 14
    a__ ret["COUGHLIN, Natalie"] == 7  # not LOCHTE, Ryan