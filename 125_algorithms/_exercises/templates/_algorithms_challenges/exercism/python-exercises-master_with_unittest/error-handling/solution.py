___ handle_error_by_throwing_exception
    r.. E..("Meaningful message describing the source of the error")


___ handle_error_by_returning_none(input_data
    ___
        r.. i..(input_data)
    ______ V..
        r.. N..


___ handle_error_by_returning_tuple(input_data
    ___
        r.. (T.., i..(input_data))
    ______ V..
        r.. (F.., N..)


___ filelike_objects_are_closed_on_exception(filelike_object
    w__ filelike_object __ fobj:
        fobj.do_something()
