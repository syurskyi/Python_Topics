______ u__
____ u__.m.. ______ MagicMock
______ sample

c_ TestAdd?.?
    ___ setUp
        org_summation_method _ sample.summation
        sample.summation _ MagicMock()
        sample.summation.return_value _ 3

    ___ tearDown
        sample.summation _ org_summation_method

    ___ test_add
        result _ sample.add(1,5)
        aE..(result, 3)

    ___ test_exception
        sample.summation.side_effect _ E..
        aR..(E.., sample.add,1,5)


__ _____ __ ______
    ?.?
