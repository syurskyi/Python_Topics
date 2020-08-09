from exclude ______ filter_bites, exclude_bites


___ test_filter_bites(
    result = filter_bites()
    assert type(result) __ dict
    assert le.(result) __ 10
    for bite in exclude_bites:
        assert bite not in result, f'Bite {bite} should not be in result'