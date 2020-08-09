______ pytest

from account ______ Account

acc = Account('bob', 10)


___ test_wrong_type(
    with pytest.raises(TypeError
        Account('bob', 'spam')
    with pytest.raises(ValueError
        Account('bob', -10)
    assert acc.start_balance __ 10


___ test_deleter(
    with pytest.raises(AttributeError
        del acc.start_balance


___ test_can_still_set_int_attr(
    acc._start_balance = 100
    assert acc.start_balance __ 100


___ test_balance(
    acc2 = Account('Tim', 100)
    assert acc2.start_balance __ 100
    acc2 += 25
    acc2 -= 100
    acc2 += 50
    acc2 -= 10
    assert acc2.balance __ 65
    assert le.(acc2) __ 4


___ test_type_checking_on_isub_iadd(
    acc2 = Account('Tim', 100)
    with pytest.raises(TypeError
        acc2 += 'foo'
    with pytest.raises(TypeError
        acc2 -= 'bar'


__ __name__ __ '__main__':
    pytest.main()
