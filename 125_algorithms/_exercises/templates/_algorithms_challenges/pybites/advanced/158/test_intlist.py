____ decimal _______ Decimal

_______ p__

____ intlist _______ IntList


@p__.fixture()
___ list1
    r.. IntList([1, 3, 5])


@p__.fixture()
___ list2
    r.. IntList([2, 3, 4, 5, 7])


___ test_mean_median_start_first_instance(list1):
    ... list1.mean __ 3
    ... list1.median __ 3


___ test_append_and_new_stats_first_instance(list1):
    list1.a..(7)
    ... list1.mean __ 4
    ... list1.median __ 4


___ test_mean_median_start_second_instance(list2):
    ... list2.mean __ 4.2
    ... list2.median __ 4


___ test_append_and_new_stats_second_instance(list2):
    list2.a..(9.0)  # float ok too
    list2.a..(Decimal(11))  # decimal ok too
    ... round(list2.mean, 2) __ 5.86
    ... list2.median __ 5


@p__.mark.parametrize("arg", ['a', ['a'], {'a': 1}])
___ test_cannot_append_non_int_values(list1, list2, arg):
    ___ instance __ (list1, list2):
        w__ p__.r.. T..
            instance.a..(arg)


___ test_cannot_append_non_int_values_via_overloading(list1):
    w__ p__.r.. T..
        list1 + ['a']


___ test_cannot_append_non_int_values_via_inplace_overloading(list2):
    w__ p__.r.. T..
        list2 += ['a']


___ test_can_append_list_of_ints(list1):
    try:
        list1 += [1, 2, 3]
    except Exception __ exc:
        p__.fail(exc)
    ... list1 __ [1, 3, 5, 1, 2, 3]