# extended_dicts.py

_____ c.. _______ U..

c_ ExtendedDict_dict d..
    ___ apply a..
        ___ ? ? __ .i..
            ____ ?  ? ?

    ___ remove k..
        d.. ____ ?

    ___ is_empty
        r_ l..  __ 0

c_ ExtendedDict_UserDict U..
    ___ apply a..
        ___ ? ? __ .i..
            ____ ?  ? ?

    ___ remove k..
        d.. ____ ?

    ___ is_empty
        r_ l.. __ 0

_______ timeit
_____ extended_dicts _______ ExtendedDict_dict
_____ extended_dicts _______ ExtendedDict_UserDict

init_data = dict(zip(range(1000), range(1000)))

dict_initialization = min(
    timeit.repeat(
        stmt="ExtendedDict_dict(init_data)",
        number=1000,
        repeat=5,
        globals=globals(),
    )
)

user_dict_initialization = min(
    timeit.repeat(
        stmt="ExtendedDict_UserDict(init_data)",
        number=1000,
        repeat=5,
        globals=globals(),
    )
)

print(
    f"UserDict is {user_dict_initialization / dict_initialization:.3f}",
    "times slower than dict",
)
# UserDict is 35.877 times slower than dict

extended_dict = ExtendedDict_dict(init_data)
dict_apply = min(
    timeit.repeat(
        stmt="extended_dict.apply(lambda x: x**2)",
        number=5,
        repeat=2,
        globals=globals(),
    )
)

extended_user_dict = ExtendedDict_UserDict(init_data)
user_dict_apply = min(
    timeit.repeat(
        stmt="extended_user_dict.apply(lambda x: x**2)",
        number=5,
        repeat=2,
        globals=globals(),
    )
)

print(
    f"UserDict is {user_dict_apply / dict_apply:.3f}",
    "times slower than dict",
)
# UserDict is 1.704 times slower than dict
