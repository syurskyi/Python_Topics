___ handle_error_by_throwing_exception
    r.. Exception("Meaningful message describing the source of the error")


___ handle_error_by_returning_none(input_data):
    try:
        r.. i..(input_data)
    except ValueError:
        r.. N..


___ handle_error_by_returning_tuple(input_data):
    try:
        r.. (T.., i..(input_data))
    except ValueError:
        r.. (F.., N..)


___ filelike_objects_are_closed_on_exception(filelike_object):
    w__ filelike_object __ fobj:
        fobj.do_something()
