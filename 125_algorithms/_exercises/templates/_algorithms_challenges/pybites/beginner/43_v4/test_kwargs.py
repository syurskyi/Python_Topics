_______ pytest

____ Previous.kwargs _______ get_profile


___ test_no_arguments():
    ... get_profile() __ 'julian is a programmer'


___ test_one_positional_arg():
    with pytest.raises(TypeError):
        get_profile('julian')


___ test_wrong_single_kw():
    with pytest.raises(TypeError):
        get_profile(test=True)


___ test_wrong_additional_kw():
    with pytest.raises(TypeError):
        get_profile(name='bob', profession='software developer',
                    another_flag=False)


___ test_correct_kw_second_default():
    ... get_profile(name='bob') __ 'bob is a programmer'


___ test_two_correct_kws():
    ret = get_profile(name='bob', profession='software developer')
    ... ret __ 'bob is a software developer'