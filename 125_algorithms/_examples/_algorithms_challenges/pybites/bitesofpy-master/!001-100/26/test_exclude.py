from exclude import filter_bites, exclude_bites


def test_filter_bites():
    result = filter_bites()
    a__ type(result) == dict
    a__ len(result) == 10
    for bite in exclude_bites:
        a__ bite not in result, f'Bite {bite} should not be in result'