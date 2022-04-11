____ dataclasses _______ astuple, r..

_______ p__

____ dc _______ Bite


?p__.f..()
___ bites
    b1 Bite(number=1, title="sum of numbers")
    b2 Bite(number=2, title="a second bite", level="Intermediate")
    b3 Bite(number=3, title="a hard bite", level="Advanced")
    bites [b1, b2, b3]
    r.. bites


___ test_type_annotations
    ... Bite.__annotations__ __ {'number': i.., 'title': s.., 'level': s..}


___ test_getting_str_for_free(bites
    e.. Bite(number=1, title='Sum of numbers', level='Beginner')
    ... bites[0] __ e..


___ test_default_level_arg_first_bite(bites
    ... bites[0].level __ 'Beginner'


___ test_attribute_access_second_bite(bites
    ... bites[1].number __ 2
    # title should get capitalized (use the __post_init__ method)
    ... bites[1].title __ 'A second bite'
    ... bites[1].level __ 'Intermediate'


___ test_my_data_class_is_mutable(bites
    b3 bites[-1]
    ... b3.level __ 'Advanced'
    # named tuples are immutable so would not allow this:
    b3 r..(b3, level='super hard')
    ... b3.level __ 'super hard'


___ test_can_order_bites(bites
    # not out of the box, need to set something on the data class ...
    sorted_bites s..(bites, r.._T..
    ... sorted_bites[0].number __ 3
    ... sorted_bites[-1].number __ 1


___ test_data_class_are_not_hashable(bites
    # this would work if namedtuples, but Bites are data classes here
    w__ p__.r.. T..
        s..(bites)


___ test_data_class_can_only_be_unpacked_when_casted_to_tuple(bites
    w__ p__.r.. T..
        number, title, level bites[0]
    # but this works:
    number, title, level astuple(bites[0])
    ... number __ 1
    ... level __ 'Beginner'
